from importlib.resources import path
from inspect import Attribute
from operator import ne
from os import sep
from signal import default_int_handler
from sqlite3 import PARSE_DECLTYPES
from struct import pack
from tkinter import *
from turtle import bgcolor, color, forward, shape 
import pyglet as py


# whole ui background
bac = 'light gray'

root = Tk()
root.geometry('300x400')
root.configure(background=bac)
root.title('music recommender UI')
root.iconbitmap(r'D:\Projects\Major Project I\Code\ICON\apple-music.ico')
root.attributes('-alpha',0.8)
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", bac)

# next window 
label_image = Label(root,bg=bac)
label_image.pack()

# media player initialized 
player = py.media.Player()

# for loading the song
def load(song) :
    src = py.media.load(song)
    songName = song.split(sep="//")
    songName= songName[len(songName)-1].split(".")
    Label(label_image,text=songName[0],bg=bac,fg='red',font=('verdana',15,'bold')).place(x=0,y=0)
    player.queue(src)


# default code 
def default() :
    backButton = Button(label_image,image=backwardBackground,command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=1,column=0,padx=10,pady=180)


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=1,column=3,padx=10,pady=180)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=1,column=6,padx=10,pady=180)

#   song
def song(num) :
    song = ["D://Projects//Major Project I//Dataset//Song//kesariya.mp3","D://Projects//Major Project I//Dataset//Song//Mast Magan.mp3"] 
    return song[num]


# play the loaded song
def play() :
    load(song(0))
    playButton.forget()
    player.play()
    # pauseButton.pack(pady=30,anchor=E)
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    pauseButton.grid(row=1,column=3,padx=10,pady=180)
    
    backButton = Button(label_image,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=1,column=0,padx=10,pady=180)
    
    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=1,column=6,padx=10,pady=180)

def pause() :
    player.pause()
    pauseButton.forget()
    main()



def next_() :
    player.pause()
    pauseButton.forget()
    
    default()
    # player.next_source(song[1])
    load(song(1))

def revert() :
    player.pause()
    pauseButton.forget()
    default()
    load(song(0))


def main() :
    # scope
    global pauseButton, playButton,forwardButton, playBackground,pauseBackground,forwardBackground,backwardBackground,backButton

    # button background 
    playBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\play.png')
    pauseBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\pause.png')
    forwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\forward.png')
    backwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\backward.png')
    
    backButton = Button(label_image,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=1,column=0,padx=10,pady=180)


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=1,column=3,padx=10,pady=180)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=1,column=6,padx=10,pady=180)
    # default()

    # extraButton = Button(label_image,image=buttonBackground,borderwidth=0)
    # extraButton.pack(padx=10,pady=30, anchor=CENTER)
        

main()
root.mainloop()