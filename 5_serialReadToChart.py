import serial
import time
from datetime import datetime
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 115200)  # Update port as needed
time.sleep(2)

x_vals = []
light_vals = []
sound_vals = []

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Light')
line2, = ax.plot([], [], label='Sound')
ax.set_xlabel('Sample Number')
ax.set_ylabel('Sensor Value')
ax.legend()

sample_count = 0

print("Live chart running. Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        print(line)

        # Safely parse the line: expects "Light:,19, Sound:,28"
        try:
            parts = line.split(',')
            light = int(parts[1].strip())
            sound = int(parts[3].strip())
        except Exception as e:
            print("Parse error, skipping line:", e)
            continue

        sample_count += 1
        x_vals.append(sample_count)
        light_vals.append(light)
        sound_vals.append(sound)

        # Update plot data
        line1.set_data(x_vals, light_vals)
        line2.set_data(x_vals, sound_vals)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)

except KeyboardInterrupt:
    print("Stopped.")

plt.ioff()
plt.show()
