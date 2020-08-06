from tkinter import *
from tkinter import filedialog

def file_explorer():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a folder/file",filetypes=(("Text files", "*.txt*"),  ("all files", "*.*")))
    l1.configure(text="File Opened: "+filename)

root = Tk()
root.title("File Explorer")
root.geometry("300x200")


l1 = Label(root, text="Opening the files")
l1.grid(column=1, rowspan=50)

b1=Button(root, text="Browse files", command = file_explorer)
b1.grid(column=1, rowspan=50)

b2=Button(root,text="Exit", command=exit)
b2.grid(column=1,rowspan=50)

root.mainloop()
