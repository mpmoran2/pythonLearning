# File handling allows you to save data entered by a user or mutated by your code
# Usually use databases for that but sometimes need files

# First, create a .txt file (Ours is filehandling.txt
# You need to open it before doing anything to it. (Open, read/write, close)

# use the open() function. Paramaters are "filename.txt", 'mode'
# file = open("filehandling.txt", 'w') # We will open the file filehandling.txt in the write mode. We can ONLY write the file
# # Here we would do something to the file
# # After we are done reading or writing data to the file we need to close to avoid errors
# file.close()


# Reading Data from a File
# file = open("filehandling.txt", 'r') # Mode is read
# content = file.read() # This will read the content from the file and save into the variable content.
# # Parameter here would be reading 10 bytes of data from the file
# # If you only need to read a particular line, use .readline() function
# print(content)
# file.close()

# Adding data to the file
file = open("filehandling.txt", 'w')
file.write("Hire me please")
file.close()

file = open("filehandling.txt", 'r')
content = file.read()
print(content)
file.close()

# If we need to add more we must use the Append mode, other wise anything we try to add in write mode will just over ride the previous data in the .txt file

# Appending data to the file
