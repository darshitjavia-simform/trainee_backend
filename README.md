# Expense Tracker Application

A full-stack expense tracking application built with React.js and Flask.

## Prerequisites

- Node.js (v14 or higher)
- Python 3.8 or higher
- MongoDB

## Database Configuration

1. Install MongoDB:
   ```bash
   # For Ubuntu
   sudo apt-get install mongodb
   # For macOS using Homebrew
   brew install mongodb-community
   # For Windows
   # Download and install from MongoDB website
   ```

2. Start MongoDB service:
   ```bash
   # For Ubuntu
   sudo service mongodb start
   # For macOS
   brew services start mongodb-community
   # For Windows
   # MongoDB runs as a service automatically
   ```

3. Create database and collection:
   ```bash
   # Open MongoDB shell
   mongosh
   
   # Create and use database
   use expense_tracker
   
   # Create expenses collection
   db.createCollection('expenses')
   
   # Verify setup
   show dbs
   show collections
   ```

4. Test database connection:
   ```bash
   # In MongoDB shell
   db.expenses.insertOne({
     name: "Test Expense",
     amount: 10.00
   })
   ```

## Setup & Installation

### Backend Setup

1. Navigate to backend directory:
```bash
cd trainee_backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-cors flask-pymongo python-dotenv
```

4. Verify MongoDB connection:
```bash
# Check if MongoDB is running
mongo
# Should show connection to mongodb://localhost:27017
```

5. Run the Flask server:
```bash
python app.py
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd trainee_frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

## Features

- View all expenses
- Add new expenses
- Update existing expenses
- Responsive design using Bootstrap
- RESTful API backend
- MongoDB database storage

## Environment Variables

The following environment variables are required:

- `REACT_APP_API_URL`: Backend API URL
- `MONGO_URI`: MongoDB connection string
- `FLASK_APP`: Flask application entry point
- `FLASK_ENV`: Flask environment (development/production)
- `PORT`: Backend server port

## API Endpoints

- GET `/expenses` - Retrieve all expenses
- POST `/expense` - Add new expense
- PUT `/expense/<id>` - Update existing expense

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
