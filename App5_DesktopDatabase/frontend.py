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
import backend


# Must start a GUI-program with the following line
window = Tk()

window.wm_title('BookStore')

def get_selected_row(event):
    try:
        global selected_row
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass


# Functions that are invoked when the buttons are pressed
def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(tittel_text.get(), forfatter_text.get(), aar_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(tittel_text.get(), forfatter_text.get(), aar_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, tittel_text.get(), forfatter_text.get(), aar_text.get(), isbn_text.get())

def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0], tittel_text.get(), forfatter_text.get(), aar_text.get(), isbn_text.get())
    print(selected_row[0], selected_row[1], selected_row[2], selected_row[3], selected_row[4])

# Labels
l1 = Label(window, text="Tittel")
l1.grid(row=0, column=0)
l2 = Label(window, text="Forfatter")
l2.grid(row=0, column=2)
l3 = Label(window, text="Utgitt år")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


# Text entry fields
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

list1 = Listbox(window, height=15, width=50)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set) #(3,8)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)


# Buttons
b1 = Button(window, text="Se alle", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Søk entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="Legg til", width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Oppdater", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Slett", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(window, text="Lukk", width=12, command=window.destroy)
b6.grid(row=7, column=3)


# and must end the program with this line...
window.mainloop()
