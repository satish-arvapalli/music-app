import os
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import pygame

root = Tk()
root.minsize(300, 300)

listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root, textvariable=v, width=35)

index = 0
songname = ''


def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updateSongName()


def previousSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updateSongName()


def stopSong(event):
    pygame.mixer.music.stop()
    v.set("")


def updateSongName():
    global index
    global songname
    v.set(realnames[index])
    return songname


def choosedirectory():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith('.mp3'):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    # pygame.mixer.music.play()
    # updateSongName()


choosedirectory()


label = Label(root, text='Play Music')
label.pack()

listbox = Listbox(root)
listbox.pack()

realnames.reverse()
for items in realnames:
    listbox.insert(0, items)

nextbutton = Button(root, text='Next')
nextbutton.pack()

previousbutton = Button(root, text='Previous')
previousbutton.pack()

stopbutton = Button(root, text='Stop')
stopbutton.pack()

nextbutton.bind('<Button-1>', nextSong)
previousbutton.bind('<Button-1>', previousSong)
stopbutton.bind('<Button-1>', stopSong)

songlabel.pack()

root.mainloop()
