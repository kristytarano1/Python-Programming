#Author Name: Kristy Tarano
#Date: 2/26/2022
#Program Name: Lo Shu Magic Square Tester
#Purpose: The purpose of this program is to test whether a list of numbers can create a Lo Shu Magic Square .



#Function to receive the numbers from user
def number():
    numbers = [[0, 0, 0, 0],  #defines list with 16 empty slots 
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    row = 4 #variable constraint to determine number of rows in list
    col = 4 #variable constraint to determine number of column in list
    for r in range(row):
        for c in range(col):
            entry = int(input('Enter a number: '))#takes input from user and stores into variable
            numbers[r][c] = entry #stores the number into specific coordinate in list
    return numbers #returns the newly filled list as output


#Function where testing of numbers is conducted
def loShu(num):
    count = 0 #Variable constraint used to limit/test the loop
    diagLeft = num[0][0] + num[1][1] +  num[2][2] + num[3][3] #Sums the total of diagnals from left to right
    diagRight = num[0][3] + num[1][2] + num[2][1] + num[3][0] #Sums the total of diagnals from right to left
    colum0 = num[0][0] + num[1][0] + num[2][0] + num[3][0] #Sums the total for column in position 0
    colum1 = num[0][1] + num[1][1] + num[2][1] + num[3][1] #Sums the total for column in position 1
    colum2 = num[0][2] + num[1][2] + num[2][2] + num[3][2] #Sums the total for column in position 2
    colum3 = num[0][3] + num[1][3] + num[2][3] + num[3][3] #Sums the total for column in position 3


    while count < len(num): #Condition to run only as many times as length of list
        for value in num:
            row = sum(value) #Sums the value in each row
            if row == diagLeft == diagRight == colum0 == colum1 == colum2 == colum3: #Condition to check if row, columns, and diagnals all sum to the same number
                count += 1 #Increase the count variable as part of the limited While condition 
                if count == len(num): #If count has successfully reached 4, which means all four rows, columns and diagnals match; then it can print success
                    print('\nSuccess! Your list of numbers does create a Lo Shu Magic Square.\n')
                    print('\n'+ str(num) + '\n Magic constant: ' + str(row)) #Prints the numbers and magic constant
            else: #Condition if row, columns, and diagnals don't sum to the same number
                count = 5 #forces While condition to quit as numbers don't match
                print('\nUnfortunately, your list of numbers does not create a Lo Shu Magic Square.\n')
                print('\n'+ str(num) + '\n') #Prints the numbers and magic constant
                break #breaks the loop
    

loShu(number())








