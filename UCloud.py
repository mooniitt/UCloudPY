import urllib2,re
url = r'http://106.75.28.160/UCloud.txt'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
text = response.read()
print text.count("UCanUup")
