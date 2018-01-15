#coding=utf-8

import urllib.request
import re
from bs4 import BeautifulSoup
import os
#<span class="thispage" data-total-page="131">1</span>
y=1

saveDir = "D:\\kk\\"
if not os.path.isdir(saveDir):
    os.makedirs(saveDir)
for y in range(1,6):
    page=(y-1)*30
    url="https://movie.douban.com/celebrity/1012533/photos/?type=C&start=%s&sortby=like&size=a&subtype=a" %page
    content=urllib.request.urlopen(url).read()

    soup=BeautifulSoup(content, "html.parser")
    img_all=soup.find_all("img",src=re.compile('.doubanio.com/view/photo'))

    print("正下载第%s页" %y)
    x=30*y
    for img in img_all:
        img_str=img["src"]
        print("img_str = %s" %img_str)
        img_name="%s-%s.jpg" %(y,x)
        path="D:\\kk\\"+img_name    #保存图片路径
        urllib.request.urlretrieve(img_str,path)
        x += 1
    y += 1

print("已下载%s张图片" %x*y)
