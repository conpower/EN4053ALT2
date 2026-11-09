import serial
import time
from datetime import datetime

# Open serial port
ser = serial.Serial('COM3', 115200)
time.sleep(2)

data_log = []

print("Logging... Press Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(timestamp, line)
        data_log.append(f"{timestamp},{line}")  # combine manually

except KeyboardInterrupt:
    print("Stopped logging.")

# Save to CSV manually
with open("log.csv", "w") as f:
    f.write("Timestamp,Line\n")  # header
    for entry in data_log:
        f.write(entry + "\n")     # no quotes

print("Saved to log.csv")
