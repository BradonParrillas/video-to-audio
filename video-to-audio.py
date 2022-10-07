from moviepy.editor import VideoFileClip
from os import listdir

dir_path = r'./videos/'
output_dir_path = r'./audio/'
file_extension = '.mp4'
videos = []

def importar_videos():
    #recorremos todos los archivos dentro del directorio que contiene dir_path
    for file in listdir(dir_path):
        #guardamos en al lista de videos los archivos tipo file_extension
        if file.endswith(file_extension):
            videos.append(file)

def convertir_videos():
    print(dir_path + videos[0])
    # for video in videos:
    #     video_file_Clip = VideoFileClip(dir_path + video)
    #     audio = video_file_Clip.audio
    #     audio.write_audiofile(output_dir_path + video + '.mp3')

importar_videos()
print(videos)
convertir_videos()