from os import environ
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import gunicorn

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is my secret key"
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

# delivers payload as a string
@socketio.on("connect", namespace="/test")
def test_connect():
    emit("my connection", {"data": "Connected"})

# delivers payload in JSON
@socketio.on("my new message", namespace="/test")
def test_message(message):
    emit("new message", {"data": message["data"]}, broadcast = True)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    socketio.run(app, host=HOST, port=PORT)
