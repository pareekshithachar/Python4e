import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter:')
n= int(input('Enter count:'))
k= int(input('Enter Position:'))
html = urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

#to retrive all the anchor tags
tags =soup('a')
lst=list()
lst1=list()
#lst2= list()
for tag in tags:
    lst.append(tag.get('href', None))

for i in range(n-1):
    link= urllib.request.urlopen(lst[k-1], context=ctx).read()
    soup1=BeautifulSoup(link, 'html.parser')
    tags1 =soup1('a')
    for tag1 in tags1:

        lst1.append(tag1.get('href', None))
    for j in range(len(lst1)):
        if j in range(len(lst)):
            lst[j]=lst1[j]
        else:
            break
    lst1.clear()
print(lst[k-1])
