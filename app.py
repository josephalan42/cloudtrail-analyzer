import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from analyzer import extract_events  # your parser module

# --- Setup ---
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash()

UPLOAD_FOLDER = 'logs'
ALLOWED_EXTENSIONS = {'json', 'gz'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('logfile')

        if not file or file.filename == '':
            flash('No file selected.')
            return redirect(request.url)

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            print("File saved to:", file_path)  # Debug info

            events = extract_events(file_path)
            print("Extracted events:", events)  # Debug info

            return render_template('results.html', events=events)
        else:
            flash('Invalid file type. Please upload a .json or .gz file.')
            return redirect(request.url)

    return render_template('index.html')

# --- Run ---
if __name__ == '__main__':
    app.run(debug=True)
