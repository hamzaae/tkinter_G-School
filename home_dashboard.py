import tkinter
from PIL import ImageTk, Image
from datetime import *
import time
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import login

class DashBoard:
    nbr_std = 0
    nbr_stf = 0
    nbr_usr = 0
    def __init__(self, window):
        # header
        '''frame'''
        self.header = tkinter.Frame(window)
        self.header.place(x=0, y=0, width=1020, height=115)
        '''user image and info'''
        self.img = (Image.open("media\\man.png")).resize((300,205), Image.ANTIALIAS)
        self.curr_img = ImageTk.PhotoImage(self.img)
        self.curr_img_fr = tkinter.Frame(self.header)
        self.curr_img_fr.place(x=820, y=5, width=82, height=105)
        self.curr_img_lbl = tkinter.Label(self.curr_img_fr, image=self.curr_img)
        self.curr_img_lbl.pack()
        self.curr_name = tkinter.Label(self.header, text=login.Login.current_user[1],font=('MS Serif', 17,'bold'))
        self.curr_name.place(x=800, y=30, anchor="e")
        self.curr_type = tkinter.Label(self.header, text=login.Login.current_user[3],font=('MS sans Serif', 13))
        self.curr_type.place(x=800, y=60, anchor="e")
        self.curr_mail = tkinter.Label(self.header, text=login.Login.current_user[4],font=('MS sans Serif', 10))
        self.curr_mail.place(x=800, y=90, anchor="e")

        '''date and time'''
        self.clock_image = ImageTk.PhotoImage(file="media\\clndr.png")
        self.date_time_image = tkinter.Label(self.header, image=self.clock_image)
        self.date_time_image.place(x=18, y=32)
        self.date_time = tkinter.Label(self.header)
        self.date_time.place(x=55, y=20)
        self.show_time()

        # dashboard
        '''number of students, stuffs and users'''
        self.t1 = tkinter.PhotoImage(file='media\\stdt.png')
        self.t2 = tkinter.PhotoImage(file='media\\tchr.png')
        self.t3 = tkinter.PhotoImage(file='media\\sett.png')
        self.studnts_lbl = tkinter.Label(window, text=" Number of students", font=('Franklin Gothic Medium', 15, 'bold'),
                            bg='white', image=self.t1, compound='left')
        self.studnts_lbl.place(x=50, y=125)
        self.hr_lbl = tkinter.Label(window, text=" Number of stuffs", font=('Franklin Gothic Medium', 15, 'bold'),
                            bg='white', image=self.t2, compound='left')
        self.hr_lbl.place(x=380, y=125)
        self.users_lbl = tkinter.Label(window, text=" Number of users", font=('Franklin Gothic Medium', 15, 'bold'),
                            bg='white', image=self.t3, compound='left')
        self.users_lbl.place(x=680, y=125)
        self.nbr_students = tkinter.Label(window, text=DashBoard.nbr_std, font=('Tunga', 18),
                                          bg='white')
        self.nbr_students.place(x=165, y=160)
        self.nbr_stuffs = tkinter.Label(window, text=DashBoard.nbr_stf, font=('Tunga', 18),
                                        bg='white')
        self.nbr_stuffs.place(x=495, y=160)
        self.nbr_users = tkinter.Label(window, text=DashBoard.nbr_usr, font=('Tunga', 18),
                                       bg='white')
        self.nbr_users.place(x=795, y=160)


        '''graphs'''
        self.plot(window)



    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 19, "bold"), bd=0)
        self.date_time.after(100, self.show_time)

    def plot(self, window):
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v = np.array([16, 16.31925, 17.6394, 16.003, 17.2861, 17.3131, 19.1259, 18.9694, 22.0003, 22.81226])
        p = np.array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
                      19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

        fig = Figure(figsize=(6, 6))
        a = fig.add_subplot(111)
        a.scatter(v, x, color='red')
        a.plot(p, range(2 + max(x)), color='blue')
        a.invert_yaxis()

        a.set_title("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().place(x=100, y=300)
        canvas.draw()

    def update_dashboard(self):
        self.nbr_students.configure(text=DashBoard.nbr_std)
        self.nbr_stuffs.configure(text=DashBoard.nbr_stf)
        self.nbr_users.configure(text=DashBoard.nbr_usr)



