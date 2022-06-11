#Part 1
from tkinter import *

# Create a GUI window
window = Tk()


# Function to convert weight
# given in kg to grams, pounds
# and ounces
def from_kg():
    # convert kg to gram
    gram = float(e2_value.get()) * 1000

    # convert kg to pound
    pound = float(e2_value.get()) * 2.20462

    # convert kg to ounce
    ounce = float(e2_value.get()) * 35.274

    # Enters the converted weight to
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)


# Create the Label widgets
e1 = Label(window, text="Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='Gram')
e4 = Label(window, text='Pounds')
e5 = Label(window, text='Ounce')

# Create the Text Widgets
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

# Create the Button Widget
b1 = Button(window, text="Convert", command=from_kg)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

# Start the GUI
window.mainloop()

#Part 2
from tkinter import *
import tkinter.font as font

#Function to Convert Celsius to Fahrenheit
def convert():
    temp_celsius = celsius_value.get()

    if(temp_celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        temp_fahrenheit = (float(temp_celsius) * 9/5) + 32
        output_fahrenheit.config(text = 'Temperature in Fahrenheit : ' + str(temp_fahrenheit))
    else:
        error_msg.grid(row=1, column=1)

my_window = Tk()
my_window.title("Celsius to Fahrenheit Converter")

#Displaying heading inside window
description = Label(text = 'Celsius -> Fahrenheit', font = font.Font(size = 20), fg = "grey")
description.pack()

frame = Frame(my_window)
frame.pack(pady = 20)

#entry box to enter temperature in celsius
message_one = Label(frame, text = 'Enter Temperature in Celsius : ', font = font.Font(size = 10))
message_one.grid(row = 0, column = 0)

celsius_value = Entry(frame)
celsius_value.grid(row = 0, column = 1)

#To Display Error Message
error_msg = Label(frame, text = 'Please enter valid input...', font = font.Font(size = 8), fg = 'red')

#To Display the Output
output_fahrenheit = Label(frame, font = font.Font(size = 12))
output_fahrenheit.grid(row = 2, column = 0, columnspan = 2, pady = 10)

#Submit Button
submit_btn = Button(frame, text = 'Convert', width = 30, fg = "black", bg = "light green", bd = 0, padx = 20, pady = 10, command = convert)
submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)

my_window.geometry('500x250')
my_window.mainloop()