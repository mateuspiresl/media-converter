import ffmpy
import os, sys, subprocess, shlex, re
from subprocess import call


def set_video_codec(codec, options):
    if len(options) > 0 and options[-1] != ' ': options = options + ' '
    options = options + '-c:v ' + str(codec)

def set_resolution(width, height, options):
    if len(options) > 0 and options[-1] != ' ': options = options + ' '
    options = options + '-s:v ' + str(width) + 'x' + str(height)

def probe_file(filename):
    cmnd = ['ffprobe', '-show_format', '-pretty', '-loglevel', 'quiet', filename]
    out, err =  p.communicate()
    return json.dumps(out)
    raise err


file_in = '../assets/SampleVideo_360x240_1mb.mp4'
file_out = '../files/result_SampleVideo_360x240_1mb.mp4'

data = probe_file(file_in)


options = ''
set_video_codec('h264', options)
set_resolution('720', '480', options)

inputs = {}
inputs[file_in] = None

outputs = {}
outputs[file_out] = ''
set_video_codec('h264', outputs[file_out])
set_resolution('720', '480', outputs[file_out])

ff = ffmpy.FFmpeg(
    inputs={ '../assets/SampleVideo_360x240_1mb.mp4': None },
    outputs={ '../files/result_SampleVideo_360x240_1mb.mp4': options })

ff.run()