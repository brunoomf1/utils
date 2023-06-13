from pytube import YouTube

print('Configurating')

link = ""
YouTube(link).streams.first().download()
yt = YouTube(link)
version = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()

print(f"Downloading {version}")

print(f"Starting Download ...")

version.download()

print(f"download completed")
