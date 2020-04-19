import urllib.request, urllib.parse,urllib.error
import json


link= input('Enter the link:')
uh=urllib.request.urlopen(link)
data=uh.read().decode()
print('Retrived:',len(data), 'characters')
lst=list()
js=json.loads(data)

for i in range(len(js["comments"])):

    lst.append(js["comments"][i]["count"])
print("Count:", len(lst))
print("Sum:", sum(lst))
