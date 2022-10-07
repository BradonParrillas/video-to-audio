from moviepy.editor import VideoFileClip

video = VideoFileClip('./video/example.mp4')

audio = video.audio

audio.write_audiofile('./audio/example.mp3')