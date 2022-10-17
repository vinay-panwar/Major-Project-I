# random function to select random Integer 
import random

# list to store question and there answer
data = []
# open the file
with open('D:\\Projects\\Major Project I\\Dataset\\train.txt.','r') as f:
   line = f.readlines()
#  insert the data into list
   for i in line :
       data.append(i.split(';'))

# find the question at random index
def getQuestion() :         
    ques = random.randint(0,len(data)-1)
    # print(data[ques][0])
    return [data[ques][0],ques]
    
# define the mood using that question's answer
def getMood(ques,ans) :
    # x = 'yes'

    if ans in  ['yes','YES','Yes',1] :
        mood = data[ques][1]
             
    else :
        mood = 'Calm'
    # print(mood)
    f.close()
    return mood
