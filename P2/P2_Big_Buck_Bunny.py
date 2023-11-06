# Importem llibreries necesàries
import subprocess
import ffmpeg
import numpy as np
import cv2
import rgb_yuv #Importem el script del lab1 per l'exercici 5

input_dir = "(Short) Big Buck Bunny.mp4" #Direcció on es troba el video de Big Buck Bunny

###### Exercise 1 ######
def convert_mp4_to_ffmpeg(input_dir, output_dir):
    ffmpeg_command = ["ffmpeg", "-i", input_dir, "-c:v", "mpeg2video", "-b:v", "10M", output_dir]
    subprocess.run(ffmpeg_command)

# Test Ex. 1
output_dir = "BBB.mpeg"
convert_mp4_to_ffmpeg(input_dir, output_dir)
print("Exercise 1 convert original Big Buck Bunny.mp4 to BBB.mpeg\n")


###### Exercise 2 ######
def modify_resolution(input_dir, output_dir, resolution):
    ffmpeg_command = ["ffmpeg", '-i', input_dir, '-vf',f'scale={resolution}', output_dir ]
    subprocess.run(ffmpeg_command)

# Test Ex. 2
output_dir = "BBB_less_resolution.mpeg"
resolution = '854:480'
modify_resolution(input_dir, output_dir, resolution)
print("Exercise 2 modify to less resolution the original BBB movie and save it as BBB_less_resolution.mpeg.\n")


###### Exercise 3 ######
def change_chroma(input_dir, output_dir):
    ffmpeg_command = ["ffmpeg", '-i', input_dir, '-vf', f"format=yuv420p",
                      "-c:v", "libx264", "-preset", "medium", output_dir]
    subprocess.run(ffmpeg_command)

# Test Ex. 3
output_dir = "BBB_changed_chroma.mpeg"
change_chroma(input_dir, output_dir)
print("Exercise 3 convert the chroma of BBB movie to yuv as BBB_changed_chroma.mpeg.\n")


###### Exercise 4 ######
def print_vido_data(input_dir, target_info):
    #probe = ffmpeg.probe(input_dir)
    ffmpeg_command = ["ffmpeg", '-i', input_dir]
    result = subprocess.run(ffmpeg_command, text=True, capture_output=True)
    output = result.stderr
    print(output)
    found_info = {}
    for info in target_info:
        for line in output.split("\n"):
            if info in line:
                value = line.split(',')[0].strip()
                found_info[info] = value
    return found_info

# Test Ex. 4
target_info = ["title", "composer", "genre", "Duration", "creation_time"]
info = print_vido_data(input_dir, target_info)

print("Exercise 4 found the info of the target:")
for info, value in info.items():
    print(value)



###### Exercise 5 ######
# Convertim el video a blanc i negre
output_dir = 'BBB_black_and_white.mpeg'
rgb_yuv.bw_transform(input_dir, output_dir)
print("\nExercise 5 uses the funcion of the last lab and convert the BBB movie to black and white as BBB_black_and_white.mpeg")


