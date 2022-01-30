import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'book':
            print("-----BOOK-----")
            print("ID: {}".format(attrs['id']))
    
    def characters(self, content):
        if self.current == 'author':
            self.author = content
        elif self.current == 'title':
            self.title = content
        elif self.current == 'genre':
            self.genre = content
        elif self.current == 'price':
            self.price = content
        elif self.current == 'publish_date':
            self.pub_date = content
        elif self.current == 'description':
            self.desc = content
    
    def endElement(self, name):
        if self.current == 'author':
            print("Author: {}".format(self.author))
        elif self.current == 'title':
            print("Title: {}".format(self.title))
        elif self.current == 'genre':
            print("Genre: {}".format(self.genre))
        elif self.current == 'price':
            print("Price: {}".format(self.price))
        elif self.current == 'publish_date':
            print("Publication Date: {}".format(self.pub_date))
        elif self.current == 'description':
            print("Description: {}".format(self.desc))
        self.current = ''

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')