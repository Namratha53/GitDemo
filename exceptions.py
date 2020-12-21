itemsinCart=0

if itemsinCart!=2: #raise Exception('Count not matching')
    pass

assert (itemsinCart==0)

try:
    with open('fill.txt', 'r') as reader:
        print(reader.read())

except:
    print('Failure in try block')



try:
    with open('test.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print('Finally executed')


