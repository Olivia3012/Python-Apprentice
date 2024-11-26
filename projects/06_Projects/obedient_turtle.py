"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk


# TODO)
#   1. Create a turtle.
import turtle                           
turtle.setup(width=600, height=600)    

tina = turtle.Turtle()                  

tina.shape('turtle')                   
tina.speed(2)           
#   2. Write 3 function definitions for drawing a square, triangle, and
sides=4
def draw_polygon(sides):

    angle = 360/sides

    for i in range(sides):                 
        tina.forward(100)                             
        tina.left(angle)   

sides=3 
def draw_triangle(sides):

    angle=360/sides

    for i in range(sides):
        tina.forward(100)
        tina.left(angle)

sides=50
def draw_circle(sides):
    angle=360/sides

    for i in range(sides):
        tina.forward(10)
        tina.left(angle)


#      circle.
#   3. Ask the user for the for a shape to draw.
shape = simpledialog.askstring("choose","Choose a shape (triangle, square, circle)")
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)

if shape == "triangle":
    draw_triangle(3)
elif shape == "square":
    draw_polygon(4)
elif shape == "circle":
    draw_circle(50)
else:
    simpledialog.askstring("nope!!")


pass
