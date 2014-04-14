text = 'yeah, but no, but yeah, but no, but yeah'
newtext = text.replace('yeah', 'yep')
print(text)
print(newtext)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
import re
newtext = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)
print(newtext)

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat =re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date, text))