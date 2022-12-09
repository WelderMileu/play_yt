#!/usr/bin/bash
figlet "Setup Youtube"
echo ""
sleep 1

# main domain
path_domain="https://raw.githubusercontent.com/weldermileu/play_yt/main/"

# dependencies
list_f=(
    "simple.py"
    "tools.py"
    "terminal_video.sh"
)

echo "[+] Downloading files"
sleep 1
echo ""

# download dependencies
for x in "${list_f[@]}"; do
    if [ $x = ${list_f[0]} ]; then
	sleep .5
	wget -q --show-progress $path_domain$x -O play.py
    else
	sleep .5
	wget -q --show-progress $path_domain$x
    fi
done

# permission of execution
chmod +x ${list_f[2]}

# download packages using pip3
echo ""
echo "[+] Downloading packages"
echo ""
sleep 1
pip3 install pytube wget pyautogui

# message congragulations
echo ""
echo "Congragulations your Finalized on setup of the video!"
