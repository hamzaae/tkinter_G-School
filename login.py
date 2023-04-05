import smtplib
import ssl
import tkinter
import tkinter as tk
from email.message import EmailMessage
from tkinter import messagebox
import traceback
import webbrowser
import cv2
from PIL import Image, ImageTk
import face_login
import mysql.connector
import hashlib
import random
import string
import home


class Login:
    current_user = {}
    def __init__(self):
        # Create the window
        self.root = tk.Tk()
        self.root.title('G-School LOGIN')
        self.root.geometry('700x402')
        self.root.resizable(False, False)
        # Add image and frame
        self.bg = tk.PhotoImage(file="media\\slide.png")
        self.img = tk.Label(self.root, image=self.bg)
        self.img.place(x=-360, y=0)
        self.frame = tk.Frame(self.root, width=340, height=405, bg='white')
        self.frame.place(x=360)
        # Show logo and heading
        self.head = tk.Label(self.frame, text='ENSAH G-SCHOOL LOGIN'
                             , font=("Helvetica", 16, 'bold'), bg='white')
        self.head.place(x=68, y=45)
        self.logo = tk.PhotoImage(file="media\\logo-ensah_50x50.png")
        self.img_logo = tk.Label(self.frame, image=self.logo, bg='white')
        self.img_logo.place(x=8, y=30)
        # Add inputs and lign decorator and validating commands
        # 1-user
        self.vcmd = (self.root.register(self.validate_input), '%P')
        self.user = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white',
                        font=('Microsoft YaHei UI Light', 18, 'bold'),
                        validate="key", validatecommand=self.vcmd)
        self.user.place(x=30, y=130)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        # 2-password
        self.pswrd = tk.Entry(self.frame, width=25, fg='black',
                        border=0, bg='white', validate="key",
                        validatecommand=self.vcmd,
                        font=('Microsoft YaHei UI Light', 18, 'bold'), show='*')
        self.pswrd.place(x=30, y=200)
        self.pswrd.insert(0, 'Password')
        self.pswrd.bind('<FocusIn>', self.on_enter_password)
        self.pswrd.bind('<FocusOut>', self.on_leave_password)
        self.forgot_pswrd = tk.Button(self.frame,text="Forgot password?",bd=0, fg='black', bg='white',
                        font=('Microsoft YaHei UI Light', 9), command=self.forgot_password)
        self.forgot_pswrd.place(x=210, y=240)

        # 3-decorators
        self.fr1 = tk.Frame(self.frame, width=295, height=2, bg='black')
        self.fr1.place(x=25, y=167)
        self.fr2 = tk.Frame(self.frame, width=295, height=2, bg='black')
        self.fr2.place(x=25, y=237)
        # 4-show and hide password
        self.checkBox_showPassword = tkinter.Button(self.frame, text="👁", bg='white',
                        borderwidth=0, font=('verdana', 14), command=self.show_and_hide)
        self.checkBox_showPassword.place(x=280, y=195)
        # add signin and face_signin buttons
        self.signin_btn = tk.Button(self.frame, width=39, pady=7, text='Sign in',
                        bg='#6cc570', fg='white', border=0,
                        command=self.on_signin)
        self.signin_btn.place(x=35, y=270)
        self.signin_face_btn = tk.Button(self.frame, width=39, pady=7,
                        text='Face Sign in', bg='#5271ff', fg='white', border=0,
                        command=self.on_face_signin)
        self.signin_face_btn.place(x=35, y=315)
        # camera
        self.camera_label = tkinter.Label(self.root)
        self.camera_label.place(x=0)
        # about
        self.abt_lbl = tk.Label(self.frame, text="Visit our site to know more About! ",
                        fg='black', bg='white',
                        font=('Microsoft YaHei UI Light', 11))
        self.abt_lbl.place(x=65, y=350)
        # Create a Label to display the link
        self.link = tk.Label(self.frame, text="https://ensah.ma/",
                        font=('Helveticabold', 10), fg="blue", bg="white",cursor="hand2")
        self.link.place(x=120, y=375)
        self.link.bind("<Button-1>", lambda e: self.callback("https://ensah.ma/"))
        # DB connection
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="g_school"
        )
        self.mycursor = self.mydb.cursor()
        # Other
        self.email_sender = 'tkinter.gschool@gmail.com'
        self.email_password = 'vizjfzoeihmxchqu'

    def start(self):
        self.root.mainloop()

    def on_enter_user(self, e):
        if self.user.get() == "Username":
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        name = self.user.get()
        if name == "":
            self.user.insert(0, 'Username')

    def on_enter_password(self, e):
        if self.pswrd.get() == "Password":
            self.pswrd.delete(0, 'end')

    def on_leave_password(self, e):
        name = self.pswrd.get()
        if name == "":
            self.pswrd.insert(0, 'Password')

    def validate_input(self, new_value):
        if len(new_value) > 15:
            return False
        else:
            return True

    def show_and_hide(self):
        if self.pswrd['show'] == '*':
            self.pswrd['show'] = ''
        else:
            self.pswrd['show'] = '*'

    def on_signin(self):
        # users' inputs
        username_input = self.user.get()
        password_input = self.pswrd.get().encode()
        password_input = hashlib.sha256(password_input).hexdigest()
        # checking
        self.mycursor.execute("SELECT * FROM users WHERE username = %s AND passwordd = %s",
                              (username_input, password_input))
        Login.current_user = self.mycursor.fetchone()


        if Login.current_user == None:
            messagebox.showerror('Error','Invalid Username or Password!')

        else:
            self.root.destroy()
            main_home = home.Home()
            main_home.start()


    def on_face_signin(self):

        app = face_login.App(self.root)
        self.signin_face_btn.configure(text='Submit', command=lambda:app.login())
        app.start(self.root,365,405)


    def callback(self, url):
        webbrowser.open_new_tab(url)

    def forgot_password(self):
        self.forg_pass_w = tk.Toplevel()
        self.forg_pass_w.title('Forgot password')
        self.forg_pass_w.geometry('300x150')
        self.forg_pass_w.resizable(False, False)
        tk.Label(self.forg_pass_w, text="Enter your email:", font=('Microsoft YaHei UI Light', 14, 'bold')).pack()
        self.email_box = tk.Entry(self.forg_pass_w, width=35, fg='black',
                        border=0, bg='white', validate="key", font=('Microsoft YaHei UI Light', 10, 'bold'))
        self.email_box.pack()
        submit_btn = tk.Button(self.forg_pass_w, text="Submit",command=self.reset_password_out)
        submit_btn.pack()
        self.answer = tk.Label(self.forg_pass_w)
        self.answer.pack()

        self.forg_pass_w.mainloop()

    def reset_password_out(self):
        email_get = self.email_box.get().strip()
        self.mycursor.execute("SELECT * FROM users WHERE email = %s ",
                              (email_get,))
        row = self.mycursor.fetchone()
        if row == None:
            self.answer.configure(text='\nEmail doesnt exists!',fg='red')
        else:
            self.answer.configure(text='\nAn email will bes sent to \nyou containing your new password',fg='green')
            em = EmailMessage()
            em['From'] = self.email_sender
            em['To'] =email_get
            em['Subject'] = "Reset your G-School password"
            new_pswrd = Login.generate_pswrd()
            em.set_content(new_pswrd)
            self.mycursor.execute("UPDATE users SET passwordd = %s WHERE email = %s",
                                  (hashlib.sha256(new_pswrd.encode()).hexdigest(),email_get))
            self.mydb.commit()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, email_get, em.as_string())

    @staticmethod
    def generate_pswrd():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''
        for _ in range(10):
            password += random.choice(chars)
        return password

