from flask import Flask, request, jsonify, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder="../frontend/dist/frontend")
# The static_folder parameter specifies the directory from which static files will be served.
# In this case, it points to the "dist/frontend" directory inside the "frontend" folder.
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test_swe_database"
mongo = PyMongo(app)
CORS(app)

@app.route('/')
def serve_angular():
    # Adjust the path if your Angular build folder is actually "dist/frontend"
    return send_from_directory('../frontend/dist/frontend', 'index.html')


@app.route("/test_mongodb")
def test_mongodb():
    try:
        # Attempt to fetch a document from the database
        test_doc = mongo.db.test.find_one()
        if (test_doc):
            return jsonify({"message": "MongoDB is connected!", "document": str(test_doc)}), 200
        else:
            return jsonify({"message": "MongoDB is connected, but no test document found."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/register", methods=["POST"])
def register():
    user_data = request.json
    # Add code to hash password and save user to MongoDB
    return jsonify({"message": "User registered successfully"}), 201

@app.route("/api/login", methods=["POST"])
def login():
    user_data = request.json
    # Add code to verify user credentials
    return jsonify({"message": "Login successful"}), 200

@app.route("/create_test_document")
def create_test_document():
    try:
        # Insert a test document
        test_document = {"name": "Test User", "email": "test@example.com"}
        result = mongo.db.test.insert_one(test_document)

        return jsonify({
            "message": "Test document created successfully",
            "document_id": str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"message": "Flask backend is connected!"})

if __name__ == "__main__":
    app.run(debug=True)
