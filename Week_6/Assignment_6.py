import json
import urllib2

url = "http://python-data.dr-chuck.net/comments_296659.json"

req = urllib2.urlopen(url)
json_buffer = json.load(req)

summy = 0

for item in json_buffer["comments"]:
    summy += item["count"]
print summy





