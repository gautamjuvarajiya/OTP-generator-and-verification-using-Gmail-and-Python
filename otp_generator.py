import os
import math
import random
import smtplib
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('OTP generator')
ws.geometry('350x200')

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP+ " is your Python Project Verification Code"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "Your app password")


def sendingg():
    strr=str(a.get())
    s.sendmail('&&&&&&&&&&&',strr,msg)

def same():
    st=str(b.get())
    if st=='':
        return messagebox.showinfo('message','Hi! Please Enter OTP')
    elif st==OTP:
        return messagebox.showinfo('message','Hi! Your Entered OTP is Matched')
    else:
        return messagebox.showinfo('message','Hi! Your Entered OTP is Not Matched')


Label(ws, text="Enter Email :").pack()
a=StringVar()
enteredmail = Entry(ws,textvariable=a)
enteredmail.pack()
Button(ws, text="CONFIRM EMAIL", command=sendingg).pack()

Label(ws, text="Enter OTP").pack()
b=StringVar()
enteredotp = Entry(ws,textvariable=b, show="*")
enteredotp.pack()
Button(ws, text="VERIFY OTP", command=same).pack()

ws.mainloop()

