import requests

#stores url response
#r = requests.get('https://xkcd.com/353')



#writes the png to a file
r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(r.content)