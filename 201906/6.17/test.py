import sys
print(sys.version)
print(sys.version_info)

import django
print(django.get_version())

import socket
import urllib.parse
import urllib.request
import urllib.error
 
#response = urllib.request.urlopen('https://www.python.org')
#print(response.read().decode('utf-8'))
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))

#data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
#response = urllib.request.urlopen('http://httpbin.org/post', data=data)
#print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')