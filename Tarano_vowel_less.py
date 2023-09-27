#Author Name: Kristy Tarano
#Date: 03/05/2022
#Program Name: VWL Program
#Purpose: The purpose of this program is to remove vowels from a user inputted statement

#Prints space prior to next statement
print()

#Takes user input 
sentence = input('Enter a sentence: ')

#Variable holding empty list
list = []

#List of vowels lower and upper case to be referenced in function
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

#Function to remove vowels 
def pigLatin(sen):
    print()#Prints space prior to next statement
    for vow in sen: #For loop to iterate through the sentence entered by user
        if vow not in vowels: #If the vowels are not in list vowels, append value to new list
            list.append(vow)
        else:
            pass #If value in Vowel list, pass
    
    newSentence = ''.join(list)#Creates a string from the list value and assigns it to a new value
    print(newSentence,'\n')#Prints new sentence created

pigLatin(sentence)#Calls function with inserted value from user

