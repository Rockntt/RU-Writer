@echo off
pyinstaller --noconfirm --onefile --console --add-data "C:/Users/kloch/PycharmProjects/Writer/Fonts;Fonts/"  "C:\Users\kloch\PycharmProjects\Writer"

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null