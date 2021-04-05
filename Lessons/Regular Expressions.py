# Allows us to manipulate strings
    # Helps with learning Django
    # Expressions that allows us to manipulate all types of strings

# 2 Popular uses
    # Verify strings match a particular pattern (log in verification)
    # Substitutions in a string

# Example of use. Need the module first
import re

pattern = r"eggs"
    # define the pattern. r"" lets python know we are using a regular expression that contains the string eggs
if re.match(pattern,"eggseggseggsbacon"):
    print('Match found')
else:
    print('No match has been found')


# Search & Find All

# Find & Replace

# Dot Metacharacter

# Caret & Dollar metacharacter

# Character Class

# Star Metacharacter

# Group