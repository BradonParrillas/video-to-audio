from moviepy.editor import VideoFileClip
from os import path

#! No funciona con videos que no tienen imagen
# video = VideoFileClip('./videos/1.mp4')
# video = VideoFileClip('./videos/example.mp4')

try:
    video = VideoFileClip('./videos/example.mp4')
except Exception as e:
    print(e)
else:
    audio = video.audio
    directorio_valido = path.isdir('./audios/')
    if(directorio_valido):
        audio.write_audiofile('./audios/example.mp3')