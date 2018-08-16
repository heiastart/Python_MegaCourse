'''
A program that stores the following book information;
Title, author
Year, ISBN

The user can (with buttons/widgets);
- View all records
- Search an entry
- Add entry
- Update entry
- Delete entry
- Close the program/window
'''

from tkinter import *

# Must start a GUI-program with the following line
window = Tk()

l1 = Label(window, text="Tittel")
l1.grid(row=0, column=0)
l2 = Label(window, text="Forfatter")
l2.grid(row=0, column=2)
l3 = Label(window, text="Utgitt år")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

tittel_text = StringVar()
e1 = Entry(window, textvariable=tittel_text)
e1.grid(row=0, column=1)

forfatter_text = StringVar()
e2 = Entry(window, textvariable=forfatter_text)
e2.grid(row=0, column=3)

aar_text = StringVar()
e3 = Entry(window, textvariable=aar_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=15, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# and must end the program with this line...
window.mainloop()
