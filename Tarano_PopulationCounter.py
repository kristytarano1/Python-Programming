#Author Name: Kristy Tarano
#Date: 2/04/2022
#Program Name: Population Growth Finder
#Purpose: The point of this program is to determine the growth of a population of species in x amount of days
 


#Requests user to enter amount of starting species and converts to integer type
organism = float(input('\n\nEnter the starting number of organisms: '))

#Requests user to enter amount of growth and converts to integer type
growth = int(input('Enter an average daily increase(percent of growth): '))

#Request user to enter amount of days to view the growth and converts to integer type
days = int(input('Enter the number of days organisms left to multiply: '))

#Print statements from line 17 to 22 which declares user inputted data and formats it to view somewhat like a chart without lines
print('\n\nStarting number of organisms: ',organism)
print('Average daily increase (percent): ',growth)
print('Number of days to multipy: ', days)
print()
print('Day Approximate\t\tPopulation')

#Reassigns new growth value that has been converted to a float and divided by 100
growth = growth/100

#For loop which iterates through the userinputted days to find out the value of growth per day
for i in range(days):
    #rounds organism value to contain certain # of decimals and renames variable
    population = round(organism, 5)
    #Formula where the growth of the organism is calculated and convrted to float
    grown_pop = float((organism * growth)+ organism)
    #Raises the iteratitive value in the range by 1 to accurately count from day 1 onward
    i += 1
    #Value of calculated growth is assigned to organism to be used in the next iteration
    organism = grown_pop

    #Prints the iterative value of the current loop next to the calculated growth 
    print(i,'\t\t\t', population)


