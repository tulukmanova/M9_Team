# Program description goes here
#this is a simple calculater program that can perform basic arithmetic operatipons like addition, subtraction, multiplication and division
# Updated on: 11-24-2024
# Updated by: Khateeja Khatoon, Takhmina Ulukmanova
# importing the tkinter module for creating the GUI
from tkinter import *
# creating the root window
root = Tk()
# setting the tittle of the window
root.title("Simple Calculator")
#creating an entry widget for displaying the input and output
#the entry idget is created with a width of 35, borderwidth of 5
# and is placed in row 0, column span3, padx 10,pady 10
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#the funtion takes a number as an argument 
# the current content of the entry widget is retrieved
#the current content is deleted and the new number is inserted
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
#defining the function for button clear events
#the function deletes the content of the entry widget
def button_clear():
    e.delete(0, END)
# defining the function for button operator events 
#the function retrieves the first number from the entry widget
#the first number is stored in a global variable f_num
#the operator is stored in a global variable num_operator
# the entry widget is cleared
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)
# defining the function for button equal events 
#the funtion retrieves the second number from the entry widget
# the second number is used to perform the arithmetic operation
# the result is inserted into entry widget 

# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
    else:
        e.insert(0, "Invalid!!!")


#Create buttons for digits 0-9 using the Button widget
#Use lambda functions to associate each button with the button_click() function, passing the corresponding digit as an argument.
#Create additional buttons for operators (+, -, *, /) using lambda to call button_operator() with the respective operator.

# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
#Add special buttons:
#= calls button_equal() to calculate the result.
#Clear calls button_clear() to reset the input.
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

#Arrange the buttons on the GUI in a grid:
#Place digit buttons (1-9) in rows 1-3 and button 0 in row 4.
#Arrange operator buttons (+, -, *, /) in rows 5-6.
#Place the = button and Clear button with specific columnspan for alignment.
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Start the GUI event loop with root.mainloop():
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Document what the following line of code do here
#Keeps the window open and responsive to user interaction.
root.mainloop()
