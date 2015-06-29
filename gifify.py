from PIL import Image
import sys

sys.path.insert(0, './vendor')
import os
from images2gif import writeGif

class FrameSettings:
    # set up for SA avatars
    width = 150
    height = 150
    # todo: support more than horizontal pane one day
    start_x = 0
    y = 27
    stop_x = 80

class SnapPosition:
    x = 0
    y = 0
    w = 150
    h = 150

def dump_frame(src, frame_settings, path):
    x1 = int(frame_settings.x)
    y1 = int(frame_settings.y)
    x2 = int(frame_settings.x + frame_settings.w)
    y2 = int(frame_settings.y + frame_settings.h)
    cropped = src.crop((x1, y1, x2, y2))
    cropped.save(path)

# compute the positions for a pan
def get_pan_locations(frame_settings, number_of_frames = 10):
    x_distance = abs(frame_settings.stop_x - frame_settings.start_x)
    start_x = min(frame_settings.stop_x, frame_settings.start_x)
    snap_positions = []

    for step in range(number_of_frames):
        frac = x_distance * (step / float(number_of_frames))
        pos = SnapPosition()
        pos.y = frame_settings.y
        pos.x = start_x + frac
        pos.w = frame_settings.width
        pos.h = frame_settings.height

        snap_positions.append(pos)

    return snap_positions

fs = FrameSettings()
fs.start_x = 18
fs.y = 10
fs.stop_x = 256
snap_positions = get_pan_locations(fs)

src = Image.open("resized_cat.png")

i = 0
filenames = []

for snap in snap_positions:
    file_name = "pic" + str(i) + ".png"
    dump_frame(src, snap, file_name)
    filenames.append(file_name)
    i = i + 1

writeGif("output.gif", [Image.open(fn) for fn in filenames], duration=0.1)
