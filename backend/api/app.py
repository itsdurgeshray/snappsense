# app.py
# Backend ka entry point.

from flask import Flask, jsonify  # Flask app banane aur response return karne ke liye
from flask_cors import CORS       # Cross-Origin Requests ko allow karne ke liye
from routes.reviews import reviews_route  # Reviews route import karte hain

app = Flask(__name__)  # Flask app create karte hain
CORS(app)              # CORS ko enable karte hain

# Register the reviews route
app.register_blueprint(reviews_route, url_prefix='/api')  # "/api/reviews" pe accessible hoga

# Base route to check server is working
@app.route('/')
def home():
    return jsonify({"message": "Welcome to SnappSense Backend API"})

# Main function to run the server
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode mein server run karte hain
