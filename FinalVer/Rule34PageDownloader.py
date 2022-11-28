import requests 
import re
from art import *
from bs4 import BeautifulSoup 
from os.path import basename
import urllib.request
#from PIL import Image
#import shutil
#import urllib
#import socket
#socket.getaddrinfo('127.0.0.1', 8080)

def getdata(url): 
    r = requests.get(url) 
    return r.text 
def reversestr(x):
  return x[::-1]
def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))
#input link

#declare variables
lista = []
drugalista = []
lista3 = []
listaLinkovaSlika = []
listalink = []
listacao = []
elementiVideoStr = []
listaimenaWEBMGIF = []
listaLinkovaWEBMGIF = []
listaimena = []
listaimenaVidea = []
listaimenaWEBM = []
#constants
f = "https://rule34.xxx/"
#counters
trecaListaCounter = 0
listlinkCounter = 0
webmcounter = 0
webmgif = 0



tprint("dp/r34 v1.1", font="small")
print("Created by GilePY#0567 <-- Discord for more scripts/script commissons")
print("If u input a false link the program will auto close")
print("It only works with Rule34 links(Search pages, Favorites, Tags, Artists, etc)")
print(r"Example of a link https://rule34.xxx/index.php?page=post&s=list&tags=sakura_haruno+")
print(r"Consider supporting me on Patreon: patreon.com/gilescripts")
link = input("Rule34 Page Link:")
print("Starting...")
print("Gathering source (Be patient)")
#gather html data for the first time
htmldata = getdata(link) 
soup = BeautifulSoup(htmldata, 'html.parser')  #bs4 bs

for item in soup.find_all('a'):
    drugalista.append(item['href']) #get all href files from the <a tag
#put the in a list and filter them so its only href links that lead to photos
trecalista = list(filter(lambda x: 'index.php?page=post&s=view&id=' in x, drugalista))
#go through them
while trecaListaCounter < len(trecalista):
    listalink.append(f + str(trecalista[trecaListaCounter])) #append the index.php etc to the f rule34 string
    trecaListaCounter+=1
#gather html data from the list of href links and append them to another list
while listlinkCounter < len(listalink):
    htmldata2 = getdata(listalink[listlinkCounter])
    soup2 = BeautifulSoup(htmldata2,'html.parser')
    for item2 in soup2.find_all('img'):
        lista3.append(item2['src'])
    for item3 in soup2.find_all(id='gelcomVideoPlayer'):     
        listacao.append(item3)
    listlinkCounter+=1    
print("Successfully extracted the data from Rule34!")
#print(listacao)
#print(lista3)

for x in listacao:
    elementiVideoStr.append(str(x))

y = 0
z = 0

#filter so its only the original image,video no ads

for item2 in lista3:
    #print(item2)
    if('.gif?' in item2):
        listaLinkovaWEBMGIF.append(item2)
        lista3.remove(item2)

#listaLinkovaWEBM = list(filter(lambda x :'https://wimg.rule34.xxx//images/' in x, lista3))


listaLinkovaVidea = list(filter(lambda x : '.mp4?' in x, elementiVideoStr))
listaLinkovaSlika = list(filter(lambda x: '.jpg?' in x, lista3)) 
listaLinkovaSlikaJPEG = list(filter(lambda x: '.jpeg?' in x, lista3))
listaLinkovaSlikaPNG = list(filter(lambda x: '.png?' in x, lista3))

t = 0
g = 0
if(len(listaLinkovaSlika) != 0):
    while g < len(listaLinkovaSlika):
        listaimena.append(listaLinkovaSlika[g].split(".jpg?", 1)[1])
        g+=1


counter = 0
listaLinkovaVideaFinale = []


while counter < len(listaLinkovaVidea):
    listaLinkovaVideaFinale.append(re.search('src="(.+?)" type', listaLinkovaVidea[counter]).group(1))
    counter+=1

#gg = 0
#if(len(listaLinkovaWEBM) != 0):
    #while gg < len(listaLinkovaWEBM):
        #if(".jpg?" in listaLinkovaWEBM[gg]):  
            #listaimenaWEBM.append(listaLinkovaWEBM[gg].split(".jpg?", 1)[1])
        #elif(".jpeg?" in listaLinkovaWEBM[gg]):  
            #listaimenaWEBM.append(listaLinkovaWEBM[gg].split(".jpeg?", 1)[1])
        #elif(".png?" in listaLinkovaWEBM[gg]): 
            #listaimenaWEBM.append(listaLinkovaWEBM[gg].split(".png?", 1)[1])
        #gg += 1
listaimenaSlikaPNG = []
listaimenaSlikaJPEG = []
ggg = 0
gggg = 0
ggggg = 0
gggggg = 0
if(len(listaLinkovaVideaFinale) != 0):
    while ggg < len(listaLinkovaVideaFinale):
        listaimenaVidea.append(listaLinkovaVideaFinale[ggg].split(".mp4?", 1)[1])
        ggg+=1

if(len(listaLinkovaWEBMGIF) != 0):
    while gggg < len(listaLinkovaWEBMGIF):
        listaimenaWEBMGIF.append(listaLinkovaWEBMGIF[gggg].split(".gif?",1)[1])
        gggg+=1

if(len(listaLinkovaSlikaPNG) != 0):
    while ggggg < len(listaLinkovaSlikaPNG):
        listaimenaSlikaPNG.append(listaLinkovaSlikaPNG[ggggg].split(".png?",1)[1])
        ggggg+=1
if(len(listaLinkovaSlikaJPEG) != 0):
    while gggggg < len(listaLinkovaSlikaJPEG):
        listaimenaSlikaJPEG.append(listaLinkovaSlikaJPEG[gggggg].split(".jpeg?",1)[1])
        gggggg+=1



print('Starting download!')


counterpng = 0
counterjpeg = 0
for items in listaLinkovaSlika:
    downloadstr = items 
    name = str(listaimena[y])
    img_data = requests.get(downloadstr).content   
    with open(name + ".jpg", 'wb+') as handler: 
       handler.write(img_data)   
    y+=1  
#download webm
for items in listaLinkovaSlikaPNG:
    downloadstr = items 
    name = str(listaimenaSlikaPNG[counterpng])
    img_data = requests.get(downloadstr).content   
    with open(name + ".jpg", 'wb+') as handler: 
       handler.write(img_data)   
    counterpng+=1  

for items in listaLinkovaSlikaJPEG:
    downloadstr = items 
    name = str(listaimenaSlikaJPEG[counterjpeg])
    img_data = requests.get(downloadstr).content   
    with open(name + ".jpg", 'wb+') as handler: 
       handler.write(img_data)   
    counterjpeg+=1  

print("Finished downloading pictures")





for items in listaLinkovaWEBMGIF:
    downloadstr = items 
    name = str(listaimenaWEBMGIF[webmgif])
    img_data = requests.get(downloadstr).content    
    with open(name + ".gif", 'wb+') as handler: 
       handler.write(img_data)   
    webmgif+=1  
#download videos


print("Finished downloading gifs")

for items in listaLinkovaVideaFinale:
    downloadstr = items 
    name = str(listaimenaVidea[z])
    img_data = requests.get(downloadstr).content   
    with open(name + ".mp4", 'wb+') as handler: 
       handler.write(img_data)   
    z+=1 
print("Finished downloading videos")

print("done")
input("Press enter to close")