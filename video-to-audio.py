from moviepy.editor import VideoFileClip
from os import listdir

dir_path = r'./videos/'
output_dir_path = r'./audios/'
file_extension = '.mp4'
videos = []

def importar_videos():
    #recorremos todos los archivos dentro del directorio que contiene dir_path
    for file in listdir(dir_path):
        #guardamos en al lista de videos los archivos tipo file_extension
        if file.endswith(file_extension):
            videos.append(file)

def convertir_videos():
    for video in videos:
        video_path = dir_path + video
        print("Direccion del video: " + video_path)
        audio_path = output_dir_path + video + '.mp3'
        print("Direccion del audio: "+ audio_path)
        try:
            video_file_Clip = VideoFileClip(video_path)
            print("\tSe importo el video: ", video)
        except Exception as e:
            print(e)
            print("No se pudo importar el video\nPosiblemente el video esta corrupto o no tiene imagen")
        else:
            audio = video_file_Clip.audio
            audio.write_audiofile(audio_path)

importar_videos()
print("Lista de videos:")
print(videos)
convertir_videos()