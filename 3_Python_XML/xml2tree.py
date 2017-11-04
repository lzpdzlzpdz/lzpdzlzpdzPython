import xml.etree.ElementTree as ET

print 'start'

tree = ET.ElementTree()
tree = ET.parse('book.xml')
root = tree.getroot()
print root


print 'process'

p = tree.find("country")     # Finds first occurrence of tag p in body
print p
for item in p:
    print item.tag,item.text
    
print '\n'
p = tree.findall("country")     # Finds first occurrence of tag p in body
print p
for item in p:
    for subitem in item:
        print subitem.tag,subitem.text
        if subitem.tag == 'rank':
            subitem.text = '111111'


print 'save'
tree.write("output.xml")