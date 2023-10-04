#Author Name: Kristy Tarano
#Date: 1/22/2022
#Program Name: Fahrenheit to Celsius Converter
#Purpose: The purpose of this program is to convert a user-inputted temperature from Fahrenheit to Celsius and show the user the new value



#This is where the user is asked to enter a value which will then be stored as the variable temperature
temperature = float(input("What is the temperature outside right now, in Fahrenheit? "))
    
    
#Calculates/converts value entered by user into celsius, as well as formats the new value to only contain two decimal values
celsius = format(((temperature - 32)* 5/9), '.2f')


#Displays the new value for the user
print('The temperature outside in Celsius is', celsius)
