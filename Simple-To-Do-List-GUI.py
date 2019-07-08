import tkinter as tk                # Import tk

def writeFile():
    file = open("ToDoList-DB.txt",'a+')
    user_Input = el.get()
    file.write(user_Input)
    file.close()

def show_entry_fields():
    print(e1.get())
    writeFile()

window = tk.Tk()                    # Create instance
window.title("Simple TO-DO list")      # Add a title
window.geometry("600x400")

tk.Label(window).grid(row=0)
e1 = tk.Entry(window, width=30)
e1.grid(row=0, column=0)

tk.Button(window,
          text='Add', bg="yellow",
          command=show_entry_fields).grid(row=10,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(window,
          text='Quit', bg="red", command=window.quit).grid(row=10,
                                                       column=10,
                                                       sticky=tk.W,
                                                       pady=4)

window.mainloop()
