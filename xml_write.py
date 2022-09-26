import xml.etree.ElementTree as et

data = et.Element('Students')

ele1 = et.SubElement(data,'Student')

sub_ele1 = et.SubElement(ele1,'Name')
fname = et.SubElement(sub_ele1,"Firstname")
lname = et.SubElement(sub_ele1,"Lastname")
fname.text = "Avnish"
lname.text = "Bharadva"

sub_ele2 = et.SubElement(ele1,"Rollno")
sub_ele2.text = "2"

ele2 = et.SubElement(data,"Student")

sub_ele3 = et.SubElement(ele2,"Name")
sub_ele3.text = "Avnish Bharadva"

sub_ele4 = et.SubElement(ele2,"Rollno")
sub_ele4.text = "2"

b_xml = et.tostring(data)

f = open("xmldata.xml","wb")
f.write(b_xml) 