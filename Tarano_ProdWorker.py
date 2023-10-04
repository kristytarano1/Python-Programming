#Author Name: Kristy Tarano
#Date: 4/03/2022
#Program Name: Employee and Production Worker program
#Purpose: The purpose of this program is to obtain employee information and return it using classes


#Declares the class Employee and its attributes
class Employee:
    #Initializes the variables that will be needed to store information 
    def __init__(self, Name, EmployeeNum):
        self.__name = Name
        self.__employeenum = EmployeeNum
    
    #Mutator for the Name attribute
    def set_name(self, Name):
        self.__name = Name

    #Mutator for the Employee Number attribute
    def set_employeenum(self, EmployeeNum):
        self.__employeenum = EmployeeNum
    
    #Accessor for the Name attribute
    def get_name(self):
       return self.__name 

    #Accessor for the Employee attribute
    def get_employeenum(self):
       return self.__employeenum 

#Declares the subclass Production worker class and its attributes    
class ProductionWorker(Employee):
    #Initializes the variables that will be needed to store information and calls on variables from Employee Class
    def __init__(self, Name, EmployeeNum, ShiftNum, PayRate):
        Employee.__init__(self, Name, EmployeeNum)
        self.__shiftnum = ShiftNum
        self.__payrate = PayRate

    #Mutator for the shift number attribute
    def set_shiftnum(self, ShiftNum):
        self.__shiftnum = ShiftNum

    #Mutator for the pay rate attribute
    def set_payrate(self, PayRate):
        self.__payrate = PayRate
    
    #Accessor for the shift number attribute
    def get_shiftnum(self):
       return self.__shiftnum 

    #Accessor for the pay rate attribute
    def get_payrate(self):
       return self.__payrate


    
#Function to obtain employee information
def main():
    #Retrieves values from user input and stores into variables
    name = input('Name: ')
    employeeNum = input('Employee Number: ')
    shiftNum = input('Shift Number: ')
    payRate = input('Pay Rate: ')

    #Variables are then passed along to Production Worker Class and assigned to the object production_worker1
    production_worker1 = ProductionWorker(name, employeeNum, shiftNum, payRate)

    #Prints employee information obtain from above by calling on the object created and using the classes accessor methods
    print('\n\nEmployee Information')
    print('---------------------')
    print('\nEmployee Name:', production_worker1.get_name())
    print('Employee Number: ', production_worker1.get_employeenum())
    print('Employee Shift: ', production_worker1.get_shiftnum())
    print('Employee Pay Rate: ', production_worker1.get_payrate())


#Calls the main function
main()

