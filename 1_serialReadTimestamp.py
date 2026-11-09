import serial
import time
from datetime import datetime

ser = serial.Serial('COM3', 115200)   # change to your port
time.sleep(2)

while True:
    line = ser.readline().decode().strip()
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp},{line}")
    
