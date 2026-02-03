"""
Resume Analyzer - AI Resume Scoring, ATS Optimization & Job Recommendation System
Flask Server with FastAPI Backend
"""

import os
import sys
from pathlib import Path
from flask import Flask, render_template, url_for, jsonify, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

CORS(app)

# FastAPI Backend URL (running on different port or same server)
FASTAPI_URL = os.getenv('FASTAPI_URL', 'http://localhost:8000')

# Routes
@app.route('/')
def index():
    """Serve the main index page"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    try:
        # Check if FastAPI backend is running
        resp = requests.get(f'{FASTAPI_URL}/', timeout=2)
        return jsonify({'status': 'healthy', 'fastapi': 'running'}), 200
    except:
        return jsonify({'status': 'degraded', 'fastapi': 'unavailable'}), 200

@app.route('/api/resume/upload', methods=['POST'])
def upload_resume():
    """Proxy request to FastAPI backend"""
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        files = {'file': (file.filename, file.stream, file.content_type)}
        resp = requests.post(f'{FASTAPI_URL}/resume/upload', files=files)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/resume/score', methods=['POST'])
def score_resume():
    """Proxy request to FastAPI backend"""
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        files = {'file': (file.filename, file.stream, file.content_type)}
        resp = requests.post(f'{FASTAPI_URL}/resume/score', files=files)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/resume/optimize', methods=['POST'])
def optimize_resume():
    """Proxy request to FastAPI backend"""
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        files = {'file': (file.filename, file.stream, file.content_type)}
        resp = requests.post(f'{FASTAPI_URL}/resume/optimize', files=files)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/jobs/recommend', methods=['POST'])
def recommend_jobs():
    """Proxy request to FastAPI backend"""
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        files = {'file': (file.filename, file.stream, file.content_type)}
        resp = requests.post(f'{FASTAPI_URL}/jobs/recommend', files=files)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user/register', methods=['POST'])
def register_user():
    """Proxy request to FastAPI backend"""
    try:
        data = request.get_json()
        resp = requests.post(f'{FASTAPI_URL}/user/register', json=data)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # For development
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
