"""
Create hotel management system. Must have a tuple, list, dictionary, 
game loop (must be able to go on untl requested), functions.
You also have to be able to add and remove guests amd give the guest(s) a final expense for 
their stay. Finally, you need to ad some of your own creativity and add another 
thing or two to your project. Good luck and begin!

Requirents:
tuple still need
list
dictionary clarify
game loop need
function
add and remove guests part of dictionary
give guests a final price
add
all functionalities are functions (everything must be in a def)
"""

from tkinter import messagebox, simpledialog, Tk
import sys
import random

guest = {}
hotel_levels = (1, 2, 3,4,5,6)
room_numbers1 = [1,2,3,4,5]
room_numbers2 = [6,7,8,9,10]
room_numbers3 = [11,12,13,14,15]
room_numbers4 = [16,17,18,19,20]
room_numbers5 = [21,22,23,24,25]
room_numbers6 = [26,27,28,29,30]


dictionary = {}
while True:

    def hotel_checkinandcheckout(dictionary):
        booking = simpledialog.askstring("Checking", "Are you booking rooms? (if not, enter 'no')")
        guest_name = simpledialog.askstring("Check-in", "What is your name?")
        if booking == "yes":
            messagebox.showinfo("Checking in", "Welcome to the Ritz-Carlton")
            number_rooms = simpledialog.askinteger("Rooms", "How many rooms would you like to book?")
            number_nights = simpledialog.askinteger("Nights", "How many nights would you like stay?")
            messagebox.showinfo("You will be given a room number when you check in.")
        elif booking == "no":
            in_or_out = simpledialog.askstring("Welcome", "Are you checking in or out")
            if in_or_out == "in":
                prefered_level = simpledialog.askinteger("Levels", "What level of the hotel would you prefer? (1,6) ")
                if prefered_level == 1:
                    room_numbers = room_numbers1
                elif prefered_level == 2:
                    room_numbers = room_numbers2
                elif prefered_level == 3:
                    room_numbers = room_numbers3
                elif prefered_level == 4:
                    room_numbers = room_numbers4
                elif prefered_level == 5:
                    room_numbers = room_numbers5
                elif prefered_level == 6:
                    room_numbers = room_numbers6
                number_room = simpledialog.askinteger("rooms", "How many rooms did you book?")
                if number_room > 6:
                    messagebox.showinfo("Error", "You can only book six rooms at a time.")
                in_levels = 0
                for i in range(number_room):
                    choosing_rooms = room_numbers[in_levels]
                    messagebox.showinfo("Your Room", choosing_rooms)
                    in_levels+=1

                    
                    dictionary = {
                        guest_name: choosing_rooms
                    }

                    guest[guest_name]= choosing_rooms

                    if guest_name in dictionary:
                        room_numbers.remove(choosing_rooms)
                        print( "Check")
                    
                    print(dictionary)

                    if number_room > 6:
                        messagebox.showinfo("Oops", "something went wrong")
                        break
                    elif choosing_rooms > room_numbers[-1]:
                        messagebox.showinfo("Oops", "Error")
                        break

                        
                    
            
            if in_or_out == "out":
                guest_name = simpledialog.askstring("Check-out", "What was your name?")
                number_room = simpledialog.askinteger("Rooms", "How many rooms did you book?")
                number_night = simpledialog.askinteger("Nights", "How many nights have you stayed with us?")
                bonuses = simpledialog.askstring("Deals", "Do you have chase saphire? If yes type yes, if no, type no")
                if bonuses == 'yes':
                    saphire = 50
                    messagebox.showinfo("Yay", "You just saved $50!")
                else:
                    messagebox.showinfo("Sorry. whthout the chase saphire card you don't get any special deals.")
                    saphire = 0
                final_cost = number_room*number_night*450 - saphire
                messagebox.showinfo("Yay", "Thank you for staying with us.")
                messagebox.showinfo("Final Cost", final_cost)
                del guest[guest_name]
                for key, value in dictionary(guest_name):
                    room_numbers.add(value)


            else:
                messagebox.showinfo("Oops", "something went wrong")

        else:
            messagebox.showinfo("Oops", "something went wrong")

        
        


    
    

    hotel_checkinandcheckout(dictionary)










