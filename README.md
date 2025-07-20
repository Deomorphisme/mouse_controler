# mouse_controler
A little script when your wireless mouse turns off.

## To make it work

```zsh
python3 -m venv mouse_env # or mouse_controler or whatever_you_want
source mouse_env/bin/activate
pip install --upgrade pip
pip install flask pyautogui

python3 server.py
```