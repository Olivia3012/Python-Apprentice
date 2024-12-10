"""
Create hotel management system. Must have a tuple, list, dictionary, 
game loop (must be able to go on untl requested), functions.
You also have to be able to add and remove guests amd give the guest(s) a final expense for 
their stay. Finally, you need to ad some of your own creativity and add another 
thing or two to your project. Good luck and begin!

Requirents:
tuple
list
dictionary
game loop
function
add and remove guests
give guests a final price
add
all functionalities are functions (everything must be in a def)
"""

from tkinter import messagebox, simpledialog, Tk
import sys
import random

guest = ()
hotel_levels = (1, 2, 3,4,5,6)
room_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
def hotel_checkinandcheckout():
    guest_name = simpledialog.askstring("Check-in", "What is your name?")
    in_or_out = simpledialog.askstring("Welcome", "Are you checking in or out?")
    if in_or_out == "in":
        messagebox.showinfo("Checking in", "Welcome to the Ritz-Carlton")
        number_rooms = simpledialog.askinteger("Rooms", "How many rooms would you like to book?")
        number_nights = simpledialog.askinteger("Nights", "How many nights would you like stay?")
        prefered_level = simpledialog.askinteger("Levels", "What level of the hotel would you prefer? (1,6) ")
        if prefered_level == 1:
            room_numbers = range(1,6)
        elif prefered_level == 2:
            room_numbers = range(6,11)
        elif prefered_level == 3:
            room_numbers = range(11,16)
        elif prefered_level == 4:
            room_numbers = range(16,21)
        elif prefered_level == 5:
            room_numbers = range(21,26)
        elif prefered_level == 6:
            room_numbers = range(26,31)
        choosing_rooms = random.choice(room_numbers)
        if number_rooms > 1:
            for more_rooms in range(number_rooms):
                messagebox.showinfo("Room Numbers", random.choice(room_numbers))
        room_number = messagebox.showinfo("Room number", choosing_rooms)
        guest.add(room_number, guest_name)
    
    elif in_or_out == "out":
        number_room = simpledialog.askinteger("Rooms", "How many rooms did you book?")
        number_night = simpledialog.askinteger("Nights", "How many nights have you stayed with us?")
        final_cost = number_room*number_night*450
        messagebox.showinfo("Final Cost", final_cost)
        guest.remove(room_number)

    dictionary = {
        guest_name: room_number,

    }
    

hotel_checkinandcheckout()








