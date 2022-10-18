from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import random as r
# import fileOpen as file
# import NewOpenFile as file

# Maximum number of song to show
maxSongs = 10
# list out all the songs could be played
def show_songs(albums) :
    song_list = {}
    num_song = 0
    # number of songs to show 
    if albums['total'] > maxSongs :
        num_song = maxSongs
    else :
        num_song =albums['total']
    try :
        for i in range(albums['total']) :
            y = albums['items'][i]
            name =y['track']['name'] 
            url = y['track']['external_urls']['spotify']
            song_list[name] = url
            # print(name, " : ",url)
    
    except :
        print("do nothing ")
    # print(song_list)
    """x=0
    for i in song_list :
        if  x < num_song :
            # print('{i} : {y}'(i,song_list[i]))
            print(i,' : ',song_list[i])
        else :
            break
        x+=1
        """
    # songlist to return 
    listCopy = song_list.copy()
    # clear the dictionary after using
    song_list.clear() 
    return [listCopy,num_song]
    
# show all the songs in album 
def show_album(albums) :
    song_list = {}
    num_song = 0
    # number of songs to show, which you got to do decide
    if albums['total'] > maxSongs :
        num_song = maxSongs
    else :
        num_song =albums['total']
        
    try :
        for i in range(albums['total']) :
            y = albums['items'][i]
            name =y['name'] 
            url = y['external_urls']['spotify']
            song_list[name] = url
            # print(name, " : ",url)
            # print(song_list)
    
    except :
        print("do nothing ")
    # print(song_list)
    """x=0
    for i in song_list :
        if  x < num_song :
            # print('{i} : {y}'(i,song_list[i]))
            print(i,' : ',song_list[i])
        else :
            break
        x+=1"""
    # songlist to return 
    listCopy = song_list.copy()
    # clear the dictionary after using
    song_list.clear()
    return [listCopy,num_song]
    
# decide the spotify uri to the song
def song(y) :
    # type of song's dictionary
    songs = {
    'sadness\n' : ['spotify:playlist:07cKOg8bqOupkf5eRFJIY2','spotify:playlist:1gd8rPLzo3bjk1yyQce0h7','spotify:album:3iMjk15PNBjloo3WLFbQdW'],
    'Happy\n' : ['spotify:playlist:4nd7oGDNgfM0rv28CQw9WQ','spotify:album:6tWmAwsXBU2R3gub5p67Hd'],
    'Energetic\n' :['spotify:playlist:7sqjkYA5C4L7EPFtrUoyjj','spotify:playlist:16JGZG9gKRs6jtbz2kb80b'],
    'Calm' :['spotify:playlist:018H0FzGVR7dguRrR78Jy1','spotify:album:0AKsODOjmUCzXLneG0Hg3h','spotify:playlist:0dsl5hbFdVT7scb7Vakkwa','spotify:playlist:6jKGZerpd82B3YGVz89Rpe'],
    'joy\n' :['spotify:album:0qHkdHtgoChQHN97d6KB3x','spotify:playlist:4ouorxAgtEl4eWuf380oib'],
    'Natural' : ['spotify:playlist:5kIN7R5Oftp2CyBfAC8DIG'],
    'love\n' : ['spotify:playlist:1zEJJsE9BkWxfT4eX6JvN8','spotify:album:5Wm1nhxZqx7i0Hp6ZBqe9T','spotify:album:6IXfWhC7omotM4lt0ROmEr']
    }
    # y = input("which genre to played")
    num = r.randint(0,len(songs[y])-1)
    print(y)
    return songs[y][num]

# establish connection b/w api and program flow
def establish_connection() :
    try :
        # scope of the spotify 
        scope = "user-read-recently-played"
        # setting up with the authentication
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
        # results = sp.artist_albums(arijit, album_type='album')
        # results = sp.album_tracks(arijit)
        return sp
    except :
        print('Failed Connection')
        return 0

# new find song function 
# find a song asked a type of 
def find_song(sp,song_type) :
#     connection established
    # sp = establish_connection()
#     get the song
    get_song_link = song(song_type)
    get_song_link_list = get_song_link.split(sep=':')
    #print(get_song_link_list)
    # songlist = None
    if get_song_link_list[1] == 'playlist' : 
        results = sp.playlist(get_song_link)
        print("Play list")
        albums = results['tracks']
        songlist =show_songs(albums)
        # print(songlist)
        return songlist
    else :
        results = sp.album(get_song_link)
        # do it incase of album
        print('album') 
        albums = results['tracks']
        songlist=show_album(albums)
        # print(songlist)
        return songlist
    

def __init__(get) :    
    sp = establish_connection()
    randomList = ['sadness\n','Happy\n','Calm','Energetic\n','joy\n','Natural']
    print(get) 
    if get not in randomList :
        get = 'Happy\n'
        print(get)
    # index =r.randint(0,len(randomList)-1)
    print("\n\nwhich genre to played : %s\n"%(get))
    # ask_song = 'Energetic'
    # find_song(sp,randomList[index])
    songs = find_song(sp,get)
    # ask_song = 'Happy'
    # find_song(sp,ask_song)
    """x=0
    for i in songlist :
        if  x < numberOfSongs :
            # print('{i} : {y}'(i,song_list[i]))
            print(i,' : ',songlist[i])
        else :
            break
        x+=1"""
    return songs

# __init__('sadness')