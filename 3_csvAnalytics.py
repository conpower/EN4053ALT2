import csv
import statistics
import matplotlib.pyplot as plt

light_values = []
sound_values = []

with open("log.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 5:
            continue

        light = int(row[2])
        sound = int(row[4].strip())
        light_values.append(light)
        sound_values.append(sound)

print("Light mean:", round(statistics.mean(light_values), 2))
print("Light median:", round(statistics.median(light_values), 2))
print("Light mode:", round(statistics.mode(light_values), 2))

print("Sound mean:", round(statistics.mean(sound_values), 2))
print("Sound median:", round(statistics.median(sound_values), 2))
print("Sound mode:", round(statistics.mode(sound_values), 2))