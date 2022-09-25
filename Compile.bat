@echo off
pyinstaller --noconfirm --onedir --console  "writer.py"

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null