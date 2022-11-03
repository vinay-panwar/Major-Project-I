from tkinter import * 
import pyglet as py


# whole ui background
bac = 'white'

root = Tk()
root.geometry('350x650')
root.configure(background=bac)
root.title('music recommender UI')
root.iconbitmap(r'D:\Projects\Major Project I\Code\ICON\apple-music.ico')
root.attributes('-alpha',0.9)
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", bac)

# Name of the UI 
Label(root,text="Music Recommender system",bg=bac,fg='Dark red',font=('San Sarif',15,'bold')).pack(padx=10,pady=10,anchor=CENTER)

# next window 
label_image = Label(root,bg=bac)
label_image.pack()

# media player initialized 
player = py.media.Player()

# for loading the song
def load(song) :
    src = py.media.load(song)
    # songName = song.split(sep="//")
    # songName= songName[len(songName)-1].split(".")
    # Label(label_image,text=songName[0],bg=bac,fg='red',font=('verdana',15,'bold')).place(x=0,y=0)
    player.queue(src)


# default code 
def default() :
    backButton = Button(label_image,image=backwardBackground,command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 50,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 50,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)

#   song
def song(num) :
    song = ["D://Projects//Major Project I//Dataset//Song//kesariya.mp3","D://Projects//Major Project I//Dataset//Song//Mast Magan.mp3"]
    songName = song[num].split(sep="//")
    songName= songName[len(songName)-1].split(".")
    Label(label_image,text=songName[0],bg=bac,fg='black',font=('San Sarif',15)).grid(row=3,column=3, pady=50) 
    return song[num]


# play the loaded song
def play() :
    load(song(1))
    playButton.forget()
    player.play()
    # pauseButton.pack(pady=30,anchor=E)
    # pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 50,fg= 'white')
    pauseButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)

    
    backButton = Button(label_image,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)
    
    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)

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
    
    # Name of the UI 
    # Label(root,text="Music Recommender system",bg=bac,fg='black',font=('verdana',15,'bold')).pack(padx=10,pady=40,anchor=CENTER) 
    # scope
    global pauseButton, playButton,forwardButton, playBackground,pauseBackground,forwardBackground,backwardBackground,backButton
    global buttonPadX, buttonPadY,buttonRaw 
    
    # button padding x and y axis 
    buttonPadX = 5
    buttonPadY = 10
    
    # button raw and colomn decide 
    buttonRaw =6
    # buttonC
    
    load(song(1))
    # button background 
    playBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\play.png')
    pauseBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\pause.png')
    forwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\forward.png')
    backwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\backward.png')
    # centerImage =PhotoImage(file="D:\Projects\Major Project I\Code\ICON\musicBack.png")
    
    # Center image pic
    # centerPic=Label(label_image,image=centerImage,bg=bac,borderwidth=0,highlightthickness=0)
    # centerPic.grid(row=5,column=3,pady=5)
    
    backButton = Button(label_image,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 50,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 50,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)
    # default()

    # extraButton = Button(label_image,image=buttonBackground,borderwidth=0)
    # extraButton.pack(padx=10,pady=30, anchor=CENTER)
    return 0 

# main()
# root.mainloop()