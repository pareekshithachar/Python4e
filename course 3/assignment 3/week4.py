from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#ignoring ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =input('Enter:')
html= urlopen(url, context=ctx).read()
soup= BeautifulSoup(html, "html.parser")

tags= soup('span')
lst= list()
for tag in tags:
    lst.append(tag.contents[0])
    for i in range(len(lst)):
        lst[i]=int(lst[i])
print(sum(lst))
