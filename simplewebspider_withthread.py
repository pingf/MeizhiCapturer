#coding=utf-8
#author: Jesse MENG
#2014.06.07
import urllib,threading  
from bs4 import BeautifulSoup

class ImagesCapturer(threading.Thread):  
    def __init__(self,base,ext):  
        threading.Thread.__init__(self)   
        self.base,self.ext=base,ext
    def run(self):  
        prefix='img/'+self.ext[3:]+'_'
        content = urllib.urlopen(self.base+self.ext).read()
        soup = BeautifulSoup(content)
        sel = soup.find_all('img')
        for i,e in enumerate(sel): 
            original = e['src']
            l=original.rfind('/')
            r=original.rfind('?')
            if r>0:  
                a, b=urllib.urlretrieve(self.base+e['src'], prefix+str(i)+'_'+original[l+1:r])

urls=[]
base_url = "http://meizhi.im"
content = urllib.urlopen(base_url).read()
soup = BeautifulSoup(content)
sel = soup.find_all('div',{"class":"box"})

for e in sel:
    ImagesCapturer(base_url,e.a['href']).start()  
    
