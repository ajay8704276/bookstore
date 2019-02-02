from tkinter import *

from BookStoreBackend import Database

database = Database("bookstore.db")


def view_command():
    list1.delete(0, END)
    for row in database.viewBook():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.searchBook(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, row)


def add_command():
    database.insertBook(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    database.deleteBook(selected_tuple[0])


def update_command():
    database.updateBook(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(),
                                ISBN_text.get())


# initialize the windows for developing graphical interface
# for book store app
window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

btn1 = Button(window, text="View All", width=15, command=view_command)
btn1.grid(row=2, column=3)

btn2 = Button(window, text="Search Entry", width=15, command=search_command)
btn2.grid(row=3, column=3)

btn3 = Button(window, text="Add Entry", width=15, command=add_command)
btn3.grid(row=4, column=3)

btn4 = Button(window, text="Update", width=15, command=update_command)
btn4.grid(row=5, column=3)

btn5 = Button(window, text="Delete", width=15, command=delete_command)
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close", width=15, command=window.destroy)
btn6.grid(row=7, column=3)

window.mainloop()
