import tkinter
import tkinter.messagebox
from tkinter import *
root=Tk()
root.title("Simple TODO")
def edit_task():
    try:
        t = input_t.get()
        if t != "":
            index_del = list_task.curselection()[0]
            list_task.delete(index_del)
            list_task.insert(index_del, t)
            input_t.delete(0, index_del)
    except:
        tkinter.messagebox.showerror("Error", "Select task or Task input is null")

def delete_task():
    try:
        index = list_task.curselection()[0]
        list_task.delete(index)
    except:
        tkinter.messagebox.showerror("Error", "Select task")
def add_task():
    t=input_t.get()
    if t != "":
        list_task.insert(tkinter.END, t)
        input_t.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showerror("Error", "Task input is null")
list_task=tkinter.Listbox(root, height=3, width=50)
list_task.pack()
input_t=tkinter.Entry(root, width=50)
input_t.pack()
button_add=Button(root, text="Add label", width=50, command=add_task)
button_add.pack()
button_del=Button(root, text="Del label", width=50, command=delete_task)
button_del.pack()
button_edit=Button(root, text="Edit label", width=50, command=edit_task)
button_edit.pack()
root.mainloop()