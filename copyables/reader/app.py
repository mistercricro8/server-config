from flask import Flask, render_template
import os
import json

app = Flask(__name__)
DATA_DIR = "/data"

@app.route('/')
def index():
    copyables = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(DATA_DIR, filename), 'r') as f:
                try:
                    data = json.load(f)
                    copyables.append({
                        "filename": filename,
                        "title": data.get("title", "Untitled"),
                        "description": data.get("description", "")
                    })
                except json.JSONDecodeError:
                    continue
    return render_template('index.html', copyables=copyables)

@app.route('/view/<filename>')
def view(filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
    return f"""
    <h1>{data.get('title', 'Untitled')}</h1>
    <p><i>{data.get('description', '')}</i></p>
    <pre>{data.get('content', '')}</pre>
    """