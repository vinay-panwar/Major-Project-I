from dataclasses import InitVar
from inspect import Attribute
from msilib.schema import RadioButton
from multiprocessing import Value
from pydoc import text
from time import sleep
from tkinter import *
import pyglet as py
# import NewOpenFile as file
import fileOpen as file
import NewMain as mod1

# whole ui background
bac = 'light gray'

root = Tk()
root.geometry('350x600')
# root.resizable(0,0)
# root.maxsize(350,600)
root.configure(background=bac)
root.title('music recommender UI')
root.iconbitmap(r'D:\Projects\Major Project I\Code\ICON\apple-music.ico')
root.attributes('-alpha',0.8)

# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", bac)
HomeFrame = Frame(root,width=350,height=600,bg=bac)
HomeFrame.pack(fill=BOTH,expand=False)

def Home() :
    # after click on sumit button get the entered value 
    def getEntry() :
        print(ans.get())
        mood = file.getMood(ques[1],ans.get())
        print(mood)
        rb1.forget()
        rb2.forget()
        submit.forget()
        Label(HomeFrame,text=ans.get(),fg='black',bg=bac,font=('San Sarif',15)).pack(pady=5,anchor=SW)
        song = mod1.__init__(mood)
        # print(song)
        # songslist
        songlist = song[0]
        # number of songs to show 
        numberOfSongs = song[1]
        # print(songlist)
        # print(numberOfSongs)
        x=0
        for i in songlist :
            if  x < numberOfSongs :
                Label(HomeFrame,text=(i+' : '+songlist[i]),fg='black',bg=bac,font=('San Sarif',15)).pack(pady=5,expand=FALSE)
                # print(i,' : ',songlist[i])
            else :
                break
            x+=1
    
    # find a question 
    ques = file.getQuestion()
    # Name of the UI 
    Label(HomeFrame,text="Music Recommender system",bg=bac,fg='black',font=('San Sarif',18,'bold','italic')).pack(padx=10,pady=25,anchor=CENTER)
    Label(HomeFrame,text=ques[0],bg=bac,fg='black',font=('San Sarif',15,'bold')).pack(padx=10,pady=40,anchor=CENTER,expand=FALSE)
    # variable 
    ans = IntVar()
    # Radiobutton
    rb1 =Radiobutton(HomeFrame,text='Yes',bg=bac,fg='black',font=('San Sarif',10),variable=ans,value=1)
    rb1.pack(padx=10,pady=5,anchor=SW,expand=FALSE)
    rb2= Radiobutton(HomeFrame,text='No',bg=bac,fg='black',font=('San Sarif',10),variable=ans,value=2)
    rb2.pack(padx=10,pady=5,anchor=SW,expand=FALSE)
    submit = Button(HomeFrame,text="Submit",font=('San Sarif',15),fg='white',bg='dark blue',command=getEntry)
    submit.pack(pady=30)

Home()
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


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)

#   song
def song(num) :
    song = ["D://Projects//Major Project I//Dataset//Song//kesariya.mp3","D://Projects//Major Project I//Dataset//Song//Mast Magan.mp3"]
    songName = song[num].split(sep="//")
    songName= songName[len(songName)-1].split(".")
    Label(label_image,text=songName[0],bg=bac,fg='black',font=('San Sarif',15)).grid(row=3,column=3, pady=20) 
    return song[num]


# play the loaded song
def play() :
    load(song(1))
    playButton.forget()
    player.play()
    # pauseButton.pack(pady=30,anchor=E)
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
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
    LabelImage()



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


def LabelImage() :
    
    """# Name of the UI 
    Label(root,text="Music Recommender system",bg=bac,fg='black',font=('verdana',15,'bold')).pack(padx=10,pady=40,anchor=CENTER)    """
    # scope
    global pauseButton, playButton,forwardButton, playBackground,pauseBackground,forwardBackground,backwardBackground,backButton
    global buttonPadX, buttonPadY,buttonRaw 
    
    # button padding x and y axis 
    buttonPadX = 5
    buttonPadY = 10
    
    # button raw and colomn decide 
    buttonRaw =5
    # buttonC
    
    load(song(1))
    # button background 
    playBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\play.png')
    pauseBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\pause.png')
    forwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\forward.png')
    backwardBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\\backward.png')
    
    backButton = Button(label_image,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)


    playButton = Button(label_image,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(label_image,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(label_image,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)
    # default()

    # extraButton = Button(label_image,image=buttonBackground,borderwidth=0)
    # extraButton.pack(padx=10,pady=30, anchor=CENTER)
        

# LabelImage()
root.mainloop()