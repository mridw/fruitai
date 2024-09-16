from flask import Flask, jsonify
from flask_cors import CORS
from routes.faq_routes import faq_bp
from config import get_db

app = Flask(__name__)
CORS(app)  # Enable CORS

# Initialize MongoDB connection
db = get_db()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fruit API!"})

# Register the FAQ routes
app.register_blueprint(faq_bp)

if __name__ == '__main__':
    app.run(debug=True)
