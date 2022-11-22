#!/usr/bin/env bash

loop=True

while [ $loop ]; do
	read -p "[ prompt-video ] -> $ " param

	if [ -z $param ]; then
	    echo "[s] search + <search_str>";
		echo "[v] tabs of the videos";
		echo "[c] coby url domain";
		echo "[p] play video + <url>";
		echo "[clc] clear cache in browser"
		echo "[cls] clear terminal"
		echo "[q] quit";

	elif [ $param = 's' ]; then
		read -p 'param search : ' search
		python tools.py s "$search"

	elif [ $param = 'v' ]; then
		python tools.py v

	elif [ $param = 'c' ]; then
		python tools.py c

	elif [ $param =  'clc' ]; then
		python tools.py clc

	elif [ $param = 'p' ]; then
		read -p 'url video: ' video
		python play.py "$video"
	
	elif [ $param = 'cls' ]; then
		clear

	elif [ $param = 'q' ]; then
		exit 0
	fi
done
