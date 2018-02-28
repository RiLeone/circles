#!/usr/bin/env bash
ffmpeg -i plts/frames/%05d.png -vcodec libx264 animation.mp4
