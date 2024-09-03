
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

import turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.turtlesize(stretch_wid=10, stretch_len=10, outline=10)


def turtle_clicked(t, x, y):
    

    print('turtle clicked!')
    



    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees



# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))



turtle.done() 


