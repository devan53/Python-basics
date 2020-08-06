from tkinter import *
import time

count = 0
class Countdown():
        def timefetch(self):
                global count
                if count==0:
                        v1 = self.e.get()
                else: v1 = count
                
                try:
                        v1 = int(v1)
                        if v1 > 0:
                                count = (v1-1)
                                if count>0:
                                        hour =  int((count)/3600) 
                                        minu =  int(((count)-hour*3600)/60)
                                        sec = int(((count)-hour*3600)%60)
                                        time_left =str(hour).zfill(2)+":"+str(minu).zfill(2)+":"+str(sec).zfill(2)
                                        self.t.set(time_left)
                                        self.root.after(970,self.timefetch)
                                else: self.t.set("00:00:00 - Time's Up!")
                                        
                                
                        else:
                                self.t.set("Enter a valid time. It can't be -ve time")
                                                                       
                except ValueError:
                                self.t.set("Not a valid time. Please enter a valid time")
                 
        


        def __init__(self):
                self.root = Tk()
                self.root.title("Countdown Timer")
                self.root.geometry("300x160")
                self.root.resizable(False, True)
                self.l = Label(self.root,text="Please enter countdown time in sec")
                self.l.config(font = ("Courier 10 bold"))
                self.l.pack(side = TOP)
                self.e = Entry(self.root, bd = 10)
                self.e.pack(side = TOP)
                self.b = Button(self.root,text="Start Countdown",command=self.timefetch) ##font=("Aerial 40 bold"))
                self.b.pack(side = TOP)
                self.t = StringVar()
                self.t.set("Wait..")
                self.l1 = Label(self.root, textvariable=self.t, wraplength=350, justify=CENTER)
                self.l1.config(font = ("Courier 15 bold"))
                self.l1.pack(side = TOP)
                self.b1 = Button(self.root,text="Quit", command=self.root.destroy)
                self.b1.pack(side = BOTTOM)


a = Countdown()
