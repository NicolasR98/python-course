file1 = open('myfile.txt', 'w')

my_text_list = ['This is Almazora\n', 'This is Castellon\n', 'This is Valencia\n']
text = 'This is Spain\n'

# Writing a string to file
file1.write(text)

# Writing multiple strings
file1.writelines(my_text_list)

# Closing a file
file1.close()

# Checking if data is written to file
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()