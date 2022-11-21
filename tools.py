#!/usr/bin/env python3
import pyautogui as pg 
from sys import argv as a 
from time import sleep
import os

def get_position():
	px, py = pg.position()
	print(px, py)

def clear_cache():
	temp = 1

	# change browser
	pg.click(384, 14)
	sleep(temp)

	# change settings
	pg.click(1334, 98)
	sleep(temp)
	pg.click(1118, 635)
	sleep(temp)

	# change privacity
	pg.click(125, 386)
	sleep(temp)
	pg.move(300, 0)

	# scrolling in clear data
	sleep(temp)
	pg.scroll(-5)

	# clear data
	sleep(temp)
	pg.click(840, 622)
	sleep(temp)
	pg.click(920, 593)
	sleep(temp)
	pg.click(976, 456)

	# srolling in clear history
	sleep(temp)
	pg.scroll(-7)

	# clear history
	sleep(temp)
	pg.click(858, 375)
	sleep(temp)
	pg.click(925, 635)

	# closed tab
	sleep(temp)
	pg.hotkey('ctrl', 'w')

def search(search_u):
	pg.click(384, 14)
	pg.click(881, 175)
	pg.write(search_u, interval=0.10)
	pg.press('enter')

def tabs_video():
	pg.click(384, 14)
	pg.click(419, 512)

def copy_url():
	pg.click(384, 14)
	pg.click(735, 714)
	sleep(1.5)
	pg.click(876, 496)
	sleep(1.5)
	pg.click(907, 329)

def main():
	try:
		if a[1] == 's':
			search(a[2])

		if a[1] == 'v':
			tabs_video()
		
		if a[1] == 'c':
			copy_url()

		if a[1] == 'clc':
			clear_cache()

	except Exception as err:
		print(err)

if __name__ == '__main__':
	main()
