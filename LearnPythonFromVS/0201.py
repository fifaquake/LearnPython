line = 'asdf fjdk; afed, fjek,asdf,       foo'
import re
result = re.split(r'[;,\s]\s*', line)
fields = re.split(r'(;|,|\s)\s*', line)
print(result)
print(fields)
