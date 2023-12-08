
import subprocess



# Classe processor
class Processor:
    def __init__(self, input):
        self.input = input

    def quality_converter(self, quality, output):
        # guarda el video amb la qualitat seleccionada
        if quality == '240p':
            ffmpeg_command = ['ffmpeg', '-i', self.input, '-vf', "scale=426:240", output]
            subprocess.run(ffmpeg_command)

        if quality == '360p':
            ffmpeg_command = ['ffmpeg', '-i', self.input, '-vf', "scale=640:360", output]
            subprocess.run(ffmpeg_command)

        if quality == '480p':
            ffmpeg_command = ['ffmpeg', '-i', self.input, '-vf', "scale=854:480", output]
            subprocess.run(ffmpeg_command)

        if quality == '720p':
            ffmpeg_command = ['ffmpeg', '-i', self.input, '-vf', "scale=1280:720", output]
            subprocess.run(ffmpeg_command)

        if quality == '1080p':
            ffmpeg_command = ['ffmpeg', '-i', self.input, '-vf', "scale=1920:1080", output]
            subprocess.run(ffmpeg_command)

    def convert_to_VP8(self, output):
        ffmpeg_command = ['ffmpeg', '-i', self.input, '-c:v', 'libvpx', '-b:v', '1M', '-c:a', 'libvorbis', output]
        subprocess.run(ffmpeg_command)

    def convert_to_VP9(self, output):
        # Codifiquem amb VP9. libvpx-vp9 selecciona el codec de VP9
        ffmpeg_command = ['ffmpeg', '-i', self.input, '-c:v', 'libvpx-vp9', '-b:v', '1M', '-c:a', 'libvorbis', output]
        subprocess.run(ffmpeg_command)

    def convert_to_h265(self, output):
        # Codifiquem amb h264. libx265 selecciona el codec de h265
        #-crf 28 controla la calitat de compressió. Valors més alts per millor compressió i menor calitat.
        #-b:a 128k és la tassa de vídeo
        ffmpeg_command = ['ffmpeg', '-i', self.input, '-c:v', 'libx265', '-crf', '28', '-c:a', 'aac', '-b:a', '128k', output]
        subprocess.run(ffmpeg_command)

    def convert_to_AV1(self, output):
        # Codifiquem amb AV1. libaom-av1 selecciona el codec de AV1
        ffmpeg_command = ['ffmpeg', '-i', self.input, '-c:v', 'libaom-av1', '-crf', '30', output]
        subprocess.run(ffmpeg_command)

    def combine_videos(self, input1, input2, output):
        ffmpeg_command = ['ffmpeg', '-i', input1, '-i', input2, '-filter_complex', '[1:v][0:v]scale2ref[wm][base];[base][wm]hstack=2', output]
        subprocess.run(ffmpeg_command)

input_direction = '(Short) Big Buck Bunny.mp4'

# Exercici 1:
input_proc = Processor(input_direction)

#Obtenim BBB en diferents resolucions
input_proc.quality_converter('240p', 'BBB_240p.mp4')
input_proc.quality_converter('360p', 'BBB_360p.mp4')
input_proc.quality_converter('480p', 'BBB_480p.mp4')
input_proc.quality_converter('720p', 'BBB_720p.mp4')

#Agafem el video de BBB amb millor calitat i el codifiquem amb 4 diferents codecs
BBB_processor = Processor('BBB_720p.mp4')

BBB_processor.convert_to_VP8('BBB_VP8.webm')  #El format de VP8 és .web
BBB_processor.convert_to_VP9('BBB_VP9.webm')
BBB_processor.convert_to_h265('BBB_h265.mp4') #Format h.265 és .mp4
BBB_processor.convert_to_AV1('BBB_AV1.mkv')    #Format AV1 és .mkv


# Exercici 2:
BBB_processor.combine_videos('BBB_VP8.webm', 'BBB_VP9.webm', 'BBB_VP8_vs_BP9.mp4')
BBB_processor.combine_videos('BBB_VP8.webm', 'BBB_h265.mp4', 'BBB_VP8_vs_h265.mkv')
