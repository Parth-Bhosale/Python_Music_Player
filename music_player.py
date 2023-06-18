import os
from tkinter import *
from tkinter import filedialog

from pygame import mixer

root = Tk()
root.title("Music Player")
root.geometry("400x500+280+10")
root.configure(background="#333333")

mixer.init()
frameCnt = 30
frames = [PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\main.gif", format="gif -index %i" %i) for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)


label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def PlayMusic():
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


lower_frame = Frame(root, bg="#FFFFFF", width=400, height=180)
lower_frame.place(x=0, y=300)

image_icon = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\logo.png")
root.iconphoto(False, image_icon)

Menu = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\menu.png")
Label(root, image=Menu).place(x=0, y=480, width=400, height=100)
Button(root, text="Browse Music", width=48, height=1, font=("calibri", 11, "bold"), fg="black", bg="#FFFFFF", command=AddMusic).place(x=0, y=470)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=365, width=400, height=100)

ButtonPlay = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\play.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=40, width=40, command=PlayMusic).place(x=255, y=317)

ButtonStop = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=40, width=40, command=mixer.music.stop).place(x=180, y=317)

ButtonPause = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=40, width=40, command=mixer.music.pause).place(x=325, y=317)

Volume1 = PhotoImage(file="D:\\Documents\\DSE\\CodeClause Internship\\Music_Player\\vol.png")
panel = Label(root, image=Volume1).place(x=106, y=317)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()
scale.place(x=0, y=317)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("calibri", 10), bg="#333333", fg="white", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)


root.mainloop()