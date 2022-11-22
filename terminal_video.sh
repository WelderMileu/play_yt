#!/usr/bin/env bash

loop=True

while [ $loop ]; do
	echo -e "\e[0;36m┌──(\e[0mprompt-video\e[0;36m)\e[0m - [$(date +'%H:%M:%S')]"
	echo -en "\e[0;36m└─ $ \e[0m"
	read -p '' param

	if [ -z $param  ]; then
		echo -n "";

	elif [ $param = "-h" ]; then
	    echo "";
		echo "[-h]  - menu help"
	    echo "[s]   - consult search";
		echo "[v]   - tabs of the videos";
		echo "[c]   - coby url domain";
		echo "[p]   - play video";
		echo "[clc] - clear cache in browser"
		echo "[cls] - clear terminal"
		echo "[q]   - quit";
		echo "";

	elif [ $param = 's' ]; then
		read -p '[search] - ' search
		python tools.py s "$search"

	elif [ $param = 'v' ]; then
		python tools.py v

	elif [ $param = 'c' ]; then
		python tools.py c

	elif [ $param =  'clc' ]; then
		python tools.py clc

	elif [ $param = 'p' ]; then
		read -p '[domain] - ' video
		python play.py "$video"
	
	elif [ $param = 'cls' ]; then
		clear

	elif [ $param = 'q' ]; then
		exit 0
	fi
done
