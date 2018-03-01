#!/usr/bin/env bash
ffmpeg -r 10 -i plts/frames/%05d.png -vcodec libx264 animation.mp4
rm -f plts/frames/*.png
