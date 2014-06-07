#coding=utf-8
#author: Jesse MENG
#2014.06.07
import urllib
from bs4 import BeautifulSoup

def capture(base,ext):
    prefix='img/'+ext[3:]+'_'
    content = urllib.urlopen(base+ext).read()
    soup = BeautifulSoup(content)
    sel = soup.find_all('img')
    for i,e in enumerate(sel):
        original = e['src']
        l=original.rfind('/')
        r=original.rfind('?')
        if r>0:   
            a, b=urllib.urlretrieve(base+e['src'], prefix+str(i)+'_'+original[l+1:r])

urls=[]
base_url = "http://meizhi.im"
content = urllib.urlopen(base_url).read()
soup = BeautifulSoup(content)
sel = soup.find_all('div',{"class":"box"})
for e in sel:
    capture(base_url,e.a['href'])
