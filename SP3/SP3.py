import subprocess
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import tkinter
from tkinter import ttk


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


# Funcions per la interfície
def elegir_visualizar_video():
    global cap
    if cap is not None:
        lblVideo.image = ""
        cap.release()
        cap = None
    video_path = filedialog.askopenfilename(filetypes=[
        ("all video format", ".mp4"),
        ("all video format", ".avi")])
    if len(video_path) > 0:
        lblInfoVideoPath.configure(text=video_path)
        lblInfoVideoPath.grid(column=5, row=12, padx=0, pady=1, columnspan=1)
        cap = cv2.VideoCapture(video_path)

    else:
        lblInfoVideoPath.configure(text="Encara no s'ha seleccionat cap vídeo.")

def GUIresolution(comboResol, GUIProcessor):
    if comboResol == "426x240": GUIProcessor.quality_converter('240p', "resolution.mp4")
    if comboResol == "640x360": GUIProcessor.quality_converter('360p', "resolution.mp4")
    if comboResol == "720x480": GUIProcessor.quality_converter('480p', "resolution.mp4")
    if comboResol == "1280x720": GUIProcessor.quality_converter('720p', "resolution.mp4")
    if comboResol == "1920x1080": GUIProcessor.quality_converter('180', "resolution.mp4")
    return "resolution.mp4"

def GUIcode(comboCode, GUIProcessor):
    # Codifiquem en el format desitjat
    coded_direction = ""
    if comboCode == "VP8":
        coded_direction = "coded.webm"
        GUIProcessor.convert_to_VP8(coded_direction)

    elif comboCode == "VP9":
        coded_direction = "coded.webm"
        GUIProcessor.convert_to_VP9(coded_direction)

    elif comboCode == "h265":
        coded_direction = "coded.mp4"
        GUIProcessor.convert_to_h265(coded_direction)

    elif comboCode == "VP8":
        coded_direction = "coded.mkv"
        GUIProcessor.convert_to_AV1(coded_direction)

    return coded_direction


def visualizar():

    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblInfoVideoPath.configure(text="Aún no se ha seleccionado un video")
            lblVideo.image = ""
            cap.release()

# Main interfície
cap = None
root = Tk()
#seleccionar video
root.geometry("800x400")
btnVisualizar = Button(root, text="Triar Video", command=elegir_visualizar_video)
btnVisualizar.grid(column=5, row=0, padx=0, pady=1, columnspan=1)

# Seleccionar resolucions
resol = ["1920x1080", "1280x720", "720x480", "640x360", "426x240"]
lblResol = Label(root, text="Seleccionar resolució:")
lblResol.grid(column=0, row=2)

# Crear desplegable (Combobox) amb opcions de resolucions
comboResol = ttk.Combobox(root, values=resol, state="readonly")
comboResol.current(0)  # Establir opció determinada
comboResol.grid(column=5, row=2, padx=5, pady=5)


# Seleccionar codificador
code = ["VP8", "VP9", "H265", "AV1"]  # Ejemplo de resoluciones
lblCode = Label(root, text="Seleccionar resolució:")
lblCode.grid(column=0, row=4)

# Crear desplegable (Combobox) amb opcions de codificadors
comboCode = ttk.Combobox(root, values=code, state="readonly")
comboCode.current(0)
comboCode.grid(column=1, row=4, padx=5, pady=5)

btnVisualizar = Button(root, text="PLAY", command = visualizar())
btnVisualizar.grid(column=0, row=8, padx=0, pady=1, columnspan=1)


lblInfoVideoPath = Label(root, text=" ")
lblInfoVideoPath.grid(column=1, row=1)
lblVideo = lblInfoVideoPath
lblVideo.grid(column=0, row=2, columnspan=2)

GUIProcessor = Processor(lblInfoVideoPath)

#Convertim video d'entrada a la resolució desitjada

resolution_path = GUIresolution(comboResol, GUIProcessor)
GUIProcessor = Processor(resolution_path) #Nou processador amb resolució desitjada

final_path = GUIcode(comboCode, GUIProcessor) #Agafem el path del video codificat

root.mainloop()



#### MAIN  EX 1, 2####
input_direction = '(Short) Big Buck Bunny.mp4'

# Exercici 1:
input_proc = Processor(input_direction)
#Obtenim BBB en diferents resolucions
#input_proc.quality_converter('240p', 'BBB_240p.mp4')
#input_proc.quality_converter('360p', 'BBB_360p.mp4')
#input_proc.quality_converter('480p', 'BBB_480p.mp4')
#input_proc.quality_converter('720p', 'BBB_720p.mp4')

#Agafem el video de BBB amb millor calitat i el codifiquem amb 4 diferents codecs
BBB_processor = Processor('BBB_720p.mp4')

#BBB_processor.convert_to_VP8('BBB_VP8.webm')  #El format de VP8 és .web
#BBB_processor.convert_to_VP9('BBB_VP9.webm')
#BBB_processor.convert_to_h265('BBB_h265.mp4') #Format h.265 és .mp4
#BBB_processor.convert_to_AV1('BBB_AV1.mkv')    #Format AV1 és .mkv


# Exercici 2:
#BBB_processor.combine_videos('BBB_VP8.webm', 'BBB_VP9.webm', 'BBB_VP8_vs_BP9.mp4')
#BBB_processor.combine_videos('BBB_VP8.webm', 'BBB_h265.mp4', 'BBB_AV1.mkv')


