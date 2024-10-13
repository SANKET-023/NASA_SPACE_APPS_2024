from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import MongoClient
import requests

app = Flask(__name__)
app.secret_key = 'REDACTED'
# MongoDB setup (replace with your MongoDB URI)
client = MongoClient('REDACTED')
db = client['farm_app']
feedback_collection = db['feedback']

# NASA API example URLs (replace with your API keys)
SMAP_API_URL = "REDACTED"
MODIS_API_URL = "REDACTED"
GLAM_API_URL = "REDACTED"


# Landing Page with 3D rotating globe
@app.route('/')
def home():
    return render_template('index.html', title='Farm Dashboard')


# User Input and Map Visualization
@app.route('/map')
def map_page():
    return render_template('map.html', title='Map')


# Crop Suitability Tab - Using NASA APIs (example)
@app.route('/crop-suitability')
def crop_suitability():
    # Example crop suitability data (replace with actual NASA API response)
    crops = [
        {"name": "Drought Resilient Crop", "description": "Best suited for dry areas"},
        {"name": "Heat Resistant Crop", "description": "Can withstand high temperatures"},
        {"name": "Water Intensive Crop", "description": "Needs high precipitation"}
    ]
    return render_template('crop-suitability.html', title='Crop Suitability', crops=crops)


# Feedback Tab
@app.route('/feedback', methods=['GET', 'POST'])
def feedback_page():
    if request.method == 'POST':
        email = request.form.get('email')
        feedback = request.form.get('feedback')
        real_conditions = request.form.get('real_conditions')

        feedback_entry = {
            "email": email,
            "feedback": feedback,
            "real_conditions": real_conditions
        }

        # Insert feedback into MongoDB
        feedback_collection.insert_one(feedback_entry)
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('feedback_page'))

    return render_template('feedback.html', title='Feedback')


# Insights Tab (with example meteorological data from SMAP)
@app.route('/insights')
def insights_page():
    # Example of fetching SMAP data (replace with actual API call)
    lat = request.args.get('lat', default=20.5937)  # Example latitude
    lon = request.args.get('lon', default=78.9629)  # Example longitude

    smap_data = {
        'soil_moisture': 0.35,
        'freeze_thaw': 0.12,
        'precipitation': 50,
        'wind_speed': 5.6,
        'heat': 35
    }

    return render_template('insights.html', title='Weather Insights', smap_data=smap_data)


# API route for fetching SMAP data
@app.route('/get_smap_data')
def get_smap_data():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Example response (replace with API response)
    response = {
        'soil_moisture': 0.35,
        'freeze_thaw': 0.12
    }
    return jsonify(response)


# Climate Guide
@app.route('/climate-guide')
def climate_guide():
    return render_template('climate-guide.html', title='Climate Guide')


if __name__ == '__main__':
    app.run(debug=True)
