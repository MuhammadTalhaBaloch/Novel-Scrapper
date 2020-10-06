import requests
from bs4 import BeautifulSoup
    
import re


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring  

session = requests.Session()
headers = {'User-Agent': 'Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02'}


#... whatever requests config you need here

 #x=149
WebUrl='https://www.readlightnovel.org/boku-no-toraburu'
#print(WebUrl)
response = session.get(WebUrl,headers=headers)
url = response.url
page = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


results = soup.find_all('div', class_ = 'col-lg-12 chapters')
first_movie = results[0]

litag=first_movie.find_all("li")

for i in litag:
        print(i.a.get('href'))
#phela=first_movie.ul

#litag=phela.find_all("li")
#print(litag[4].text)
#print(litag[4].a.text)

#for i in range(len(litag)):
 #   if i % 2 == 0: 
  #          print("Name:{0}:  \n".format(litag[i].a.text))
   #         print("Url:{0}:  \n".format(litag[i].a.get('href')))

#for tag in phela.find_all("li"):
        


#print('\n')
#print(first_movie.a.text)
#print('\n')
#print(first_movie.a)
#print('\n')
#print(first_movie.div.p)