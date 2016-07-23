import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_296655.xml'
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
count = 0

for item in tree[1].findall("comment"):
    count += int(item.find("count").text)

print count
