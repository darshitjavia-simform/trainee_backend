from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)

# GET: Retrieve all expenses
@app.route("/expenses", methods=["GET"])
def get_expenses():
    expenses = []
    for expense in mongo.db.expenses.find():
        expenses.append({
            "_id": str(expense["_id"]),
            "name": expense["name"],
            "amount": expense["amount"]
        })
    return jsonify(expenses)

# POST: Add a new expense
@app.route("/expense", methods=["POST"])
def add_expense():
    data = request.json
    if not data or "name" not in data or "amount" not in data:
        return jsonify({"error": "Missing required fields"}), 400
        
    try:
        amount = float(data["amount"])
    except ValueError:
        return jsonify({"error": "Amount must be a number"}), 400
        
    new_expense = {
        "name": data["name"],
        "amount": amount
    }
    inserted_id = mongo.db.expenses.insert_one(new_expense).inserted_id
    return jsonify({"message": "Expense added successfully!", "id": str(inserted_id)})

# PUT: Update an existing expense
@app.route("/expense/<expense_id>", methods=["PUT"])
def update_expense(expense_id):
    try:
        data = request.json
        if not data or "name" not in data or "amount" not in data:
            return jsonify({"error": "Missing required fields"}), 400
            
        try:
            amount = float(data["amount"])
        except ValueError:
            return jsonify({"error": "Amount must be a number"}), 400
            
        result = mongo.db.expenses.update_one(
            {"_id": ObjectId(expense_id)},
            {"$set": {"name": data["name"], "amount": amount}}
        )
        
        if result.matched_count == 0:
            return jsonify({"error": "Expense not found"}), 404
            
        return jsonify({"message": "Expense updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# DELETE: Delete an existing expense
@app.route("/expense/<expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    try:
        result = mongo.db.expenses.delete_one({"_id": ObjectId(expense_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Expense not found"}), 404
        return jsonify({"message": "Expense deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
