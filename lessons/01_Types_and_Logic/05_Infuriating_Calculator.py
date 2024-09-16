"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw()


# Ask the user for the first number   
n1 = simpledialog.askinteger("Adding caculator", "Type in first number.")
# Ask the user for the second number
n2 = simpledialog.askinteger("Adding caculator","Type in second number.")

# Ask the user for the math operation
operation = simpledialog.askstring("Adding caculator" , "What operation would you like to use? Please do not use word form. If you would prefer division, use '/'.")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "+" :
   messagebox.showinfo( "Your numbers added together are ", n1+ n)

elif operation == "-" :
   messagebox.showinfo( "Your numbers subtracted are ", n1 - n2)

elif operation == "x" :
   messagebox.showinfo( "Your numbers multiplied together are ", n1 * n2)

elif operation == "/" :
   messagebox.showinfo( "Your numbers divided are ", n1 / n2)
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
else:
   messagebox.showinfo( "error")
# Keep the window open
