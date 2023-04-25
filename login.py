import smtplib
import ssl
import tkinter
import tkinter as tk
import datetime
from email.message import EmailMessage
from tkinter import messagebox
import webbrowser
import face_login
import mysql.connector
import hashlib
import random
import string
import home
import home_dashboard


class Login:
    log_path = 'log/log.txt'
    current_user = {}
    app = face_login.App_face()
    root = tk.Tk()
    def __init__(self):
        # Create the window
        Login.root.title('G-School LOGIN')
        Login.root.geometry('700x402')
        Login.root.resizable(False, False)
        # Add image and frame
        self.bg = tk.PhotoImage(file="media\\slide.png")
        self.img = tk.Label(Login.root, image=self.bg)
        self.img.place(x=-360, y=0)
        self.frame = tk.Frame(Login.root, width=340, height=405, bg='white')
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
        self.vcmd = (Login.root.register(self.validate_input), '%P')
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
        # 5-keep me logged in
        self.keep_me = tkinter.IntVar()

        self.keep_me_btn = tkinter.Checkbutton(self.frame, text="Keep me logged in ",
                        variable=self.keep_me, onvalue=1, offvalue=0,
                        font=('verdana', 9), bg='white')
        self.keep_me_btn.place(x=30, y=240)
        # add signin and face_signin buttons
        self.signin_btn = tk.Button(self.frame, width=39, pady=7, text='Sign in',
                        bg='#6cc570', fg='white', border=0,
                        command=self.on_signin)
        self.signin_btn.place(x=35, y=270)
        self.signin_face_btn = tk.Button(self.frame, width=39, pady=7,
                        text='Face Sign in', bg='#5271ff', fg='white', border=0,
                        command=self.on_face_signin)
        self.signin_face_btn.place(x=35, y=315)
        self.end_video = tkinter.Button(self.frame, width=18, pady=7,
                                        text='End camera', bg='#fc4e63', fg='white', border=0)
        # camera
        self.camera_label = tkinter.Label(Login.root)
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
        self.mycursor.execute("SELECT COUNT(*) FROM users")
        home_dashboard.DashBoard.nbr_usr = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data")
        home_dashboard.DashBoard.nbr_std = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM stuff_data")
        home_dashboard.DashBoard.nbr_stf = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE gender = 'Man'")
        home_dashboard.DashBoard.nbr_std_m = self.mycursor.fetchone()[0]
        home_dashboard.DashBoard.nbr_std_w = home_dashboard.DashBoard.nbr_std - home_dashboard.DashBoard.nbr_std_m
        self.mycursor.execute("SELECT COUNT(*) FROM stuff_data WHERE gender = 'Man'")
        home_dashboard.DashBoard.nbr_stf_m = self.mycursor.fetchone()[0]
        home_dashboard.DashBoard.nbr_stf_w = home_dashboard.DashBoard.nbr_stf - home_dashboard.DashBoard.nbr_stf_m
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'AP1'")
        home_dashboard.DashBoard.nbr_std_ap1 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'AP2'")
        home_dashboard.DashBoard.nbr_std_ap2 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'ID1'")
        home_dashboard.DashBoard.nbr_std_id1 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'ID2'")
        home_dashboard.DashBoard.nbr_std_id2 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'ID3'")
        home_dashboard.DashBoard.nbr_std_id3 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GI2'")
        home_dashboard.DashBoard.nbr_std_gi1 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GI1'")
        home_dashboard.DashBoard.nbr_std_gi2 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GI-GL'")
        home_dashboard.DashBoard.nbr_std_gigl = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GI-BI'")
        home_dashboard.DashBoard.nbr_std_gibi = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GC1'")
        home_dashboard.DashBoard.nbr_std_gc1 = self.mycursor.fetchone()[0]
        self.mycursor.execute("SELECT COUNT(*) FROM student_data WHERE field = 'GC2'")
        home_dashboard.DashBoard.nbr_std_gc2 = self.mycursor.fetchone()[0]
        # TODO : all fields
        # Other
        self.email_sender = 'tkinter.gschool@gmail.com'
        self.email_password = 'vizjfzoeihmxchqu'

    def start(self):
        self.mycursor.execute("SELECT * FROM users WHERE keepme = true")
        Login.current_user = self.mycursor.fetchone()
        if Login.current_user == None:
            Login.root.mainloop()
        else:
            Login.app.end_video()
            with open(Login.log_path, 'a') as f:
                f.write('{}{}{}\n'.format(Login.current_user[1], " logged in using keep me at ", datetime.datetime.now()))
                f.close()
            with open('log/logins_nbr.txt', "r") as f:
                lines = f.readlines()

            last_line = lines[-1].strip()
            now = datetime.datetime.now()
            today = str(now.date())
            if last_line.split(':')[0] == today:
                parts = last_line.split(':')
                parts[-1] = ':'+str(int(parts[-1])+1)
                new_last_line = "".join(parts)

                lines[-1] = new_last_line

                with open('log/logins_nbr.txt', "w") as f:
                    f.writelines(lines)
            else:
                with open('log/logins_nbr.txt', "a") as f:
                    f.write(f'\n{today}:1')

            Login.root.destroy()
            main_home = home.Home()
            main_home.start()

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
            messagebox.showerror('Error', 'Invalid Username or Password!')

        else:
            Login.app.end_video()
            with open(Login.log_path, 'a') as f:
                f.write('{}{}{}\n'.format(Login.current_user[1], " logged in at ", datetime.datetime.now()))
                f.close()
            if self.keep_me.get() == 1:
                self.mycursor.execute("UPDATE users SET keepme = true WHERE username = %s",(username_input,))
                self.mydb.commit()

            Login.root.destroy()
            main_home = home.Home()
            main_home.start()

    def on_face_signin(self):
        self.signin_face_btn.configure(text='Submit', command=lambda:Login.app.login(), width=18)
        self.end_video = tkinter.Button(self.frame, width=18, pady=7,
                                        text='End camera', bg='#fc4e63', fg='white', border=0)
        self.end_video.configure(command=self.end_video_cmd)
        self.end_video.place(x=175, y=315)
        Login.app.start(Login.root, 365, 405)

    def end_video_cmd(self):
        self.end_video.destroy()
        self.signin_face_btn.configure(width=39, pady=7,
                        text='Face Sign in', bg='#5271ff', fg='white', border=0,
                        command=self.on_face_signin)
        self.signin_face_btn.place(x=35, y=315)
        Login.app.end_video()

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
                                  (hashlib.sha256(new_pswrd.encode()).hexdigest(), email_get))
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



