from ast import In
from hashlib import new
from re import M


carName = input('\nName of Car: \n')
carMSRP = float(input('MSRP of Car: \n'))
carInterest = (float(input('Enter interest rate: \n')))/100.00
downPayment = float(input('Down payment?: \n'))
monTerm = int(input('How many months financed?: \n'))
principal = carMSRP - downPayment
monthlyNet = float(principal/(monTerm))

monInterest = (carInterest/12.0)*(carMSRP - downPayment)
monPayment = format(monInterest + monthlyNet, '.2f')



print(f'\nYour monthly payment estimate for {carName} is ${monPayment}\n')
newBalance = (input('\nDo you want to see your principal increase with interest added? ')).lower()
if newBalance == 'y':
    for m in range(monTerm):
        newPrincipal = principal + monInterest
        newInterest = (carInterest/12.0)* newPrincipal
        principal = newPrincipal
        monInterest = newInterest
        m += 1
        print(f'Month {m} $', format(principal,'.2f'))
elif newBalance == 'n':
        quit
    