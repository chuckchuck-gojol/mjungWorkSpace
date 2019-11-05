from pytube import YouTube
import subprocess
import os

print('before download')
# yt = YouTube('https://www.youtube.com/watch?v=2yfhyfQObwE')
# yt = YouTube('https://youtu.be/6T2jEKesKXY')
yt = YouTube('https://www.youtube.com/watch?v=T9PREvZvDGo ')

print('after download')

vids = yt.streams.all()
for i in range(len(vids)):
    print(i, '. ', vids[i])
    
vnum= int(input("Enter vid num: "))

parent_dir = r"C:\YTDownloads"
vids[vnum].download(parent_dir)

new_filename = input("new_filename.wav")

default_filename = vids[vnum].default_filename
print(default_filename)
print(new_filename)

subprocess.call([
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('done')

# yt.streams
# .filter(progressive=True, file_extension='mp4')
# .order_by('resolution')
# .desc()
# .first()
# .download()
