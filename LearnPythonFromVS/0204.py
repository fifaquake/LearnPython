text = 'yeah, but no, but yeah, but no, but yeah'

print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')


dateWithGroup = re.compile(r'(\d+)/(\d+)/(\d+)')
m = dateWithGroup.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(dateWithGroup.findall(text))

for m in dateWithGroup.finditer(text):
    print(m.groups())