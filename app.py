from PyDictionary import PyDictionary
from wordfreq import word_frequency as wf
import time as t

def findMeaning(y):
    dictionary=PyDictionary()
    x=dictionary.meaning(y)
    solnStr=""
    solnStr="Word: "+y+"\n"
    if x is not None:
        for i, j in x.items():
            solnStr+="\n ("+str(i)+") \n"
            for k,l in enumerate(j):
                if l[0]!='(':
                    solnStr+=str(k+1)+ " "+ l+".\n"
                else:
                    solnStr+=str(k+1)+ " "+ l[1:]+".\n"
                
    else:
        return None
    return solnStr

#main
import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password=""
)

done=dict()
startTime=t.time()
while True:
    for submission in reddit.subreddit("india").new(limit=300):
        string=submission.title
        if string not in done:
            done[string]=True
            arr=[i for i in string.split(' ')]
            arr=sorted(arr, key=len, reverse=True)
            print(arr)
            comment=""
            for i in arr:
                print(i)
                usage=wf(i,"en")
                if (usage<0.00003 and usage!=0) or len(i)>7:
                    x=findMeaning(i)
                    if x!=None:
                        comment+=x+"\n"
            if comment!="":
                print("reply sent")
                submission.reply("[A Real user's application that autogenerates synonyms of some words] \n\n"+comment)
            print("[A Real user's application that autogenerates synonyms of some words] \n\n" +comment)

    if t.time-startTime>86400:
        done=dict()
        startTime=t.time()

print(findMeaning("Inadvertently"))