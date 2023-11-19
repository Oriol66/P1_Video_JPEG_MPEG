# P3_Python_Video

By: Oriol Estabanell Santiago 229320


Aquest script conté els 6 exercicis proposats en la pràctica i un afegit :)

Cal compilar en python el arxiu P3_main.py

S'utilitza el video de Big Buck Bunny. Canviar la variable "input_direction" per la ubicació d'aquest arxiu.

Es compilaran els 6 exercicis de cop. En funció de la durada del video el programa tardarà significativament més o menys.

Primer trobem els imports, després les funcions i després la classe VideoPocessor. Aquesta classe la utilitzarem en l'exercici 1, 2 i 3. 


#Exercici 1, 2 i 3:

Primer de tot es defineix una funció per tallar n segons d'un video, l'utilitzem amb el video de BBB i el tallem 9 segons.
Aleshores, definim la classe VideoProcessor que ens serveix per definir 3 funcions. Una per cada exercici.
    
    Ex 1: Es crea un video on apareixen els macroblocks del video d'entrada. 
        Output: BBB_macroblocks.mp4
    
    Ex 2: Aquest exercici directament talla 50segons d'un video, exporta el àudio en mono, stereo i AAC, i finalment ho ajunta tot en un .mp4
        Output 50segons: BBB_50seconds.mp4
        Output mono: BBB_mono.mp3
        Output stereo: BBB_stereo.mp3
        Otuput AAC: BBB_AAC.aac
        Output container: BBB_container.mp4

    Ex3: Aquest exercici defineix la funció container_counter() i ens retorna el número de tracks que té el vídeo de la clase VideoProcessor


#Exercici 4:
    Creem el script P3_ex4.py. Conté una funció que ens permet incrustar subtítols en un vídeo.

#Exercici 5:
    Importem el script P3_ex4.py a dalt del codi i l'utilizem per posar els subtítols del trailer de Trainspotting al vídeo de BBB:)
    Com a més a més, afegim el àudio de Trainspoting "Trainspoting_mono.mp3" al vídeo de BBB i obtenim una veritable obra d'art.
    Output BBB amb subtítols: BBB_trainspoting_subtitles.mp4
    Output final: BBB_with_trainspoting_audio.mp4


#Exercici 6:
	Creem l'arxiu P3_ex6.py on definim una funció per crear un vídeo de BBB amb el seu histograma de YUV en temps real situat a dalt a l'esquerra.
    Output: BBB_histogram.mp4


