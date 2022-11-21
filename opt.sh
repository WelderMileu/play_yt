#!/usr/bin/env bash

if [ -z $1 ]; then
	echo "[s] search + <search_str>";
	echo "[v] tabs of the videos";
	echo "[c] coby url domain";
	echo "[p] play video + <url>";
	echo "[clc] clear cache in browser"

elif [ $1 = 's' ]; then
	python tools.py s "$2"

elif [ $1 = 'v' ]; then
	python tools.py v

elif [ $1 = 'c' ]; then
	python tools.py c

elif [ $1 =  'clc' ]; then
	python tools.py clc

elif [ $1 = 'p' ]; then
	python play.py "$2"
fi
