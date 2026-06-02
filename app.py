from flask import Flask, send_from_directory, abort
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    allowed_extensions = ('.html', '.jpg', '.jfif', '.png', '.css', '.js')
    if not filename.endswith(allowed_extensions):
        abort(404)
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.isfile(file_path):
        return send_from_directory(BASE_DIR, filename)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
