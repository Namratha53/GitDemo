#read the file
#reverse the content
#place the reversed content back to the file



with open('test.txt','r') as reader:
    var = reader.readlines()
    reversed(var)
    with open('test.txt', 'w') as writer:
        for i in reversed(var):
            writer.write(i)
