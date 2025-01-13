@echo off
call .\venv\Scripts\activate.bat
pip install pandas
pip install PySide6
python mainwindow.py
pause