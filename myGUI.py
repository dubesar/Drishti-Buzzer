import tkinter as tk
from tkinter import *
class Timer:
    #defining the initial class
    def __init__(self, master):
        self.master = master
        self.master.title("GUIDrishti")
    
        self.state = False
        self.minutes=0
        self.seconds = 60

        self.last_line="0000"
        self.mins=0
        self.secs = 0
        self.listofq=["QUESTIONS WILL BE DISPLAYED HERE","What is the capital of India","What is your name","What is your pet's name","What is your city","What is the airline with air in it?"]
        self.t=0
        self.t1=0
        self.t2=0
        self.t3=0
        self.t4=0
        self.length=len(self.listofq)
        
        self.frame1=Frame(master,width=200,height=200,bg='#fbdbd0',relief=SUNKEN)
        self.frame1.grid(row=0,column=0)

        self.frame2=Frame(master,width=200,height=200,relief=SUNKEN)
        self.frame2.grid(row=0,column=1)

        self.frame3=Frame(master,width=200,height=200,relief=SUNKEN)
        self.frame3.grid(row=1,column=0)

        self.frame4=Frame(master,width=200,height=200,relief=SUNKEN)
        self.frame4.grid(row=1,column=1)
        
        self.display = Label(self.frame2, height=5, width=5, textvariable="",font="-weight bold")
        self.display.config(text="00:00")
        self.display.grid(row=0, columnspan=2)

        self.start_button = Button(self.frame2, bg="light green", activebackground="Dark Green", text="Start", width=8, height=2, command=self.start)
        self.start_button.grid(row=1, column=0)

        self.pause_button = Button(self.frame2, bg="#ff6347", activebackground="Dark Red", text="Pause", width=8, height=2, command=self.pause)
        self.pause_button.grid(row=1, column=1)

        self.order1=Label(self.frame4,text=self.last_line,bg="grey",fg="blue",font="-weight bold")
        self.order1.grid(row=0,column=0)

        self.teamnames1=Label(self.frame3,text="A")
        self.teamnames1.grid(row=0,column=0)

        self.teamnames2=Label(self.frame3,text="B")
        self.teamnames2.grid(row=0,column=1)

        self.teamnames3=Label(self.frame3,text="C")
        self.teamnames3.grid(row=0,column=2)

        self.teamnames4=Label(self.frame3,text="D")
        self.teamnames4.grid(row=0,column=3)

        self.labelintro=Label(self.frame1,text="WELCOME TO THE FLASH BUZZER ROUND",font="-weight bold",bg='#fbdbd0')
        self.labelintro.grid(row=0,column=0)

        #part1 updation of code of questions
        self.labelques=Label(self.frame1,text=self.listofq[self.t],width=40,font="-weight bold",bg='#fbdbd0')
        self.labelques.grid(row=2,column=0)
        self.nextb = Button(self.frame1, bg="Yellow", text="Next", width=6, height=2, command=self.ques)
        
        #part2 updation of scores of teams
        self.labelques1=Label(self.frame3,text=self.t1,width=20,font="-weight bold")
        self.labelques1.grid(row=1,column=0)
        self.nextb1 = Button(self.frame3, bg="Yellow", text="Correct", width=6, height=2, command=self.updatescore1)

        #part3 updation of scores of teams
        self.labelques2=Label(self.frame3,text=self.t2,width=20,font="-weight bold")
        self.labelques2.grid(row=1,column=1)
        self.nextb2 = Button(self.frame3, bg="Yellow", text="Correct", width=6, height=2, command=self.updatescore2)

        #part4 updation of scores of teams
        self.labelques3=Label(self.frame3,text=self.t3,width=20,font="-weight bold")
        self.labelques3.grid(row=1,column=2)
        self.nextb3 = Button(self.frame3, bg="Yellow", text="Correct", width=6, height=2, command=self.updatescore3)
       

        #part5 updation of scores of teams
        self.labelques4=Label(self.frame3,text=self.t4,width=20,font="-weight bold")
        self.labelques4.grid(row=1,column=3)
        self.nextb4 = Button(self.frame3, bg="Yellow", text="Correct", width=6, height=2, command=self.updatescore4)

        self.b=Button(self.frame3,text="Bind",width=80,bg="white")
        self.b.grid(columnspan=4)
        self.b.bind('<Right>', lambda e: self.ques())
        self.b.bind('<a>', lambda e: self.updatescore1())
        self.b.bind('<b>', lambda e: self.updatescore2())
        self.b.bind('<c>', lambda e: self.updatescore3())
        self.b.bind('<d>', lambda e: self.updatescore4())
        self.b.bind('<s>', lambda e: self.start())
        self.b.bind('<p>', lambda e: self.pause())
        self.b.bind('<t>', lambda e: self.buzzerdata())
        self.b.focus_set()
        self.b.place(x=100,y=100)

    def countdown(self):

        if self.state == True:

            if (self.mins == 0) and (self.secs == 0):
                self.display.config(text="Done!")
                self.state = False
            else:
                self.display.config(text="%02d:%02d" % (self.mins, self.secs))

                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)

    def start(self):
        if self.state == False:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds
            self.countdown()

    def pause(self):
        if self.state == True:
            self.state = False
            self.countdown()

    def ques(self):
        if self.t<self.length-1:
            self.t=self.t+1
            self.labelques.config(text=self.listofq[self.t])

    def updatescore1(self):
        if self.t1<10:
            self.t1=self.t1+1
            self.labelques1.config(text=self.t1)

    def updatescore2(self):
        if self.t2<10:
            self.t2=self.t2+1
            self.labelques2.config(text=self.t2)

    def updatescore3(self):
        if self.t3<10:
            self.t3=self.t3+1
            self.labelques3.config(text=self.t3)

    def updatescore4(self):
        if self.t4<10:
            self.t4=self.t4+1
            self.labelques4.config(text=self.t4)

    def buzzerdata(self):
        self.fh=open("buzzer.txt","r")
        self.last_line=self.fh.readlines()[-1]
        self.order1.config(text=self.last_line)
        self.fh.close()

root = Tk()
my_timer = Timer(root)
root.mainloop()
