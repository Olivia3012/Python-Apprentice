"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""


from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age
n1 = simpledialog.askinteger("Adding caculator", "Type in first number.")

1
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

n2 = simpledialog.askinteger("Adding caculator","Type in second number.")

# Display the sum of the two numbers 

answer = n1 + n2

messagebox.showinfo( "Your numbers added together are ", n1 + n2)

# Keep the window open

