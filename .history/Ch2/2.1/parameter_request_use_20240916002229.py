import urllib.request

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
