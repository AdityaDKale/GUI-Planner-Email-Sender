from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime


today = datetime.today()
t = today.strftime("%d %b")

tasks = Tk()


class Task:

    def __init__(self, title, description, date, time, priority, type, order):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.priority = priority
        self.type = type
        self.order = order

    def task(title, description, date, time, priority, type, order):
        if(type == 0):
            cb = Checkbutton(tasks, text=title, font=("Inter", 15), image=offImg, compound='left', padx=20,
                             selectimage=onImg, indicatoron=False, background="#313131", activebackground="#313131", selectcolor="#313131", foreground="#d1d1d1", activeforeground="#d1d1d1", border=0)
            cb.place(relx=0.1, rely=0.2+(0.23*(order-1)))
            time = Label(text=time, font=("Inter", 10),
                         background="#313131", foreground="#d1d1d1")
            time.place(relx=0.34, rely=0.27)
            if(priority == 1):
                pri = Label(image=priority1img, background="#313131")
                pri.place(relx=0.45, rely=0.273)
            elif(priority == 2):
                pri = Label(image=priority2img, background="#313131")
                pri.place(relx=0.45, rely=0.273)
            elif(priority == 3):
                pri = Label(image=priority3img, background="#313131")
                pri.place(relx=0.45, rely=0.273)
            elif(priority == 4):
                pri = Label(image=priority4img, background="#313131")
                pri.place(relx=0.45, rely=0.273)

            des = Label(text=description, font=("Inter", 10),
                        background="#313131", foreground="#d1d1d1")
            des.place(relx=0.34, rely=0.3)

        else:
            canvas = Canvas(tasks, width=60, height=100,
                            background="#313131", highlightthickness=0)
            canvas.place(relx=0.153, rely=0.07+(0.23*(order-1)))
            canvas.create_line(30, 0, 30, 100, fill="#d1d1d1", width=2)
            cb = Checkbutton(tasks, text=title, font=("Inter", 15), image=offImg, compound='left', padx=20,
                             selectimage=onImg, indicatoron=False, background="#313131", activebackground="#313131", selectcolor="#313131", foreground="#d1d1d1", activeforeground="#d1d1d1", border=0)
            cb.place(relx=0.1, rely=0.2+(0.23*(order-1)))
            time = Label(text=time, font=("Inter", 10),
                         background="#313131", foreground="#d1d1d1")
            time.place(relx=0.34, rely=0.043+(0.227*(order)))
            if(priority == 1):
                pri = Label(image=priority1img, background="#313131")
                pri.place(relx=0.45, rely=0.046+(0.227*(order)))
            elif(priority == 2):
                pri = Label(image=priority2img, background="#313131")
                pri.place(relx=0.45, rely=0.046+(0.227*(order)))
            elif(priority == 3):
                pri = Label(image=priority3img, background="#313131")
                pri.place(relx=0.45, rely=0.046+(0.227*(order)))
            elif(priority == 4):
                pri = Label(image=priority4img, background="#313131")
                pri.place(relx=0.45, rely=0.046+(0.227*(order)))

            des = Label(text=description, font=("Inter", 10),
                        background="#313131", foreground="#d1d1d1")
            des.place(relx=0.34, rely=0.073+(0.227*(order)))


onImg = PhotoImage(file='images//OnButton.png', master=tasks)
offImg = PhotoImage(file='images//OffButton.png', master=tasks)
offImg1 = PhotoImage(file='images//OffButton1.png', master=tasks)
onImg1 = PhotoImage(file='images//OnButton1.png', master=tasks)
priority1img = PhotoImage(file='images//Priority1.png', master=tasks)
priority2img = PhotoImage(file='images//Priority2.png', master=tasks)
priority3img = PhotoImage(file='images//Priority3.png', master=tasks)
priority4img = PhotoImage(file='images//Priority4.png', master=tasks)

tasks.geometry("418x664")
tasks.title("Tasks")
tasks.configure(background="#313131")
date = Label(text=t, font=("Inter", 20), background="#313131",
             foreground="#d1d1d1")
date.place(relx=0.1, rely=0.1)


Task.task("Spam", "I Am Spamming", 16, "20:00", 1, 0, 1)
Task.task("Hi", "Hey Everyone", 16, "21:00", 2, 1, 2)
Task.task("Hello", "Hello World", 16, "22:00", 4, 1, 3)


mainloop()
