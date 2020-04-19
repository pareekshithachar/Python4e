import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
results = list()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:


    url = input("Enter - ")
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    (data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('comments/comment/count')
    print('Count', len(counts))
    sum=0
    total = 0
    for count in counts:
        sum = int(count.text) + sum


    print ('Sum', sum)
    break
