from tkinter import *
import smtplib

# main screen
master = Tk()
master.title('Email App')
master.geometry('400x425')


# functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username == " " or password == "" or to == "" or subject == "" or body == "":
            notif.configure(fg='red')
            notif["text"] = "All fields requires"
            return
        else:
            finalMessage = 'Subject:{}\n\n{}'.format(subject, body)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, finalMessage)
            notif.config(text='Email has been sent', fg='green')
    except:
        notif.config(text='Error sending email', fg="red")


def reset():
    usernaemEntry.delete(0, 'end')
    passwordeEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    bodyEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')


# for graphics
Label(master, text=" Custom Email App", font=(' Calibri', 20)).grid(row=0, padx=60, pady=10)
Label(master, text=" Use the form below to send email", font=('Calibri', 11)).grid(row=1, sticky=W, padx=5, pady=10)
Label(master, text="Email", font=('caliberi', 13)).grid(row=2, sticky=W, padx=5, pady=5)
Label(master, text="Password", font=('caliberi', 13)).grid(row=3, sticky=W, padx=5, pady=5)
Label(master, text="To", font=('caliberi', 13)).grid(row=4, sticky=W, padx=5, pady=5)
Label(master, text="Subject", font=('caliberi', 13)).grid(row=5, sticky=W, padx=5, pady=5)
Label(master, text="Body", font=('caliberi', 13)).grid(row=6, sticky=W, padx=5, pady=5)
notif = Label(master, text="", font=('Calibri', 13))
notif.grid(row=7, sticky=S, padx=5)

# Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# entries
usernaemEntry = Entry(master, textvariable=temp_username, width=30)
usernaemEntry.grid(row=2, column=0, )
passwordeEntry = Entry(master, textvariable=temp_password, width=30, show='*')
passwordeEntry.grid(row=3, column=0, padx=30, sticky=S)
receiverEntry = Entry(master, textvariable=temp_receiver, width=30)
receiverEntry.grid(row=4, column=0)
subjectEntry = Entry(master, textvariable=temp_subject, width=30)
subjectEntry.grid(row=5, column=0)
bodyEntry = Entry(master, textvariable=temp_body, width=30)
bodyEntry.grid(row=6, column=0)

# button
Button(master, text="send", command=send, font=('caliberi', 13)).grid(row=7, sticky=W, pady=15, padx=40)
Button(master, text="Reset", command=reset, font=('caliberi', 13)).grid(row=7, sticky=W, pady=45, padx=140)
master.mainloop()
