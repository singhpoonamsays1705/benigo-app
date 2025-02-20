# app.py

from flask import Flask, jsonify, request
from utils import (
    scrape,
    generate_response_context,
    generate_response_core_intent,
    generate_response_off_intent,
    generate_response_role,
    run_all
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})

@app.route('/scrape', methods=['GET'])
def scrape_route():    
    result = scrape()
    return jsonify(result)

@app.route('/generate_response_context', methods=['GET'])
def generate_response_context_route():
    result = generate_response_context()
    return jsonify(result)

@app.route('/generate_response_core_intent', methods=['GET'])
def generate_response_core_intent_route():
    result = generate_response_core_intent()
    return jsonify(result)

@app.route('/generate_response_off_intent', methods=['GET'])
def generate_response_off_intent_route():
    result = generate_response_off_intent()
    return jsonify(result)

@app.route('/generate_response_role', methods=['GET'])
def generate_response_role_route():
    result = generate_response_role()
    return jsonify(result)

@app.route('/run_all', methods=['POST'])
def run_all_route():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL parameter is required in JSON body'}), 400
    
    url = data['url']
    result = run_all(url)
    return jsonify(result)
