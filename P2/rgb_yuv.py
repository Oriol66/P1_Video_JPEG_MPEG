
# Importem llibreries necesàries
import subprocess
import ffmpeg
import numpy as np
import cv2
from scipy.fftpack import dct, idct

###### Aquest script només conté les funcions del laboratori 1!!!


###### Exercise 1 ######
def rgb_to_yub(r,g,b):
    y = round(0.299*r + 0.587*g +0.114*b)
    u= round(0.492*(b-y))
    v= round(0.877*(r-y))
    return y,u,v

def yuv_to_rgb(y,u,v):
    r = round(y + 1.14*v)
    g = round(y - 0.39465*u -0.5806*v)
    b = round(y + 2.03211*u)
    return r,g,b


###### Exercise 2 ######
def resize_image(input, output):

    ffmpeg_command = ["ffmpeg", "-i", input, "-vf", "scale=640:-1", "-q:v", "2", output]
    subprocess.run(ffmpeg_command)



###### Exercise 3 ######
def serpentine(input_image):
    # Leer la imagen utilizando OpenCV
    image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

    # Obtener las dimensiones de la imagen
    height, width = image.shape

    # Inicializar la matriz de salida
    output_matrix = np.zeros((height, width), dtype=np.uint8)

    # Inicializar las coordenadas de inicio
    x, y = 0, 0

    # Inicializar la dirección (1 para derecha, -1 para izquierda)
    direction = 1

    for value in range(256):
        if direction == 1:
            for _ in range(width):
                output_matrix[y, x] = image[y, x]
                x += 1
            x -= 1
            y += 1
            direction = -1
        else:
            for _ in range(width):
                output_matrix[y, x] = image[y, x]
                x -= 1
            x += 1
            y += 1
            direction = 1

    return output_matrix


###### Exercise 4 ######
def bw_transform(input_image, output_image):
    #Max tax compression = 32k
    command = ["ffmpeg", "-i", input_image, "-vf", "format=gray", "-q:v", "32k", output_image]
    subprocess.run(command)


###### Exercise 5 ######
def run_length_encoding(bits):
    encoded = []
    count = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            count += 1
        else:
            encoded.append((count, bits[i-1]))
            count = 1
    encoded.append((count, bits[-1]))
    return encoded


###### Exercise 6 ######
class DCTConverter:
    def __init__(self):
        pass

    def encode(self, input_matrix): # Apply DCT

        return dct(dct(input_matrix, axis=0, norm='ortho'), axis=1, norm='ortho')

    def decode(self, encoded_matrix):   # Apply inverse DCT
        return idct(idct(encoded_matrix, axis=0, norm='ortho'), axis=1, norm='ortho')
