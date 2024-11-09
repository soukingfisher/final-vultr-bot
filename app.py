from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.model import FinancialAdviceModel
from config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET_KEY

db = SQLAlchemy(app)
model = FinancialAdviceModel()  # Load AI/ML model

# Define User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Float, nullable=False)
    advice = db.Column(db.String(200), nullable=True)

with app.app_context():
    db.create_all()

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get financial advice
@app.route('/get-advice', methods=['POST'])
def get_advice():
    user_data = request.json
    name = user_data['name']
    data = float(user_data['data'])

    # Generate advice using AI model
    advice_message = model.generate_advice(data)
    
    # Save user and advice to the database
    user = User(name=name, data=data, advice=advice_message)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": advice_message})

if __name__ == '__main__':
    app.run(debug=True)
