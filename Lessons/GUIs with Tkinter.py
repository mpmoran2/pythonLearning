# GUI
    # Graphical User Interface

# this imports EVERYTHING with the * from tkinter
from tkinter import *
# need a window to place elements
root = Tk() # creates the class an object

label1 = Label(root, text="Hewwo Wowold") # create a lable lets our code know that this class belongs to root and the text of it
label1.pack()# this adds this label to the window with .pack()

#if we run from this point, it will not show up because it auto closes the window.
# to get the window to stay open until we tell it to close we need the following code
root.mainloop()

# now when you run your code, it pops up!


