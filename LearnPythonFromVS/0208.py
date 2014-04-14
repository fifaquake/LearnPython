import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*** this is a comment */'

text2 = '''/* this is a
              multiline comment */
'''

print(comment.findall(text1))
print(comment.findall(text2))

commentDOTALL = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(commentDOTALL.findall(text2))

commentNonCapture = re.compile(r'/\*((?:.|\n)*?)\*/')
print(commentNonCapture.findall(text2))