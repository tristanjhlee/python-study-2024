from xml.etree.ElementTree import *

person = Element('Person')
name = Element('Name')
name.text = 'Eric'
person.append(name)

age = Element('Age')
age.text = '15'
person.append(age)

SubElement(person, 'adress').text = 'Seoul'

no = Element('No')
no.text = '17'
person.insert(1, no)

person.remove(no)

person.attrib['date'] = '2024-05-18'

dump(person)

#ElementTree(person).write('/Users/JuneHyukLee/Desktop/person.xml')