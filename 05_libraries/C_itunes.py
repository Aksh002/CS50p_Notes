#                           APIs
#Its stands for "Application programming Interface"
#It refers to third party services that we can write code that talk to.Many APIs(not all) live on internet these days,we can write code that in effects pretends to be a browser,connects to that third party API on a server,and download some data thatwe can incorporate in our own program

#                           REQUESTS
#To do all this, python has this popular package       "REQUESTS"    it can be downloaded using pip
#Request library allows us to make web request suing python code essentially though u r the browser yourself.You can automate therefore the retrieval of URLs that start with HTTP and HTTPS
#Source - pypi.org/progect/requests

#Now to acces the api if itunes first visit "https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html#//apple_ref/doc/uid/TP40017632-CH5-SW1",the documentation site for itunes api
#Here it states that-
'''
To search for content from a field in your website and display the results in your website, you must create a search field that passes a fully-qualified URL content request to the iTunes Store, parse the JavaScript Object Notation (JSON) format returned from the search, and display the results in your website.

The fully-qualified URL must have the following format: https://itunes.apple.com/search?parameterkeyvalue. Where parameterkeyvalue can be one or more parameter key and value pairs indicating the details of your query.

To construct a parameter key and value pair, you must concatenate each parameter key with an equal sign (=) and a value string. For example: key1=value1. To create a string of parameter key and value pairs, you must concatenate each pair using an ampersand (&). For example: key1=value1&key2=value2&key3=value3.
'''

#They basically saying that if i wanna search for info abt songs in there database i should specify some parameters like entity=songs, if i want info on one song,we say limit=1,and term= weezer specifies the band i want to search for.After specifying such parameters and manually constructing my URL,search it on google
#here the url is - "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
#On running the search,a text file gets downloaded,which is full of key value pairs closed in "{[...]}", This type of file is a standard text format called JSON

#                           JSON
#JavaScript object notation ,which is related to JavaScript,but its usually used nowdays as a language agnostic format for exchanging data between computers.Language agnostic mean you dont need javascript to read n write that file , u can do it with python or any other language
#Its a complete text based format, which means that if i visit the url with my browser, what gets downloaded is just a bunch of text, but that text is formatted in a standard way with {},[],"",etc that ultimately contains all the info in apples database about weezer's songs
#Api is thus a mechanism whereby we can access data on someone elses server and somehow integrate it into my own program
#We actually hv to write sm pyhon code that perhaps pretends to be a browser ot grab the same data.

import requests            #to make those https requests
import sys

if len(sys.argv)!=2:
    sys.exit()
    #if the input is not desired,it will terminates the program prematurely,this makes sure that sys.argv has what i want.We cant use break here btw
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
#Its fxn in request package that will getresponse from the server
print(response.json())
#Enter "python C_itunes.py <artistname>" on terminal for output

#What python does here is it standardize this json response given by apple into a python dictionary
#It consists of 2 keys, one is named 'resultcount' which is 1,2nd key is 'results' which is equal to a wholeass list of data
#ITs quitse intimidating to comprehend the whole data, so we use another library to comprehend json file
#                           #JSON library
import json
import requests
import sys
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=4&term="+sys.argv[1])    #Index is also changed to 4, it gave me 4 seperate dict of 4 songs where ed sheeran was part of it(ft also)
print(json.dumps(response.json(),indent=2))    #Its documentation states that we can indent the result by 2 spaces
#It will do the pretty printing of the data
#Basically what we can comprehend easily now is that theres a main dict which has 2 keys,"resultcount"=<index>,"results" which contain a list full of dictionaries(quantity depends on the index) containing info about songs

#Now our purpose is to extract and  return the name of all the  songs of the artist user inputed  
import json
import requests
import sys
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
#So basically to sum up we r making https request from python to the server, just like we type URl on browser
o=response.json()
#Here we r grabbing the json object(which we need) from the variable where response of apple is stored and store it in "o"
for result in o["results"]:
    if result["artistName"]==sys.argv[1]:    #This done to eliminate all the songs that just feature him
        print(result["trackName"])  #Make sure to write correct names




# Printing all the solo songs and all the albums they r from

import json
import requests
import sys
'''artist=""
for i in range(len(sys.argv)-1):
    artist+=" "+sys.argv[i+1]'''


if len(sys.argv)==3:
    artist=sys.argv[1].title()+" "+sys.argv[2].title()
elif len(sys.argv)==2:
    artist=sys.argv[1]
else:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+artist)    #Index is also changed to 4, it gave me 4 seperate dict of 4 songs where ed sheeran was part of it(ft also)
#print(json.dumps(response.json(),indent=2)) 
o=response.json()
albums=[]
print("\n Tracks \n")
for result in o["results"]:
    if result["artistName"]==artist:    
        print(result["trackName"])  
        if result["collectionCensoredName"] not in albums:
            albums.append(result["collectionCensoredName"])
print("\n Albums: \n")
for i in albums:
    print(i)



