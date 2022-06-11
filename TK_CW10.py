from tkinter import *
from tkinter.ttk import *

mainWin=Tk()
mainWin.title('Address Book')

#design mainwindow

#Label address book name
bookName = Label(mainWin, text='My Address Book',width=35)
bookName.grid(row = 0, column = 1,pady = 10,columnspan=3)

#Open address book 
open_button = Button(mainWin, text='Open')
open_button.grid(row = 0, column = 3,pady = 10)

# Contact list
book_list =Listbox(mainWin,height=15,width=30)
book_list.grid(row = 2, column = 0,columnspan=3, rowspan = 5 )



### Text fields to display contact information ###
# name
name_label =Label(mainWin, text = 'Name:')
name_label.grid(row= 2, column = 3)
name =Entry(mainWin)
name.grid(row = 2, column = 4,padx=5)

# Address 
address_label =Label(mainWin, text = 'Address :')
address_label.grid(row = 3, column = 3)
address =Entry(mainWin)
address.grid(row = 3, column = 4,padx=5)

# Mobile phone
mobile_label =Label(mainWin, text = 'Mobile:')
mobile_label.grid(row = 4, column = 3)
mobile =Entry(mainWin)
mobile.grid(row = 4, column = 4,padx=5)

# Email
email_label = Label(mainWin, text = 'Email:')
email_label.grid(row = 5, column = 3)
email =Entry(mainWin)
email.grid(row = 5, column = 4,padx=5)

# Birthday
birthday_label = Label(mainWin, text = 'Birthday:')
birthday_label.grid(row = 6, column = 3)
birthday = Entry(mainWin)
birthday.grid(row =6, column = 4,padx=5)

#buttons

# Edit contact button
Edit_button = Button(mainWin, text = 'Edit',width=10)
Edit_button.grid(row = 7, column = 0, padx = 12,pady=12) 

# Delete contact button
delete_button =Button(mainWin, text = 'Delete',width=10)
delete_button.grid(row = 7, column = 1,pady=12 )

# Update/Add  contact button
add_button =Button(mainWin, text = 'Update/Add')
add_button.grid(row = 7, column = 4,pady=12)

#save address book button
save_button = Button(mainWin, text='Save',width=35)
save_button.grid(row = 8, column = 1,pady = 10,columnspan=3)

mainWin.mainloop()
