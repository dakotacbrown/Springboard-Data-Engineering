from multiprocessing import AuthenticationError
import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

books = group.getElementsByTagName('book')

for book in books:
    print('-----BOOK-----')
    if book.hasAttribute('id'):
        print('ID: {}'.format(book.getAttribute('id')))
    
    print('Author: {}'.format(book.getElementsByTagName('author')[0].childNodes[0].data))
    print('Title: {}'.format(book.getElementsByTagName('title')[0].childNodes[0].data))
    print('Genre: {}'.format(book.getElementsByTagName('genre')[0].childNodes[0].data))
    print('Price: {}'.format(book.getElementsByTagName('price')[0].childNodes[0].data))
    print('Publication Date: {}'.format(book.getElementsByTagName('publish_date')[0].childNodes[0].data))
    print('Description: {}'.format(book.getElementsByTagName('description')[0].childNodes[0].data))
    print('')


newBook = domtree.createElement('book')
newBook.setAttribute('id', 'bk113')

author = domtree.createElement('author')
author.appendChild(domtree.createTextNode('Nylund, Eric'))

title = domtree.createElement('title')
title.appendChild(domtree.createTextNode('Halo: The Fall of Reach'))

genre = domtree.createElement('genre')
genre.appendChild(domtree.createTextNode('Sci-Fi'))

price = domtree.createElement('price')
price.appendChild(domtree.createTextNode('13.95'))

pub_date = domtree.createElement('publish_date')
pub_date.appendChild(domtree.createTextNode('2001-10-30'))

description = domtree.createElement('description')
description.appendChild(domtree.createTextNode('Legends are not simply born... they are willed into existence.'))

newBook.appendChild(author)
newBook.appendChild(title)
newBook.appendChild(genre)
newBook.appendChild(price)
newBook.appendChild(pub_date)
newBook.appendChild(description)

group.appendChild(newBook)

domtree.writexml(open('data2.xml', 'w'))