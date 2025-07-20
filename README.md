# mouse_controler
A little script when your wireless mouse turns off.

## To make it work

```zsh
pip clone https://github.com/Deomorphisme/mouse_controler.git
cd mouse_controler

python3 -m venv mouse_ctrl # or mouse_env or whatever_you_want
source mouse_ctrl/bin/activate
pip install --upgrade pip
pip install flask pyautogui flask-socketio

python3 server.py
```

Next, go to `http://<your-computer-ip>:10270` using your mobile web browser and voila!