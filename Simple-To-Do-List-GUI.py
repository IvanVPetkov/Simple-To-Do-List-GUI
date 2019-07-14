# import all from tkinter
from tkinter import *

# create main window
window = Tk()
window.title('Simple-To-Do-List')
window.geometry('300x200')

# read the user input
user_input = StringVar()

# creates the entry box for the user input
entry_box = Entry(window, textvariable=user_input, width=25).place(x=75, y=25)

# creates a function which gets user's input and writes in on a file
def write_File():
    file = open("ToDoList-DB.txt",'a+')
    file.write(f'{user_input.get()} \n')
    file.close()

# this is a function which displays the user input
def return_user_input():
    result_Label.config(text=user_input.get())

# This in the main function of Add button which prints user's input and also calls other functions
def add_button():
    print(user_input.get())
    write_File()
    return_user_input()

# 'Add' button creation
add_button = Button(window, text="Add", width=5, height=1, bg="yellow", command=add_button).place(x=0, y=70)

# 'Quit' button creation
quit_button = Button(window, text="Quit", width=5, height=1, bg="red", command=window.quit).place(x=260, y=70)

# Creation of a label which returns the user input
result_Label = Label(window, text="")
result_Label.place(x=125, y=70)

window.mainloop()
