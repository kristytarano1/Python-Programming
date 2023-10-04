#Author Name: Kristy Tarano
#Date: 1/28/2022
#Program Name: Flu-CommonCold-Allergies-COVID-19 Diagnostic test
#Purpose: The point of this program is to determine if the user has Flu/Allergies/Covid-19/CommonCold


#function to print invalid entry and end program
def end():
    print('\nInvalid input entered, program ended\n\n')

#function that states the disclaimer at the end of each possible branch of options
def disclaimer():
    print('''\nThese are COMMON SYMPTOMS, which may vary from person to person. 
Only a doctor can give you a diagnosis.\n\n''')

#Intial statement beginning the program, and formats the users input into lower case
fever = (input('\nDo you have a fever? ')).lower()

#Beginning of If statement
if fever == 'yes':

    #Ask user next question and formats response into lowercase
    covid19 = (input('\nAre you experiencing shortness of breath? ')).lower()
    
    #if user selects yes, then they're prompted the following print statements and calls the disclaimer function
    if covid19 == 'yes':
        print('\nYou MAY have COVID-19.')
        print('\nOther symptoms are: \n-Cough \n-Fatigue \n-Weakness \n-Exhaustion')
        disclaimer()

    #if user selects no, then they're prompted the following print statements and calls the disclaimer function
    elif covid19 == 'no':
        print('\nYou MAY have the flu.')
        print('\nOther symptoms are: \n-Cough \n-Fatigue \n-Weakness \n-Exhaustion')
        disclaimer()

    #Calls the end function if anything besides yes or no is entered
    else:
        end()

#second if statement to the program
elif fever == 'no':

    #Ask user next question and formats response into lowercase
    allergies = (input('\nDo you have itchy eyes? ')).lower()
    
    #if user selects yes, then they're prompted the following print statements and calls the disclaimer function
    if allergies == 'yes':
        print('\nYou MAY have allergies.')
        print('\nOther symptoms are: \n-Sneezing \n-Runny Nose')
        disclaimer()

    #if user selects no, then they're prompted the following print statements and calls the disclaimer function
    elif allergies == 'no': 
        print('\nYou MAY have the common cold.')
        print('\nOther symptoms are: \n-Sneezing \n-Runny Nose \n-Mild chest discomfort')
        disclaimer()

    #Calls the end function if anything besides yes or no is entered
    else:
        end()

#Calls the end function if anything besides yes or no is entered
else:
    end()



#  student = 1

# while student <= 3:
#     total = 0
#     for score in range(1,4):
#         score = int(input("enter score: "))
#         total += score
#         average = total/3
#         print('student:', student, 'average:', average)
#         student += 1