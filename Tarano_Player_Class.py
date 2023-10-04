#Author Name: Kristy Tarano
#Date: 3/27/2022
#Program Name: Basketball player class
#Purpose: The purpose of this program was to create a class that can store data regarding each basketball player in an object


#Declares the class Player which will define each attribute of the player
class Player:
    #Initializes the variables that will be needed to store information 
    def __init__(self, Name, Team, Position, Age, GamePoint, Mpg):
        self.__name = Name
        self.__team = Team
        self.__position = Position
        self.__age = Age
        self.__gamepoint = GamePoint
        self.__mpg = Mpg

    #Suppose to return the value stored in each method
    def __str__(self):
        return "Name: " + self.__name + \
          "\nTeam: " + self.__team + \
            "\nPosition: " + self.__position + \
            "\nAge: " + self.__age + \
            "\nGame Points: " + self.__gamepoint + \
            "\nMinutes Per Game: " + self.__mpg + '\n\n' 

    

#Declares the main function
def main():
    player1 = Player('Jaylen Adams', 'Mil', 'G', str(24.86), str(7), str(2.6))
    player2 = Player('Steven Adams', 'Nor', 'C', str(27.65), str(36), str(27.4))
    player3 = Player('Bam Adebayo', 'Mia', 'C-F', str(23.66), str(33), str(27.4))

    print(player1)
    print(player2)
    print(player3)
   

#Calls the main function
main()