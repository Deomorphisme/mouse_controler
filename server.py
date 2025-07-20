from flask import Flask, request, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    deltaX = data['deltaX']
    deltaY = data['deltaY']
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x + deltaX, current_y + deltaY)
    return {'status': 'success'}

@app.route('/click', methods=['POST'])
def click():
    pyautogui.click()
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10270)
