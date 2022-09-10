import sys, os, subprocess, yt_dlp


url = input("Input URL Here: ")
song_there = os.path.isfile("output.mp3")
try:
	if song_there:
		os.remove("output.mp3")
except PermissionError:
	print("Permission Error")
	quit()
ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
for file in os.listdir("./"):
	if file.endswith(".mp3"):pass
		#os.rename(file, "output.mp3")
print("\nFinished")

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

# explorer would choke on forward slashes
path = os.path.normpath(r"C:\Users\raymo\OneDrive\Desktop\coding\Python Programs\! youtube download")

if os.path.isdir(path):
    subprocess.run([FILEBROWSER_PATH, path])
elif os.path.isfile(path):
    subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])