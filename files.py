myFile=open('myfile.txt', 'w')

print(myFile.name)
print(myFile.closed)

myFile.write('hello')
myFile.close()

myFile =open('myfile.txt', 'a')

myFile.write("more")
myFile.close()

myFile =open('myfile.txt', 'r+')

text = myFile.read(1)

print(text)
myFile.close()