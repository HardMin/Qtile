#!/bin/sh

# feh --bg-scale ~/Image/Wallpapers/6.jpg

# systray battery icon
cbatticon -u 5 &
# # systray volume
volumeicon &
nm-applet &

nitrogen --restore

picom &

flameshot &
