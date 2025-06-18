from flask import Flask, request, render_template
import os
import json
import uuid
from datetime import datetime

app = Flask(__name__)
DATA_DIR = "/data"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Generate unique filename
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:6]}.json"
        filepath = os.path.join(DATA_DIR, filename)
        
        # Save as JSON
        with open(filepath, 'w') as f:
            json.dump({
                "title": request.form['title'],
                "description": request.form['description'],
                "content": request.form['content']
            }, f)
        return "Copyable saved!"
    return render_template('index.html')