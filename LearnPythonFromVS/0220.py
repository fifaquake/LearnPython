data = b'Hello world'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')
print(data)
print(data.startswith(b'Hello '))
print(data.split())