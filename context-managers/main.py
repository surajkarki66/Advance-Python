file = open("./context-managers/file.txt", "w")
file.write("Hello")
file.close()

# lets say by some reason file is not close, it throw error in second line
# to avoid this

try:
    file.write("Good")

finally:
    file.close()

"""
Context managers allow you to allocate and release resources precisely when you want to.
The most widely used example of context managers is the with statement.
Suppose you have two related operations which you’d like to execute as a pair,
with a block of code in between. Context managers allow you to do specifically that. 

A common use case of context managers is locking and unlocking resources and 
closing opened files (as I have already shown you).


"""

# another way is to use context manager

with open("./context-managers/file.txt", "r") as file:
    file.write("Bye")
