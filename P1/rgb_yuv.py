
# Importem llibreries necesàries
import subprocess
import numpy as np
import cv2
from scipy.fftpack import dct, idct

ffmpeg_direction = "C:/Users/oriol/PycharmProjects/Pràctica2_Codificació d'audio i video/ffmpeg/ffmpeg-2023-10-29-git-2532e832d2-full_build/bin/ffmpeg.exe"
##### Exercise 1 ######
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

#TEST Ex1
r, g, b = 255, 255, 0               #Define RGB values
y, u, v = rgb_to_yub(r, g, b)       #Convert RGB to YUV
nr, ng, nb = yuv_to_rgb(y, u ,v)    #Reconvert YUV to new RGB values

print("\nExercise1")
print('RGB = ', r, g, b, ' is converted to YUV = ', y, u, v)
print('RGB = ', y, u, v, ' is converted to YUV = ', nr, ng, nb)



###### Exercise 2 ######
def resize_image(input, output):

    ffmpeg_command = [ffmpeg_direction, "-i", input, "-vf", "scale=640:-1", "-q:v", "2", output]
    subprocess.run(ffmpeg_command)

# Test Ex2
input = "berlin_wall.jpg"
output = "berlin_wall_resized.jpg"
resize_image(input, output)
print("\nExercise 2 convert the quality of berlin_wall.jpg and save berlin_wall_resized.jpg")



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


imagen_path = "berlin_wall.jpg"  # Reemplaza "tu_imagen.bmp" con la ruta de tu imagen (formato BMP de 24 bits)
matriz_serpentina = serpentine(imagen_path)
print("\nExercise 3: read in serpentine mode and we obtain the image:\nThe print shows the first 20x20values of the image:\n",matriz_serpentina[:20,:20])


###### Exercise 4 ######
def bw_transform(input_image, output_image):
    #Max tax compression = 32k
    command = [ffmpeg_direction, "-i", input_image, "-vf", "format=gray", "-q:v", "32k", output_image]
    subprocess.run(command)

# Test Ex4
bw_output = "berlin_wall_black_and_white.jpg"
bw_image = bw_transform(input, bw_output)
print("\nExercise 4 save berlin_wall_black_and_white.jpg")


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

# Test Ex5
bits = "0001100001111"
code = run_length_encoding(bits)
print("\nExercise 5 code the bits ",bits, " to ", code)


###### Exercise 6 ######
class DCTConverter:
    def __init__(self):
        pass

    def encode(self, input_matrix): # Apply DCT

        return dct(dct(input_matrix, axis=0, norm='ortho'), axis=1, norm='ortho')

    def decode(self, encoded_matrix):   # Apply inverse DCT
        return idct(idct(encoded_matrix, axis=0, norm='ortho'), axis=1, norm='ortho')

# Test Ex6
input_matrix = np.random.random((8, 8))  #Matrix 8x8 example

dct_converter = DCTConverter()  #Creem variable tipo DCTConverter

encoded_matrix = dct_converter.encode(input_matrix) #Matrix DCT encode

decoded_matrix = dct_converter.decode(encoded_matrix) #Matrix inverse DCT decode

print("\nExercise 6:")
print("Input matrix:")
print(input_matrix)

print("\nCoded matrix:")
print(encoded_matrix)

print("\nDecoded matrix:")
print(decoded_matrix)