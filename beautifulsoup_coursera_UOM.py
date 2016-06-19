import urllib 

from BeautifulSoup import *

import

n=int(raw_input('Enter n:'))

lis=list()

html=urllib.urlopen('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Annagayle.html').read()

soup=BeautifulSoup(html)

tags=soup('a')


for i in range(n):
 if i==0:
   for tag in tags:
    ta=str(tag.get('href',None))
    lis.append(ta)
 else:
   x=str(lis[17])
   html=urllib.urlopen(x).read()
   lis=list()
   soup=BeautifulSoup(html)
   tags=soup('a')
   for tag in tags:
    ta=str(tag.get('href',None))
    lis.append(ta)
    
print lis[17]
   
    
    

     
    
    




