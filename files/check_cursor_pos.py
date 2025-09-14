#---Check cursor position while reading the file or writing a file

f=open('sample.txt','a+')
print('Cursor at',f.tell())
