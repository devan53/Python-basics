import tkinter as tk
from pytube import YouTube


def downloadVid():
    global E1
    string = str(E1.get())
    yt = YouTube(string)
    videos = yt.streams
    for count, v in enumerate(videos):
        print(str(count + 1) + ": " + str(v))
    n = int(input("Please select your choice: "))
    vid = videos[n - 1]
    dest = input("enter your destination folder: ")
    vid.download(dest)
    print("Your video has been downloaded")


root = tk.Tk()

w = tk.Label(root, text="This is YouTube Downloader")
w.pack()

E1 = tk.Entry(root, bd=7)
E1.pack(side=tk.TOP)

button = tk.Button(root, bd=2, text="Download", fg="Red", command=downloadVid)
button.pack()

root.mainloop()
