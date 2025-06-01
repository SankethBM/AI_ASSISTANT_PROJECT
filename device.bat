@echo off
echo Disconnecting old connections...
"C:\platform-tools\adb.exe" disconnect
echo Setting up connected device
"C:\platform-tools\adb.exe" tcpip 5555
echo Waiting for device to initialize
timeout 3
FOR /F "tokens=2" %%G IN ('"C:\platform-tools\adb.exe" shell ip addr show wlan0 ^|find "inet "') DO set ipfull=%%G
FOR /F "tokens=1 delims=/" %%G in ("%ipfull%") DO set ip=%%G
echo Connecting to device with IP %ip%...
"C:\platform-tools\adb.exe" connect %ip%

rem Optional: reconnect to a known static IP
set DEVICE_IP=192.0.0.4
set ADB_PORT=5555
"C:\platform-tools\adb.exe" kill-server
"C:\platform-tools\adb.exe" start-server
"C:\platform-tools\adb.exe" connect %DEVICE_IP%:%ADB_PORT%
