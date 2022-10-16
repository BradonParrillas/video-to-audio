from moviepy.editor import VideoFileClip
from os import listdir
from os import path

dir_path = r'./videos/'
output_dir_path = r'./audios/'
file_extension = '.mp4'
videos = []

def extraer_nombre(text):
    return text.split('.')[0]


def importar_videos():
    #recorremos todos los archivos dentro del directorio que contiene dir_path
    for file in listdir(dir_path):
        #guardamos en al lista de videos los archivos tipo file_extension
        if file.endswith(file_extension):
            videos.append(file)
            print("\t" + str(file))

def convertir_videos():
    for video in videos:
        video_path = dir_path + video
        audio_path = output_dir_path + extraer_nombre(video) + '.mp3'
        try:
            video_file_Clip = VideoFileClip(video_path)
        except Exception as e:
            print(e)
            print("No se pudo importar el video\nPosiblemente el video esta corrupto o no tiene imagen")
        else:
            print(video)
            audio = video_file_Clip.audio
            audio.write_audiofile(audio_path)
            print("\n")

if(path.isdir(dir_path)):
    print("Lista de videos:")
    importar_videos()
    print("\nConvirtiendo videos:\n")
    if(path.isdir(output_dir_path)):
        convertir_videos()
    else:
        print("No se encontro el directiorio de audio")
else:
    print("No se encontro el directorio de los videos")