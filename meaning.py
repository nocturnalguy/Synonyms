# Importing BeautifulSoup and request

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import sys

url = 'https://www.dictionary.com/browse/'

word=''

try:
	for i in range(1, len(sys.argv)):
		word += sys.argv[i]
except:
	print('\n No input given \n')
	exit(-1)

url += word

try:
	response = urlopen(url)
	html = response.read()
	response.close()
except:
	print('\n Sorry, either you are not connected to the Internet or there is no meaning for this word. \n')
	exit(-1)

pageSoup = soup(html, 'html.parser')

# Getting the Main Definations

section = pageSoup.section.section.div.findAll('section',recursive='false')

if(not section):
	print('\n No defination found')
	exit(-1)

for index in range(1, len(section)):
    
    partsOfSpeechContent = section[index].findAll('span', {
        'class':'one-click-content'
    });
    
    # Getting the Parts of Speech

    partsOfSpeech = section[index].find('span', {
        'class':'luna-pos'
    })
    
    print('\n #### ' + partsOfSpeech.text.capitalize() + ' #### \n')

    # Getting the Meaning

    for (i,item) in enumerate(partsOfSpeechContent):
        print('\t' + str(i + 1) + ". ",item.text, '\n')
        