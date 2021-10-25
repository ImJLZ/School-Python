#!/usr/bin/env python3

# Everything after a hash sign (#) is considered a comment in Python

# The print statement could be written on the top-level (zero indentation),
# but here we have put it inside the main function.
# This enables TestMyCode (TMC) framework to work correctly.

# In more complicated programs it is good practise not to clutter the top-level of the program
# by using a main function as here.

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(("{:6d}".format(i * j,)), end='')
        print()

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == '__main__':
    main()
