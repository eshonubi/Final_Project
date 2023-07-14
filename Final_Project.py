from tkinter import *

pizza = Tk()
pizza.geometry("600x500")
pizza.title("My pizza ordering app")


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


my_pizza_list = ["Pepperoni", "Cheese", "Mushroom", "Steak", "Olives"]


pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="black", fg="red")
pizza_list.grid(row=4, column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)



def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text="Your Pizza Selection: " + "\n" + result)


add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

add_button = Button(pizza, text="Add pizza", command= add_pizza)
add_button.grid(row=5, column=0)


def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address: " + text2)
    new_lbl2.grid(row=6, column=2)

    text3= phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone Number: " + text3)
    new_lbl3.grid(row=7, column=2)
    
check_button = Button(pizza, text="Checkout", command=check)
check_button.grid(row=6, column=0)

def deleteme():
    pizza_list.delete(0,5)

del_button = Button(pizza, text="Delete Pizza", command=deleteme)
del_button.grid(row=7, column=0)


drinks = StringVar()
drinks.set("Choose a drink")

drink = OptionMenu(pizza, drinks, "Cola", "Beer", "Fanta", "Sprite")
drink.grid(row=8, column=0)

