from dataclasses import InitVar
from inspect import Attribute
from msilib.schema import ListBox, RadioButton
from multiprocessing import Value
from os import link
from pydoc import text
from time import sleep
from tkinter import *
import pyglet as py
# import NewOpenFile as file
import fileOpen as file
import NewMain as mod1

# whole ui background
bac = 'Light gray'

root = Tk()
root.geometry('350x650')
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
        # Label(HomeFrame,text=ans.get(),fg='black',bg=bac,font=('San Sarif',15)).pack(pady=5,anchor=SW)
        song = mod1.__init__(mood)
        # print(song)
        # songslist
        songlist = song[0]
        # number of songs to show 
        numberOfSongs = 2*song[1]
        # print(songlist)
        # print(numberOfSongs)
        # frame to store the list of songs in UI.
        listboxFrame = Frame(root,width=300,height=600,bg=bac)
        listboxFrame.pack(padx=10,pady=10,fill=None,expand=False)
        
        # creating the list box which will be stored in the listboxFrame.
        listbox = Listbox(listboxFrame,height=40,width=35,bg=bac,font=('Helvetica',12,'italic'),fg='black')
        listbox.pack(pady=10,fill='both',expand=True)
        
        # scrollbar in listbox
        vsb = Scrollbar(listboxFrame, orient="vertical", command=listbox.yview)
        listbox.configure(yscrollcommand=vsb)
        vsb.pack(side="right", fill="y")
        
        # adding a logo of music at the time of starting of insert.
        # D:\Projects\Major Project I\Code\ICON\music.png
        """addMusicBackground = PhotoImage(file='D:\Projects\Major Project I\Code\ICON\music.png')
        imagenew = Label(HomeFrame, image=addMusicBackground,background=bac,fg='white')
        imagenew.pack(pady=20)"""
        # inserting value in the listbox on UI.
        # to limit the song to a given number of time.
        x=0
        for i in songlist : 
            if x <= numberOfSongs :
                # listbox.insert(x,i+' : '+songlist[i])
                listbox.insert(x,("    "+i+" : "+songlist[i]))
                x+=1
                listbox.insert(x,'')
            else :
                break
            x+=1
            # Label(HomeFrame,text=(i+' : '+songlist[i]),fg='black',bg=bac,font=('San Sarif',15)).pack(pady=5,expand=FALSE)
            # print(i,' : ',songlist[i])
        # listbox.forget()
        return 0
    # find a question 
    ques = file.getQuestion()
    # Name of the UI 
    Label(HomeFrame,text="Music Recommender system",bg=bac,fg='black',font=('San Sarif',16,'bold')).pack(padx=10,pady=25,anchor=CENTER)
    Label(HomeFrame,text=ques[0],bg=bac,fg='black',font=('Helvetica',14)).pack(padx=10,pady=10,expand=FALSE)
    # variable 
    ans = IntVar()
    # Radiobutton to select yes or no for an answer
    rb1 =Radiobutton(HomeFrame,text='Yes',bg=bac,fg='black',font=('San Sarif',13,'bold'),variable=ans,value=1)
    rb1.pack(padx=10,pady=5,anchor=SW,expand=FALSE)
    rb2= Radiobutton(HomeFrame,text='No',bg=bac,fg='black',font=('San Sarif',13,'bold'),variable=ans,value=2)
    rb2.pack(padx=10,pady=5,anchor=SW,expand=FALSE)
    
    # submit button to send the details to another function.
    submit = Button(HomeFrame,text="Submit",font=('San Sarif',13),fg='white',bg='dark blue',command=getEntry)
    submit.pack(pady=30)
# Home window call 
Home()
# next window 
nextWindow = Label(root,bg=bac)
nextWindow.pack()

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
    backButton = Button(nextWindow,image=backwardBackground,command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)


    playButton = Button(nextWindow,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(nextWindow,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(nextWindow,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)

#   song
def song(num) :
    song = ["D://Projects//Major Project I//Dataset//Song//kesariya.mp3","D://Projects//Major Project I//Dataset//Song//Mast Magan.mp3"]
    songName = song[num].split(sep="//")
    songName= songName[len(songName)-1].split(".")
    Label(nextWindow,text=songName[0],bg=bac,fg='black',font=('San Sarif',15)).grid(row=3,column=3, pady=20) 
    return song[num]


# play the loaded song
def play() :
    load(song(1))
    playButton.forget()
    player.play()
    # pauseButton.pack(pady=30,anchor=E)
    pauseButton= Button(nextWindow,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    pauseButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)

    
    backButton = Button(nextWindow,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)
    
    forwardButton = Button(nextWindow,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)

def pause() :
    player.pause()
    pauseButton.forget()
    secondWindow()



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

# UI to play music and song which are stored on the source device.
def secondWindow() :
    
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
    
    backButton = Button(nextWindow,image=backwardBackground,command= revert,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # pause_button.pack(padx= 10,pady= 30, anchor=CENTER)
    backButton.grid(row=buttonRaw,column=0,padx=buttonPadX,pady=buttonPadY)


    playButton = Button(nextWindow,image=playBackground, command= play,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # playButton.pack(pady=30,anchor=E)
    playButton.grid(row=buttonRaw,column=3,padx=buttonPadX,pady=buttonPadY)
    
    pauseButton= Button(nextWindow,image=pauseBackground, command= pause,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')

    forwardButton = Button(nextWindow,image=forwardBackground,command= next_,bg=bac,borderwidth= 0.1,width= 30,fg= 'white')
    # forwardButton.pack(padx= 10,pady= 30, anchor=W)
    forwardButton.grid(row=buttonRaw,column=6,padx=buttonPadX,pady=buttonPadY)
    # default()

    # extraButton = Button(label_image,image=buttonBackground,borderwidth=0)
    # extraButton.pack(padx=10,pady=30, anchor=CENTER)
        

# secondWindow()
root.mainloop()