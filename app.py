from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import os
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

FILE_DIRECTORY = "files"  # Folder containing files to be shared
os.makedirs(FILE_DIRECTORY, exist_ok=True)

def get_files():
    files = []
    for filename in os.listdir(FILE_DIRECTORY):
        filepath = os.path.join(FILE_DIRECTORY, filename)
        if os.path.isfile(filepath):
            file_info = {
                'name': filename,
                'size': f"{os.path.getsize(filepath) / 1024:.2f} KB",
                'modified': os.path.getmtime(filepath)
            }
            files.append(file_info)
    files.sort(key=lambda x: x['modified'], reverse=True)
    return files

@app.route('/')
def index():
    return render_template('index.html', files=get_files())

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(FILE_DIRECTORY, filename, as_attachment=True)

# Function to watch the folder and notify clients
def watch_folder():
    last_files = set(os.listdir(FILE_DIRECTORY))
    while True:
        time.sleep(2)  # Check every 2 seconds
        current_files = set(os.listdir(FILE_DIRECTORY))
        if current_files != last_files:
            socketio.emit('update')  # Notify clients
            last_files = current_files

# Run the folder watcher in a separate thread
threading.Thread(target=watch_folder, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
