import pickle
import json
import csv
import xml.etree.ElementTree as ET

## Serializable (Pickle) Mixin ###################################################################################
class Serializable():
    def __init__(self):
        pass
    def dump(self, filename):
        pickle.dump(self, open(filename, 'wb'))

    def load(self, filename):
        tempload = pickle.load(open(filename, 'rb'))
        self.title = tempload.title
        self.author = tempload.author
        self.price = tempload.price

## JSON Mixin ####################################################################################################
class JSONMixin():
    def __init__(self):
        pass
    def dump(self, filename):
        ## form a dictionary from our Book object
        myDict = dict()
        myDict['title'] = self.title
        myDict['author'] = self.author
        myDict['price'] = self.price
        ## write to JSON file
        with open(filename, 'w') as outfile:
            outfile.write(json.dumps(myDict))

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            myDict = json.load(file)
        self.title = myDict['title']
        self.author = myDict['author']
        self.price = myDict['price']

## XML Mixin ####################################################################################################
class XMLMixin():
    def __init__(self):
        pass
    def dump(self, filename):
        data = ET.Element('book')
        title = ET.SubElement(data, 'title')
        author = ET.SubElement(data, 'author')
        price = ET.SubElement(data, 'price')
        title.text = self.title
        author.text = self.author
        price.text =  str(self.price)
        # convert XML doc to bytes object for flushing to tile
        xmldoc = ET.tostring(data)
        # save to file       
        with open(filename, 'wb') as file:
            file.write(xmldoc)

    def load(self, filename):
        # parse XML file.. seems to be able to open files only with name (cool!)
        tree = ET.parse(filename)
        # get root of XML doc
        root = tree.getroot()
        # this is nasty... but works..not sure if subelements are gauranteed to be stored in the same position otherwise would use array indexing
        for child in root:
            if child.tag == 'title':
                self.title = child.text
            if child.tag == 'author':
                self.author = child.text
            if child.tag == 'price':
                self.price = child.text 

## CSV Mixin ####################################################################################################
class CSVMixin():
    def __init__(self):
        pass
    def dump(self, filename):
        header = ['title','author','price']
        entry = [self.title, self.author, self.price]
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)    
            # write the header
            writer.writerow(header)
            # write the data
            writer.writerow(entry)

    def load(self, filename):
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                # process the 'line' -- there's only one
                self.title = line[0]
                self.author = line[1]
                self.price = line[2]

class Book(Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self) -> str:
        return ('Title: {0}, Author: {1}, Price: {2}'.format(self.title, self.author, self.price))


## main() #########################################################################################################
def main():
    b = Book("Python Workout", "Reuven Lerner", 39)
    print(b)
    b.dump('book.data')      # book is now stored on disk, in pickle format

    b2 = Book('blah title', 'blah author', 100)
    b2.load('book.data')     # title, author, and price now reflect disk file
    print(b2)

if __name__ == "__main__":
    main()
