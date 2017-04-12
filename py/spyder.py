import urllib.request as request

with request.urlopen('http://python.org/') as response:
    html = response.read()

print(html)
