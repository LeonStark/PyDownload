#coding=utf-8

import urllib.request
import re
from bs4 import BeautifulSoup
import os
from tkinter import *
#<span class="thispage" data-total-page="131">1</span>

def download():
    url_head = url_text.get()
    #https://movie.douban.com/celebrity/1022004/photos/
    saveDir = "D:\\kk\\"
    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
    y=1
    if url_head.strip() == '':
        url_head= "https://movie.douban.com/celebrity/1012533/photos/"
    content=urllib.request.urlopen(url_head).read()
    soup=BeautifulSoup(content, "html.parser")
    span_all = soup.find_all("span",attrs={'class':'thispage'})
    for spans in span_all:
        len = int(spans.attrs['data-total-page'])
    for y in range(1,len+1):
        page=(y-1)*30
        url = url_head+"?type=C&start=%s&sortby=like&size=a&subtype=a" %page
        content=urllib.request.urlopen(url).read()
        soup=BeautifulSoup(content, "html.parser")
        img_all=soup.find_all("img",src=re.compile('.doubanio.com/view/photo'))
        
        
        print("正下载第%s页" %y)
        x=30*y
        for img in img_all:
            img_str=img["src"]
            #print("img_str = %s" %img_str)
            img_name="%s-%s.jpg" %(y,x)
            path="D:\\kk\\"+img_name    #保存图片路径
            urllib.request.urlretrieve(img_str,path)
            x += 1
            y += 1
    print("已下载%s张图片" %x*y)

def windowExit():
    window.destroy()
    sys.exit();

if __name__ == '__main__':
    window = Tk()
    window.geometry("300x300")
    url_text = Entry()
    url_text.pack()
    Button(window,text="download",command=download).pack()
    Button(window,text="exit", command=windowExit).pack()
    window.mainloop()
