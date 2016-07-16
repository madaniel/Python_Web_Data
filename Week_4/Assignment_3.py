import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    count += int(tag.contents[0])

print count

"""
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('class="comments"', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
   """