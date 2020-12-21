file = open('test.txt')
print(file.read(7))
print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

#file.close()

#print line by line using readline method

#file=open('test.txt')

#for i in range(1,4):
#    print(file.readline())

#file.close()


#another way of printing

#line = file.readline()
#while line!='':
 #   print(line)
   # line=file.readline()




#readlines method

for i in file.readlines():
    print(i)



file.close()