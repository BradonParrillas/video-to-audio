from moviepy.editor import VideoFileClip

#! No funciona con videos que no tienen imagen
# video = VideoFileClip('./videos/1.mp4')
# video = VideoFileClip('./videos/example.mp4')

try:
    video = VideoFileClip('./videos/example.mp4')
except Exception as e:
    print(e)
    print("No se pudo importar el video\nPosiblemente el video esta corrupto o no tiene imagen")
else:
    audio = video.audio
    audio.write_audiofile('./audios/example.mp3')