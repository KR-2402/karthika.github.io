import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et


url=input('Enter location: ')
uh = urllib.request.urlopen(url) 
data = uh.read() 

tree=et.fromstring(data)
lists=tree.findall('commentinfo/commemts/comment')
s=0
for l in lists:
    sum+=l.get('count')
print(sum)

