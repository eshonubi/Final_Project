"""
First, the code imports the tkinter module and the messagebox module.
The tkinter module is used to create the GUI for the pizza ordering
app, while the messagebox module is used to display message boxes in
the app.
"""

#Importing necessary modules
from tkinter import *
from tkinter import messagebox

"""
The code then creates a new window for the app using the Tk() method.
The window is set to a fixed size using the geometry() method. The title
of the window is set to "My pizza ordering app" using the title() method.
"""

#Creating the main window
pizza = Tk()
pizza.geometry("600x500")
pizza.title("My pizza ordering app")

"""
Next, the code creates three labels for the user to enter their name,
address, and phone number. Each label is then placed on the window using
the grid() method. The code also creates three entry fields for the user
to input their name, address, and phone number. Each entrey field is placed
on the window using the grid() method. 
"""

#Creating labels and entry fields for user input
name_Label = Label(pizza, text="What is your name? ")
name_Label.grid(row=0, column=0)
name_entry = Entry(pizza, width=30)
name_entry.grid(row=0, column=1)


address_Label = Label(pizza, text="What is your address? ")
address_Label.grid(row=1, column=0)
address_entry = Entry(pizza, width=30)
address_entry.grid(row=1, column=1)


phone_Label = Label(pizza, text="What is your phone number? ")
phone_Label.grid(row=2, column=0)
phone_entry = Entry(pizza, width=30)
phone_entry.grid(row=2, column=1)

"""
The code then creates a list of pizza toppings called my_pizza_list
and a listbox called pizza_list. The listbox allows the user to select
multiple pizza toppings from my_pizza_list. The code then loops through
each item in my_pizza_list and inserts each item into pizza_list using
the insert() method. A background color and foreground color is also used.
The listbox is then placed on the window using the grid() method.
"""

#Creating a listbox for pizza selection, bg and fg color, and position
my_pizza_list = ["Pepperoni", "Onions", "Mushrooms", "Sausage", "Bacon"]
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="blue")
pizza_list.grid(row=4, column=1)
for item in my_pizza_list:
    pizza_list.insert(0, item)

"""
The code then defines a function called add_pizza() that is called
when the user clicks a button to add their pizza selection. The function
loops through each item that the user has selected in pizza_list and adds
each item to a string called result. The function then sets the text of a
label called add_lbl to display the user's pizza selection using the config()
method. 
"""
#defines the add_pizza button and sets the add_lbl to display pizza selection
def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"
        add_lbl.config(text="Your Pizza Selection: " + "\n" + result)

add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

"""
The program creates a "Add pizza" button that allows user to add the
selected pizza toppings to their order. When the button is clicked,
the code calls the add_pizza() function. The button is placed on the
window using the grid() function.
"""
#Creating an add pizza button
add_button = Button(pizza, text="Add pizza", command= add_pizza)
add_button.grid(row=5, column=0)

#confirms and checkout order information on the screen. This is placed on the window using the grid() function
def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Your order has been confirmed \n \n Name: " + text1)
    new_lbl.grid(row=5, column=2)
    
    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address: " + text2)
    new_lbl2.grid(row=6, column=2)
    
    text3= phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone Number: " + text3)
    new_lbl3.grid(row=7, column=2)

"""
The code then creates a checkout button that allows the user to checkout
and submit their order. When the button is clicked, the code calls the
checkout() function. The button is placed on the window using the grid()
function.
"""
#Creating a checkout button   
check_button = Button(pizza, text="Checkout", command=check)
check_button.grid(row=6, column=0)

"""
The program the defines a deleteme function and creates a delete
button that allows the user to remove a selected pizza or lists
of selected pizza toppings from their order. When the button is clicked,
the code calls the deleteme function. The button is placed on the window
using the grid() function.
"""
#defining the deleteme function and creating a delete button
def deleteme():
    pizza_list.delete(0,5)
del_button = Button(pizza, text="Delete Pizza", command=deleteme)
del_button.grid(row=7, column=0)

"""
Then the code creates a dropdown button using the "OptionMenu" widget
from the tkinter module. The OptionMenu widget creates a drop down menu that
allows the user to select from a list of options. The list of options is the
drinks list. When the user selects an option from the dropdown menu, the drink
variable is set to the selected value. The button is placed on the window
using the grid() function.
"""
#creating a dropdown button for drinks
drinks = StringVar()
drinks.set("Choose a drink")
drink = OptionMenu(pizza, drinks, "Cocacola", "Lemonade", "Fanta", "Sprite")
drink.grid(row=8,column=0)

"""
The exit_me() function is called when the user clicks the exit button.
It opens a new window that displays a message asking the user if they
really want to exit the program. If the user clicks "yes", the program is
closed. If the user clicks "No", the message is closed and the program
continues. 
"""
#Creates another window that displays a yes or no message
def exitme():
    answer = messagebox.askyesno("Hi", "Are you sure you want to exit? ")
    if answer == 1:
        pizza.destroy()
    else:
        return
    
#creates the exitme button and is placed on the window using the grid() function.
exit_button = Button(pizza, text="Exit Me", command=exitme)
exit_button.grid(row=4, column=7)


pizza.mainloop()


