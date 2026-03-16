from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enables Cross-Origin requests to prevent "blocked:origin" errors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve JSON data from the request
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({"error": "Missing name in request"}), 400
        
    name = data.get('name')
    # You can add logic here (e.g., saving to a database)
    return jsonify({
        "status": "success",
        "message": f"Hello {name}, welcome to your Flask App!"
    })

if __name__ == '__main__':
    app.run(debug=True)
