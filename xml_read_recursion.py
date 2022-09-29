from cgi import print_arguments
import xml.etree.ElementTree as et

def printXml(element):
    if element.text != '\n':
        print(element.text)
    if element:
        childern = element.getchildren()
        if len(childern)==0:
            return 0
        else:
            for child in childern:
                printXml(child)

tree = et.parse("xmldata.xml")
root = tree.getroot()
print(root)

printXml(tree)