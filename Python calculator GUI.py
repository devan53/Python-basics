from tkinter import *

expression = ""
def press(char):
    global expression
    expression = expression + str(char)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
        
    except:
        total = "Error"
        equation.set(total)
        expression = ""

def clrscr():
    global expression
    expression = ""
    equation.set(expression)


if __name__=="__main__":
    root = Tk()
    root.title("Simple Calculator")
    root.geometry("300x150")
    equation = StringVar()
    equation.set("Enter your expression")
    lab1 = Entry(root,textvariable=equation)
    lab1.pack(fill = 'x')
    
    #result.pack(fill ='y', ipadx=10)
    button1 = Button(root,text='1',command=lambda:press(1),height=1, width=4)
    button1.grid(row=1,column=0)
    button2 = Button(root,text='2',command=lambda:press(2),height=1, width=4)
    button2.grid(row=1,column=1)
    button3 = Button(root,text='3',command=lambda:press(3),height=1, width=4)
    button3.grid(row=1,column=2)
    button4 = Button(root,text='4',command=lambda:press(4),height=1, width=4)
    button4.grid(row=1,column=3)
    result = Button(root,text='=',command=equalpress,height=6, width=4)
    result.grid(row=1,column=4)
    button5 = Button(root,text='5',command=lambda:press(5),height=1, width=4)
    button5.grid(row=3,column=0)
    button6 = Button(root,text='6',command=lambda:press(6),height=1, width=4)
    button6.grid(row=3,column=1)
    button7 = Button(root,text='7',command=lambda:press(7),height=1, width=4)
    button7.grid(row=3,column=2)
    button8 = Button(root,text='8',command=lambda:press(8),height=1, width=4)
    button8.grid(row=3,column=3)
    button9 = Button(root,text='9',command=lambda:press(9),height=1, width=4)
    button9.grid(row=4,column=0)
    button10 = Button(root,text='0',command=lambda:press(0),height=1, width=4)
    button10.grid(row=4,column=1)
    button11 = Button(root,text='.',command=lambda:press('.'),height=1, width=4)
    button11.grid(row=4,column=2)
    clear = Button(root,text='Clear',command=clrscr,height=1, width=4)
    clear.grid(row=4,column=3)
    plus = Button(root,text='+',command=lambda:press(text),height=1, width=4)
    plus.grid(row=5,column=0)
    minus = Button(root,text='-',command=lambda:press('-'),height=1, width=4)
    minus.grid(row=5,column=1)
    multiply = Button(root,text='*',command=lambda:press('*'),height=1, width=4)
    multiply.grid(row=5,column=2)
    div = Button(root,text='/',command=lambda:press('/'),height=1, width=4)
    div.grid(row=5,column=3)
    

    root.mainloop()
