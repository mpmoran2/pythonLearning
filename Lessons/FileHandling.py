# File handling allows you to save data entered by a user or mutated by your code
# Usually use databases for that but sometimes need files

# First, create a .txt file (Ours is filehandling.txt
# You need to open it before doing anything to it. (Open, read/write, close)

# use the open() function. Paramaters are "filename.txt", 'mode'
file = open("filehandling.txt", 'w') # We will open the file filehandling.txt in the write mode. We can ONLY write the file
# Here we would do something to the file
# After we are done reading or writing data to the file we need to close to avoid errors
file.close()
