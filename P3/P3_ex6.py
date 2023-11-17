import subprocess

def extract_yuv_histogram(input_video, output_histogram):
    ffmpeg_command = ['ffmpeg', '-i', input_video, '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay', '-c:v', 'libx264', '-c:a', 'aac', output_histogram]
    subprocess.run(ffmpeg_command)

