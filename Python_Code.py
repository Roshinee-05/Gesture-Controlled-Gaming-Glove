import serial
import pyautogui
import time
port = ‘COM10’
baudrate = 9600
try:
ser = serial.Serial(port, baudrate, timeout=1)
time.sleep(2)
print(“Mouse control active...”)
while True:
line = ser.readline().decode().strip()
if line.startswith(“MOVE:”):
try:
coords = line[5:].split(“,”)
x = float(coords[0])
y = float(coords[1])
# Adjust sensitivity
move_x = int((x – 180) / 10) # center at 180
move_y = int((y – 180) / 10)
if abs(move_x) > 1 or abs(move_y) > 1:
pyautogui.moveRel(move_x, move_y)
except:
continue
elif line == “CLICK”:
pyautogui.click()
print(“Click!”)
except Exception as e:
print(“Error:”, e)
