# M9_Team
begin simple calculator 
import tkinter
creat root window
set title of root to "simple calcualtor"
creayte entry widget e wit width 35 and border width 5
place e in grid at row 0, coloumn 0, spanning 3 columns, with padding
funtion button_click(number):
set current to content of e
clear e 
insert current+number into e
end function
funtion button_clear();
clear e 
end function
funtion button_operator(operator):
set first_number to content of e
set global f_num to integer value of first_number
set global num_operator to operator 
clear e
end function 
funtion button_equal():
set second_number to content of e
clear e
if num_operator is "+' then 
insert f_num +second_number into e
else if num_operator is "*" then 
insert f_num * second_number into e
else if num_operator is"/" then 
insert f-num/ second_number into e
else if num_operator is "_" then 
insert f_num - seocnd number into e
else insert :invalid!!!" into e
end if 
end function
Set up the GUI.
Make and set up every button.
Put the buttons in a grid pattern.
To listen for button clicks and respond appropriately, start the event loop.
Button_click, button_operator, button_equal, and button_clear are the functions that are called when a button is clicked.
Continue until the program is closed by the user.
