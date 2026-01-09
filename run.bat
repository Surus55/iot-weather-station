@echo off
title IoT Weather Station

echo Indul a Mosquitto broker...
start "" "C:\Program Files\mosquitto\mosquitto.exe" -v
timeout /t 2 /nobreak >nul

echo Indul az IoT Publisher...
start "" "C:\Users\Anna\AppData\Local\Programs\Python\Python314\python.exe" "%~dp0mqtt_publisher.py"
timeout /t 1 /nobreak >nul

echo Indul a Dashboard...
start "" "C:\Users\Anna\AppData\Local\Programs\Python\Python314\python.exe" "%~dp0dashboard.py"

echo Minden elindítva. Nyomj meg egy gombot a bezáráshoz.
pause
