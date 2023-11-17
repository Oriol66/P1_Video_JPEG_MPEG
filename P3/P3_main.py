
import subprocess
import P3_ex4 as  ex4
import P3_ex6 as ex6

#Direcció input de BBB
input_direction = '(Short) Big Buck Bunny.mp4'

###### EXERCICI 1 ######
def cut_save_video(input_dir, seconds, output_dir):
    #Comanda per guardar un nou video amb dla duració "seconds"
    ffmpeg_command = ['ffmpeg', '-i', input_dir, '-t', str(seconds), '-c:v', 'copy', '-c:a', 'copy', output_dir]
    subprocess.run(ffmpeg_command)

# Tallem 9 segons del video
cuted_video = 'BBB_cut.mp4'
sec = 9
cut_save_video(input_direction, sec, cuted_video)


#Creem la classe VideoProcesor per l'exercici 2 i 3
class VideoProcessor:
    def __init__(self,input_macroblocks_dir, output_macroblocks_dir, input_container, output_container):
        self.input_macroblocks_dir = input_macroblocks_dir
        self. output_macroblocks_dir = output_macroblocks_dir
        self.input_container = input_container
        self.output_container = output_container

    #Funció exercici 1
    def add_macroblocks_and_motion_vectors(self):
        # Comanda ffmpeg per obtenir informació dels macroblocks
        subprocess.run(["ffmpeg", "-flags2", "+export_mvs", "-i", self.input_macroblocks_dir, '-vf', "codecview=mv=pf+bf+bb", output_macroblocks_dir])

    #funció exercici 2
    def create_50seconds_container(self):

        # Comanda per guardar un nou video amb 50 segons de duració
        ffmpeg_command = ['ffmpeg', '-i', self.input_container, '-t', str(50), '-c:v', 'copy', '-c:a', 'copy', "BBB_50seconds.mp4"]
        subprocess.run(ffmpeg_command)

        # Guardar el audio en mp3 format estereo
        ffmpeg_command = ['ffmpeg', '-i', 'BBB_50seconds.mp4', '-f', 'mp3', '-ab', '192000', '-vn', 'BBB_stereo.mp3']
        subprocess.run(ffmpeg_command)

        # Guardar el àudio en mono
        ffmpeg_command = ['ffmpeg', '-i', 'BBB_50seconds.mp4', '-ac', '1', 'BBB_mono.mp3']
        subprocess.run(ffmpeg_command)

        # Guardar el audio en AAC
        ffmpeg_command = ['ffmpeg', '-i', 'BBB_50seconds.mp4', '-codec:a', 'aac', 'BBB_AAC.aac']
        subprocess.run(ffmpeg_command)

        # Agrupem tots els arxius en un mp4
        ffmpeg_command = ['ffmpeg', '-i', 'BBB_50seconds.mp4', '-i', 'BBB_stereo.mp3', '-i', 'BBB_mono.mp3', '-i',
                          'BBB_AAC.aac',
                          '-filter_complex', '[1:0][2:0][3:0]amix=inputs=3:duration=first', '-c:v', 'copy', '-c:a',
                          'aac', '-strict',
                          'experimental', self.output_container]
        subprocess.run(ffmpeg_command)

    def container_counter(self):

        ffmpeg_command = ['ffprobe', '-show_entries', 'stream=channels', '-of', 'compact=p=0:nk=1','-v', '0', self.output_container]
        resultado = subprocess.check_output(ffmpeg_command, stderr=subprocess.STDOUT, text=True)

        return int(resultado.strip())


# Instància de VideoProcessor
input_macroblocks_dir = cuted_video                 #Obtenim els macroblocks del video amb 9 segons.
output_macroblocks_dir = 'BBB_macroblocks.mp4'
input_container_dir = input_direction               #Fem el container del video sencer
output_container_dir = 'BBB_container.mp4'
processor = VideoProcessor(input_macroblocks_dir, output_macroblocks_dir, input_container_dir, output_container_dir )

###### Exercici 1 ########
#generem video amb macroblocks vectors BBB_macroblocks.mpeg
processor.add_macroblocks_and_motion_vectors()

###### Exercici 2 ######
# Generem els arxius d'àudio stereo, mono, en format AAC i ho unim tot en un .mp4 com a BBB_container.mp4
processor.create_50seconds_container()


###### Exercici 3 ######
# Executem la funció que retorne l número de tracks d'àudio
chanels_counter = processor.container_counter()
print('El container té: ', chanels_counter, 'tracks')


###### Exercici 4,5 ######

# integrem els subtítols de Trainspoting a BBB :)
input_video = 'Choose Life Trainspotting.mp4'
subtitles = 'Choose Life Trainspotting.en.srt'
output_BBB_with_subtitles = 'BBB_trainspoting_subtitles.mp4'
ex4.integrate_subtitles(input_direction, subtitles, output_BBB_with_subtitles)

# Juntem el video de BBB amb els subtítols i el àudio del trailer de Trainspoting
trainspoting_audio = 'Trainspoting_mono.mp3'
BBB_trainspoting_audio = 'BBB_with_trainspoting_audio.mp4'

ffmpeg_command = ['ffmpeg', '-i',output_BBB_with_subtitles, '-i', trainspoting_audio,
                  '-filter_complex', '[1:0]amix=inputs=1:duration=first', '-c:v', 'copy', '-c:a',
                  'aac', '-strict', 'experimental', BBB_trainspoting_audio]
subprocess.run(ffmpeg_command)


###### Exercici 6 ######
#Obtenim el video de BBB amb els histogrames de YUV
output_histogram_dir = 'BBB_histogram.mp4'
ex6.extract_yuv_histogram(cuted_video, output_histogram_dir)
