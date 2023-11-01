# P1_Video_JPEG_MPEG

Aquest script conté els 6 exercicis proposats en la pràctica.
Cal compilar en python.
Cal posar la direcció d'on es troba la carpeta ffmpeg en la variable ffmpeg_direction. De normal,la comanda només s'ha de canviar per 'ffmpeg'.
S'utilitza la imatge berlin_wall.jpg

Es compilaran els 6 exercicis de cop. L'ordre que segueix el codi és el mateix per cada exercici, s'implementa la funció i es fa el seu test.

Exercici 1:
  Es creen dues funcions. Una converteix de rgb a yuv i l'altre de yuv a rgb.

Exercici 2:
  Rebaixem la calitat de la imatge berlin_wall.jpg amb comandes de ffmpeg. 
  Per tant, la imatge obtinguda, berlin_wall_resized.jpg,  té molts menys bytes.

Exercici 3:
  Es crea la funció serpentine(input). Aquesta, llegeix una imatge en forma de serpentina i retorna la imatge llegida en forma de matriu.

Exercici 4:
   A aprtir de comandos de ffmpeg es converteix la imatge barlin_wall.jpg a blanc i negre.
   
Exercici 5:
  Aquest exercici conté la funció run_length_encoding(bits). Implementa un codificador de bits.
  Li entra per referència una sequència de "n" bits i retorna una llista on a cada element indica la cantitat de uns i zeros que hi ha consecutivament.
  
Exercici 6:
  Aquest últim exercici té dues funcions. Una fa la transofrmada de Fourier i l'altre fa la inversa.
  Aleshores, generem una matriu 8x8 de valors aleatòris i podem veure com un cop feta la inversa de la DCT de la matriu obtenim la mateixa.
