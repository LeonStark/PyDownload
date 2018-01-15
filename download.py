#coding=utf-8

import urllib.request
#import urllib2
import re
from bs4 import BeautifulSoup
#<span class="thispage" data-total-page="131">1</span>
y=1
#设置下载页数，进行循环，当前为3页
for y in range(1,60):
    page=(y-1)*30
    url="https://movie.douban.com/celebrity/1012533/photos/?type=C&start=%s&sortby=like&size=a&subtype=a" %page
    #url="http://movie.douban.com/celebrity/1018980/photos/?type=C&start=%s&sortby=vote&size=a&subtype=a" %page
    content=urllib.request.urlopen(url).read()

    soup=BeautifulSoup(content, "html.parser")
    img_all=soup.find_all("img",src=re.compile('.doubanio.com/view/photo'))
    #下载链接头中有img3,img5，故正则时不写进去

    print("正下载第%s页" %y)
    #print("图片%s" %img_all)
    x=30*y
    for img in img_all:
        img_str=img["src"]
        #img_b=img_str.replace("thumb","photo")
        print("img_str = %s" %img_str)
        img_name="%s-%s.jpg" %(y,x)
        path="D:\\kk\\"+img_name    #保存图片路径
        urllib.request.urlretrieve(img_str,path)
        x += 1
    y += 1

print("已下载%s张图片" %x*y)
