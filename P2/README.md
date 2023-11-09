# P2_Python_Video

By: Oriol Estabanell Santiago 229320


Aquest script conté els 5 exercicis proposats en la pràctica.

Cal compilar en python.

S'utilitza el video de Big Buck Bunny. Canviar la variable "input_dir" per la ubicació d'aquest arxiu.

Es compilaran els 5 exercicis de cop. L'ordre que segueix el codi és el mateix per cada exercici, s'implementa la funció i es fa el seu test.


#Exercici 1:
	Es crea una funció convert_mp4_to_ffmpeg(input_dir,output_dir) que converteix el format del video de BBB i ho guarda com a BBB.mpeg.

#Exercici 2:
	Es crea la funció modify_resolution(input_dir, output_dir, resolution). utilitza una comanda de ffmpeg per rebaixar la resolució del video. Per tant, el video resultant com a BBB_less_resolution.mpeg ocupa molt menys espai que el original.

#Exercici 3:
	Es defineix la funció change_chroma(input_dir, output_dir). Reconverteix el format del video de RGB a YUVe. Es guarda com a BBB_changed_chroma.mpeg. Com podem observar. El video és aparentment igual que l'original.

#Exercici 4:
  	Trobem la funció print_vido_data(input_dir, target_info). Aquesta, agafa la direcció del vido i retorna la informació que posem en la variable "target_info". Posteriorment, s'imprimeix per pantalla la informació demanada. 
   
#Exercici 5:
	Aquest exercici utilitza el document rgv_yuv.py de l'anterior pràctica. Importem aquest script a dalt de tot del programa. Aleshores, aquest exercici agafa el video de Big Buck Bunny i utilitza  la funció bw_transform(input_dir, output_dir) de el script rgb_yuv. El resultat és el video en blanc i negre anomenat com BBB_black_and_white.mpeg.
	

