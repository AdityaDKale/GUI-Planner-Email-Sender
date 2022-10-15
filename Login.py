from tkinter import *

login = Tk()

# Giving Dimensions and background image
login.geometry("1280x720")
login.title("Planner")
img = PhotoImage(file='images//login.png', master=login)
img_label = Label(login, image=img)
img_label.place(x=0, y=0)

# Placing Submit Button
submitButton = PhotoImage(file="images//submitButton.png")
submit = Button(image=submitButton, border=0,
                background="#d1d1d1", activebackground="#d1d1d1")
submit.place(x=1114, y=449)

# Placing forgotPassword Button
forgotPasswordButton = PhotoImage(file="images//forgotPassword.png")
forgotPassword = Button(image=forgotPasswordButton, border=0,
                        background="#d1d1d1", activebackground="#d1d1d1")
forgotPassword.place(x=1111, y=508)

# Placing register Button
registerButton = PhotoImage(file="images//register.png")
register = Button(image=registerButton, border=0,
                  background="#d1d1d1", activebackground="#d1d1d1")
register.place(x=821, y=671)

# Placing Text Entry of Username
userName = Entry(background="#d1d1d1", border=0, width=40, font=("Inter", 15))
userName.place(x=764, y=290, height=43)

# Placing Text Entry of Password
password = Entry(background="#d1d1d1", border=0,
                 width=40, show="*", font=("Inter", 15))
password.place(x=764, y=363, height=43)

mainloop()
