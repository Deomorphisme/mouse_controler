from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pyautogui

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('move')
def handle_move(data):
    deltaX = data['deltaX']
    deltaY = data['deltaY']
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x + deltaX, current_y + deltaY)

@socketio.on('click')
def handle_click():
    pyautogui.click()

@socketio.on('rightClick')
def handle_right_click():
    pyautogui.rightClick()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10270)
