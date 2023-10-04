#Author Name: Kristy Tarano
#Date: 2/20/2022
#Program Name: Personal Web Page Generator 
#Purpose: The purpose of this program is to create an HTML file with the input of the user.


#Defines the main function that will take the user input and input into html file
def main():

    #Defines the variable which will declare the new html file 
    webFile = open('UserDescription.html', 'w')

    #Takes the user input 
    name = input("Enter your name: ")

    #Takes the user input 
    description = input("Describe yourself: ")

    #Variable that contains the contents of what will be inputted into the file, as well as contains the input from the user
    webPage = '''<html> 
                <head> </head>
                    <body>
                    <center>
                 <h1>{}</h1>
                    </center>
                         <hr />{}<hr />
                         </body>
                         </html> '''.format(name, description)

    #The file is being filled with the contents of the variable WebPage
    webFile.write(webPage)
    print()

    #Closes the file once its done writing to it
    webFile.close()

#Calls the function 
main()