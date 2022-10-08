#import any value
from types import new_class
from matplotlib import use
from pandas import * 
userData = read_csv(r'D:\\Projects\\Major Project I\\Dataset\\data_moods.csv')
new_data =userData.drop(['release_date','popularity','acousticness',"instrumentalness",'liveness','valence','loudness','speechiness','tempo','key','time_signature'],axis='columns')

def update_rate(song_name,rating) :
    if song_name == [x for x in new_data['name']] :
        print(True)

def music(chr,rate) :
    # print(chr)
    #drop non required columns 

    # print(new_data.isnull().count(True))
    for i,j,k in zip(new_data['mood'],new_data['name'],new_data['ratings']) :
        # print(i)
        # k = int(k)
        if str(i) == chr :
            if k >= 5 :
                # print(new_data['name'])
                print(j ," rating " ,int(k))
                # print(j, " ",new_data)
    else :
        print()    

song_genre = "Sad"
song =music(song_genre,5)
# print(song)
#get the feed back of the song 
# rate = int(input("Give an feedback for the suggested song : "))
rate = 3
update_rate(song,rate)
song = music(song_genre,rate)
# print(song)