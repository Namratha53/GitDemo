#print('hello')

#a=6
#print(a)
#print('The value is', a, "end of sentence")

x = [1,2,3,4,5]
y= ['q', 'w', 'e', 'r']

#print(x[1:-1])

x.insert(3,'new member')
print(x)
x.append("newest member")
print(x)
del x[2]
print(x)

values = [1,2,"Nam", 4.5]
print(values)
print(values[2])
values[2] = "Namratha"
print(values)

Dicti = {1:"Name", 'age':23, 3:"old"}
print(Dicti[3])

dict={}
dict[1]="A String"
dict["Type"]="STR"
dict[2]=5
print(dict)

#loops
a='Orange'

if type(a)==str:
    print(a)
else:
    print('incorrect')
print('If Else statement succesfully completed!')

val=[1,3,5,7,9]
for i in val:
    print(i*2)
    
sum=0
for j in range(1,6):
    sum=sum+j

print('Total:',sum)
print('******************************************')

for k in range(1,10,2):
    print(k)
print('******************************')

l=6
while(l>1):
    if(l==3):
        l-=1
        continue
    print(l)
    l-=1
print('While loop printed!')
print('*********************************')


str="Nammu.G"
str1='Vinu'
str3='Nam'
print(str[0:3])
print(str+str1)
print(str3 in str)
var = str.split(".")
print(var[0])
var1="    Namratha    "
print(var1.strip())
print(var1.lstrip())
print(var1.rstrip())