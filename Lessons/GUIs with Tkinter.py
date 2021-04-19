# GUI
    # Graphical User Interface

# this imports EVERYTHING with the * from tkinter
from tkinter import *
# need a window to place elements
# root = Tk() # creates the class an object

# label1 = Label(root, text="Hewwo Wowold") # create a lable lets our code know that this class belongs to root and the text of it
# label1.pack()# this adds this label to the window with .pack()

# frames
    # container within a windows which we add our widgets to
# newframe = Frame(root) #auto on top of window
# newframe.pack()
#
# otherframe = Frame(root)
# otherframe.pack(side=BOTTOM) #tells our code to put this at the bottom
#
# button1 = Button(newframe, text="UwU", fg="Purple")
# button2 = Button(otherframe, text="OwO", fg="Red")
#
# button1.pack()
# button2.pack()

#if we run from this point, it will not show up because it auto closes the window.
    # to get the window to stay open until we tell it to close we need the following code
# root.mainloop() # now when you run your code, it pops up!

# Grid Format
root = Tk()

label1 = Label(root, text= "First Name")
label2 = Label(root, text= "Last Name")

entry1 = Entry(root) # for input from User
entry2 = Entry(root)

label1.grid(row=0, column=0) #.grid allows us to place things in the frame as we like
label2.grid(row=1, column=0) #this lets us know it is under row one, aligned in the same column

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()





