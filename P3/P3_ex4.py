import subprocess



# Funció per integrar subtítols
def integrate_subtitles(input, subtitles, output):
    ffmpeg_command = ['ffmpeg', '-i', input, '-vf', 'subtitles=' +subtitles, output]
    subprocess.run(ffmpeg_command)

