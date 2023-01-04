import eyed3
import os
from colorama import Fore, Back, Style

dir_path = os.path.dirname(os.path.realpath(__file__))
division = ' - '
long_div = len(division)
print(long_div)

def imprimir(text):
    print(Fore.BLACK + Back.WHITE + text + Style.RESET_ALL)

for file in os.listdir(dir_path):
    if file[-3:] == 'mp3':
        div_posicion = file.find(' - ')
        artista = file[0:div_posicion]
        titulo = file[div_posicion + long_div:-4]

        imprimir(file)
        imprimir(str(div_posicion))
        imprimir(titulo)
        imprimir(artista)
        print()

        try:
            song = eyed3.load(file)
            song.tag.title = titulo
            song.tag.artist = artista
            song.tag.save()
        except Exception as e:
            print(Fore.WHITE + Back.RED + file + " - " + str(e) + Style.RESET_ALL + "\n")