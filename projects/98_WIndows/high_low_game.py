from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 100)

# 2. Print out the random variable that you made in step #1

print(random_num)

# 3. Code a for loop to run steps 4-10, 10 times
for guesses in range(10):

    # 4. Ask the user for a guess using a pop-up window, and save their response
    guess=simpledialog.askinteger("Enter a number between 1 and 100, inclusive", " ")

    # 5. If the guess is correct
    if guess==random_num:
        messagebox.showinfo("You win", "congrats")
        sys.exit(0)
        
        # 6. Win. Use 'sys.exit(0)' to end the program

    # 7. if the guess is high
    elif guess>random_num:
        messagebox.showinfo( "nice try", "Tis too high")
        # 8. Tell them it's too high
    # 9. Else if the guess is low
    elif guess<random_num:
        messagebox.showinfo("nice try", "tis too low")
        # 10. Tell them it's too low

#11. Outside of the loop, tell the user they lost
messagebox.showinfo("Byb-bye", "You Lost")

window.mainloop()
