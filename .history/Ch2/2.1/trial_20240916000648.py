# -*- coding: utf-8 -*-
import urllib.request

response = urllib.request.urlopen("https://www.python.org")
print(type(response))