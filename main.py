#!/usr/bin/env python3
import tkinter as tk
import json
import time
import sys

CONFIG_PATH = "config.json"
DANGERS = [
	"#66ff33",
	"#ffff00",
	"#ff9933",
	"#ff3300"
]

def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def change_danger_col(canvas, gcol, color):
	for col in range(35):
		for row in range(18):
			if col == gcol:
				canvas.itemconfig((col * 18) + row + 1, fill=color)

def main():
	print("led")
	root = tk.Tk()
	canvas = tk.Canvas(root, width=1920, height=1080, borderwidth=0, highlightthickness=0, bg="black")
	canvas.grid()
	def _create_circle(self, x, y, r, **kwargs):
		return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
	tk.Canvas.create_circle = _create_circle
	for col in range(35):
		for row in range(18):
			canvas.create_circle(100 + (col * 50), 100 + (row * 50), 20, fill=DANGERS[0], outline="#DDD", width=4)
	with open(CONFIG_PATH, "r") as fd:
		config = json.load(fd)
	frames = []
	for frame in config:
		for reset in range(35):
			change_danger_col(canvas, reset, DANGERS[0])
		for led in frame["leds"]:
			change_danger_col(canvas, led["col"], DANGERS[led["danger"]])
		root.update()
		time.sleep(float(frame["time"]))
	sys.exit()

if __name__ == "__main__":
    main()
