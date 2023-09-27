#Author Name: Kristy Tarano
#Date: 04/24/2022
#Program Name: Fast Food Order 
#Purpose: The point of this program is to obtain order information from user and display it on the screen

#Import module that allows GUI interaction
from email import message
import tkinter
import tkinter.messagebox

#State Class
class myOrder:
    def __init__(self):

        #Creates main window
        self.main_window = tkinter.Tk()

        #Creates the two frames for checkbuttons and regular buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Creates the 7 objects to use with checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        #Sets all checkbuttons to zero
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        #Creates the frame for the input section
        self.input_frame = tkinter.Frame(self.main_window)
        
        #Create the Checkbutton widgets in the top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                        text='Hamburger',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                        text='Cheeseburger',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                        text='Bacon Cheeseburger',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                        text='Hot Dog',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                          text='Fries',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                        text='Shake',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                        text='Soda',
                                       variable=self.cb_var7)

       #Defines the input section of the frame 
        self.input_label = tkinter.Label(self.input_frame, 20, text="Special Instructions: ")
        self.input_entry = tkinter.Entry(self.input_frame, 22, width=10)
        
       
        # Pack the checkbuttons and the input labels
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.input_label.pack(side='left')
        self.input_entry.pack(side='left')
        
        #Creates the Order and Quit buttons
        self.order_button = tkinter.Button(self.bottom_frame, 
                                            text='Order',command=self.show_choice)
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                            text='Quit', 
                                            command=self.main_window.destroy)
        
        #Packs the butons
        self.order_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #Packs the frames
        self.input_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Starts the loop
        tkinter.mainloop(10)


    def show_choice(self):
        self.message = message
         # Determine which Checkbuttons are selected and builds the response message.
            #If checkbutton is selected, adds each option to the message
        if self.cb_var1.get() == 1:
            self.message = self.message + 'Hamburger\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + 'Cheeseburger\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + 'Bacon Cheeseburger\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Hot Dog\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Fries\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Shake\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + 'Soda\n'
        
        #Display the message in a dialog box.
        tkinter.messagebox.showinfo('You Ordered: ',self.message)
    
        



#Creates an instance of myOrder class
my_order = myOrder()
