import xml.etree.ElementTree as et

tree = et.parse("xmldata.xml")

print(tree)

root = tree.getroot()
print(root)

print(root.tag)
print(root.text)

for child in root:
    print(child.tag,child.text)
    for subchild in child:
        print(subchild.tag,subchild.text)