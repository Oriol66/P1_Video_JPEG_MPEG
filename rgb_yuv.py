
# Importem llibreries necesàries
import subprocess
import numpy as np
from scipy.fftpack import dct, idct


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

print("\nExercise1\n")
print('RGB = ', r, g, b, ' is converted to YUV = ', y, u, v)
print('RGB = ', y, u, v, ' is converted to YUV = ', nr, ng, nb)



###### Exercise 2 ######
def resize_image(input, output):

    ffmpeg_command = ["ffmpeg", "-i", input, "-vf", "scale=640:-1", "-q:v", "2", output]
    subprocess.run(ffmpeg_command)

# Test Ex2
input = "/home/vboxuser/Downloads/berlin_wall.jpg"
output = "/home/vboxuser/Downloads/berlin_wall_resize.jpg"
#resize_image(input, output)



###### Exercise 3 ######
def serpentine(imagen_path):
    with open(imagen_path, 'rb') as imagen_file:
        imagen_file.read(
            54)  # Suposem que treballem amb 24 bits, per tant el encapcelament té 54
        # Tamany de la imatge
        ancho = int.from_bytes(imagen_file.read(4), byteorder='little')
        alto = int.from_bytes(imagen_file.read(4), byteorder='little')

        datos_serpentina = []


        izquierda_a_derecha = True
        fila_actual = 0

        for _ in range(ancho * alto):

            b = ord(imagen_file.read(1))
            g = ord(imagen_file.read(1))
            r = ord(imagen_file.read(1))

            datos_serpentina.append((r, g, b))

            if izquierda_a_derecha:
                if fila_actual % 2 == 0:
                    # Seguent columna
                    if fila_actual % 2 == 0:
                        if fila_actual % 2 == 0:
                            imagen_file.seek(3, 1)
                        else:
                            imagen_file.seek(6, 1)
                    else:
                        imagen_file.seek(3, 1)
                else:
                    # Retrocedeix la columna anterior
                    imagen_file.seek(-3, 1)
            else:
                if fila_actual % 2 == 0:
                    # Retrocedeix la fila
                    if fila_actual % 2 == 0:
                        if fila_actual % 2 == 0:
                            imagen_file.seek(-3, 1)
                        else:
                            imagen_file.seek(-6, 1)
                    else:
                        imagen_file.seek(-3, 1)
                else:
                    # Seguent columna
                    imagen_file.seek(3, 1)

            # Actualiza fila i direcció de lectura
            if izquierda_a_derecha:
                if fila_actual % 2 == 0:
                    fila_actual += 1
                else:
                    fila_actual -= 1
            else:
                if fila_actual % 2 == 0:
                    fila_actual -= 1
                else:
                    fila_actual += 1

            # Canvi de direcció si és necesssari
            if fila_actual >= alto or fila_actual < 0:
                izquierda_a_derecha = not izquierda_a_derecha
                if fila_actual >= alto:
                    fila_actual = alto - 1
                else:
                    fila_actual = 0

    return datos_serpentina

# Test Ex3
size = serpentine(input)



###### Exercise 4 ######
def bw_transform(input_image, output_image):
    # Tassa de bits muy baja para una máxima compressión = 32k
    command = ["ffmpeg", "-i", input_image, "-vf", "format=gray", "-q:v", "32k", output_image]
    subprocess.run(command)

# Test Ex4
bw_output = "/home/vboxuser/Downloads/berlin_wall_black_and_white.jpg"
bw_image = bw_transform(input, bw_output)


###### Exercise 5 ######
def run_length_encoding(bits ):
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
print(code)


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
print("Matriu de entrada:")
print(input_matrix)

print("\nMatriu codificada:")
print(encoded_matrix)

print("\nMatriu decodificada:")
print(decoded_matrix)
