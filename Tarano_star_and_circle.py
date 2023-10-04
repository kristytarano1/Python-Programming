#Author Name: Kristy Tarano
#Date: 2/13/2022
#Program Name: Star and Circle Graphics
#Purpose: The purpose of this program is to draw stars with 5 circles around it 9 times.



#imports the module Turtle
import turtle

#Assigns Turtle to variable star
star = turtle.Turtle()

#Defines distance between each star/circle
star_distance = 150

#Number of stars in each row
width = 3

#Number of stars in each column
height = 3

#Positions the turtle at a specific placement in the window
star.penup()
star.goto(0, 150)
star.pendown()

#Function that defines the star and how it will be drawn. Also referencing the 
# circles being drawn at each vertices
def draw_star():
    for i in range(5):
        star.forward(50)
        draw_circle() #calls the function to draw the circle
        star.right(144)

#Function that creates the circle 
def draw_circle():
    star.circle(25)

#Loop which calls upon the Draw Star function, and moves the location of the turtle to correct position to draw the next iteration of the star/circles
for y in range(height):
    #Loop to create the next row of star/circles
    for i in range(width):
        draw_star()
        star.penup()
        star.forward(star_distance)
        star.pendown()
    #Below is the positioning of the next column of star/circles
    star.penup()
    star.backward(star_distance * width)
    star.right(90)
    star.forward(star_distance)
    star.left(90)
    star.pendown()

#Turtle is finished
turtle.done()