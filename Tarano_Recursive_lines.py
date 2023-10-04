#Author Name: Kristy Tarano
#Date: 4/10/2022
#Program Name: Largest Number in List Program
#Purpose: The purpose of this program is to obtain the largest number from a randomly created list using recursion


#Importing Random module to generate list of random numbers
import random



#Function where random list is created
def main():
    #Declaring empty list
    numList = []

    #Loop to append 10 random numbers to empty list
    for i in range(10):
        numList.append(random.randint(1,1000))
    
    print()
    print(numList)#Prints randomly generated list 
    bigNum(numList)#Recursive function to find largest item in list

#Function to find largest number in list 
def bigNum(list):
    number = 0 #Declaring a variable 
    for i in list: #Loop to iterate over list and find largest number, passing any smaller numbers
        if i > 0 and i > number:
            number = i 
        else:
            pass
    
    print("\nThe biggest number:", number)
    print("The biggest number index:", list.index(number))#Prints the index of the largest number in the list
    print()

#Calling the main function
main()




