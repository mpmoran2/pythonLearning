 # Write code to open file named demo.txt and put in random data
file = open("demo.txt", 'w')
file.write("Hello Moonshine")
file.close()
 # Open file, read contents, display as output
file = open("demo.txt", 'r')
result = file.read()
print(result)
 # Add additional text to file on a new line
file = open("demo.txt", 'a')
file.write("\n You look radiant today")
file.close()

file = open("demo.txt", 'r')
result = file.read()
print(result)