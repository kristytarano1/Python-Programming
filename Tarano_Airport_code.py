#Author Name: Kristy Tarano
#Date: 3/20/2022
#Program Name: Airport Coder Program
#Purpose: The purpose of this program is to return information regarding airports by entering acornoym for each airport

#Declaring dictionaries below with corresponding information regarding each IATA Code
NameDict = {'MIA':'Miami International Airport', 'MCO':'Orlando International Airport','DEN':'Denver International Airport','ATL':'Hartsfield-Jackson International Airport', 'LAX':'Los Angeles International Airport', 'PHX':'Phoenix Sky Harbor International Airport'}
CityDict = {'MIA':'Miami', 'MCO':'Orlando','DEN':'Denver','ATL':'Atlanta', 'LAX':'Los Angeles', 'PHX':'Phoenix'}
StateDict = {'MIA':'Florida', 'MCO':'Florida','DEN':'Colorado','ATL':'Georgia', 'LAX':'California', 'PHX':'Arizona'}

#Takes user input and capitalizes it
code = input('Enter IATA Code: ').upper()

#Checks to see if user input is in the dictionaries and gives corresponding input depending if it is or isn't 
if code not in NameDict and CityDict and StateDict:
    print() #prints empty space
    print("Airport code not found in dictionaries")
    print()#prints empty space
else:
    print()#prints empty space
    print(NameDict[code]+'\n'+ CityDict[code]+', '+ StateDict[code])#Concatinates each dictionary value and formats the way it'll print on the screen
    print()#prints empty space
    


