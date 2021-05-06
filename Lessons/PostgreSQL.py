#  How Code Execution works
# Input => Python Code => Output => Console
    # Usually when console is closed and code stops running, information is lost
    # If we want to save the input/output even if code stops, we save it to Databases.

# Why would we want to store our data?
    # By storing data, we are about to perform these operations:
        # Can read the data when we want without running our code
            # Ex: Banking Application
        # Can update/modify data
            # Ex: Updating addresses/name/contact info
        # Can delete data

# Data is stored in the form of tables
    # EX: ID, Name, Address, Phone Number. These are attributes of a person.

# PostgreSQL INFO
    # A general purpose and object-relational database management system
        # Object-relational: Objects, classes, & inheritance is directly supported in db schemas
    # Originally designed to work on UNIX like platforms but can not work on Mac and Windows
    # Is open source (source code available under PostgreSQL liscence
        # Can use, modify, and distribute the code as well as use in commercial applications for free
    # Highly stable and used by most major apps
        # SQLlite is used more developmental

    # Creating a database
        # Open SQL Shell
        # \l lets you see a list of databases you have

        # to create: CREATE DATABASE (name);
        # \l to make sure it was created
            # if you need to delete it: drop database (name);
        # to go into that database: \c (database name)
