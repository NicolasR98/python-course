# file = open('./myfile.txt', 'r')
# contents = file.read()
# print(contents)

with open('./myfile.txt') as my_file:
    contents = my_file.read()
    print(contents)
