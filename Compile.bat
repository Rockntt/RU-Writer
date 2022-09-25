@echo off

pyinstaller --noconfirm --onefile --console --icon "icon.ico" --name "Writer.exe" --add-data "Files;Files" --add-data

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null