from tkinter import *

from BookStoreBackend import Database

database = Database("bookstore.db")


class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Book Store")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.ISBN_text = StringVar()
        self.e4 = Entry(window, textvariable=self.ISBN_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb = Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6)
        self.list1.configure(yscrollcommand=sb.set)
        sb.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        btn1 = Button(window, text="View All", width=15, command=self.view_command)
        btn1.grid(row=2, column=3)

        btn2 = Button(window, text="Search Entry", width=15, command=self.search_command)
        btn2.grid(row=3, column=3)

        btn3 = Button(window, text="Add Entry", width=15, command=self.add_command)
        btn3.grid(row=4, column=3)

        btn4 = Button(window, text="Update", width=15, command=self.update_command)
        btn4.grid(row=5, column=3)

        btn5 = Button(window, text="Delete", width=15, command=self.delete_command)
        btn5.grid(row=6, column=3)

        btn6 = Button(window, text="Close", width=15, command=window.destroy)
        btn6.grid(row=7, column=3)

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.viewBook():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.searchBook(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                       self.ISBN_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insertBook(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END,
                          (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def delete_command(self):
        database.deleteBook(self.selected_tuple[0])

    def update_command(self):
        database.updateBook(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                            self.ISBN_text.get())


window = Tk()
Window(window)
window.mainloop()
