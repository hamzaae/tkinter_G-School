import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import *
import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import login

class DashBoard:
    nbr_std = 0
    nbr_std_m = 0
    nbr_std_w = 0
    nbr_stf = 0
    nbr_stf_m = 0
    nbr_stf_w = 0
    nbr_usr = 0
    nbr_usr_m = 0
    nbr_usr_w = 0
    nbr_std_ap1 = 0
    nbr_std_ap2 = 0
    nbr_std_id1 = 0
    nbr_std_id2 = 0
    nbr_std_id3 = 0
    nbr_std_gi1 = 0
    nbr_std_gi2 = 0
    nbr_std_gigl = 0
    nbr_std_gibi = 0
    nbr_std_gc1 = 0
    nbr_std_gc2 = 0
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
        self.style = ttk.Style(window)
        self.style.configure('graph.TNotebook', tabposition='s')
        self.style1 = ttk.Style()
        self.style1.configure('Custom.TFrame', background="white")
        self.graph_notebook = ttk.Notebook(window, style='graph.TNotebook', width=500, height=300)
        self.graph_notebook.place(x=20, y=200)
        self.students_tab = ttk.Frame(self.graph_notebook, style='Custom.TFrame')
        self.stuff_tab = ttk.Frame(self.graph_notebook, style='Custom.TFrame')
        self.users_tab = ttk.Frame(self.graph_notebook, style='Custom.TFrame')
        self.graph_notebook.add(self.students_tab, text='              STUDENTS              ',
                                image=self.t1, compound='left')
        self.graph_notebook.add(self.stuff_tab, text='              STAFFS              ',
                                image=self.t2, compound='left')
        self.graph_notebook.add(self.users_tab, text='              USERS              ',
                                image=self.t3, compound='left')
        # Students graph 0
        self.fig0 = Figure(figsize=(8, 6))
        self.a = self.fig0.add_subplot(221)
        self.data00 = [DashBoard.nbr_std_ap1, DashBoard.nbr_std_ap2]
        self.a.pie(self.data00, labels=['AP1', 'AP2'])
        self.a.set(aspect="equal", title='CP STUDENTS')
        self.canvas_a = FigureCanvasTkAgg(self.fig0, master=self.students_tab)
        self.canvas_a.get_tk_widget().pack()
        self.canvas_a.draw()
        self.d = self.fig0.add_subplot(222)
        self.data01 = [DashBoard.nbr_std_id1, DashBoard.nbr_std_id2,DashBoard.nbr_std_id3,
                       DashBoard.nbr_std_gi2, DashBoard.nbr_std_gi2, DashBoard.nbr_std_gigl,
                       DashBoard.nbr_std_gibi, DashBoard.nbr_std_gc1, DashBoard.nbr_std_gc2]
        self.d.pie(self.data01, labels=['ID1', 'ID2', 'ID3', 'GI1', 'GI2', 'GI-GL', 'GI-BI', 'GC1', 'GC2'])
        self.d.set(aspect="equal", title='CI STUDENTS')
        self.canvas_d = FigureCanvasTkAgg(self.fig0, master=self.students_tab)
        self.canvas_d.get_tk_widget().pack()
        self.canvas_d.draw()
        # Users graph 1
        self.fig1 = Figure(figsize=(8, 6))
        self.b = self.fig1.add_subplot(121)
        size = 0.3
        self.vals = np.array(
            [[DashBoard.nbr_std_m, DashBoard.nbr_std_w], [DashBoard.nbr_stf_m, DashBoard.nbr_stf_w], [1., 0.]])

        self.cmap = plt.get_cmap("tab20c")
        self.outer_colors = self.cmap(np.arange(3) * 4)
        self.inner_colors = self.cmap(np.array([1, 2, 5, 6, 9, 10]))
        self.b.pie(self.vals.sum(axis=1), radius=1, colors=self.outer_colors,
              wedgeprops=dict(width=size, edgecolor='w'), labels=['STUDENTS', 'STUFF', 'USERS'])

        self.b.pie(self.vals.flatten(), radius=1 - size, colors=self.inner_colors,
              wedgeprops=dict(width=size, edgecolor='w'), labels=['M', 'W', 'M', 'W', 'M', 'W'], labeldistance=0.7)

        self.b.set(aspect="equal", title='Users and genders pie')
        # self.fig1.legend(loc=(-0.3, 0))
        self.canvas_b = FigureCanvasTkAgg(self.fig1, master=self.users_tab)
        self.canvas_b.get_tk_widget().pack()
        self.canvas_b.draw()

        self.c = self.fig1.add_subplot(122)
        with open('log/logins_nbr.txt', 'r') as f:
            data = f.readlines()[1:]

        # separate date and number_of_logins into separate lists
        dates = []
        logins = []
        for d in data:
            date, num_logins = d.strip().split(':')
            dates.append(date)
            logins.append(int(num_logins))
        if len(dates) > 6:
            dates = dates[-6:]
            logins = logins[-6:]
        # plot data
        self.c.plot(dates, logins)
        #self.c.set_xlabel('Date')
        #self.c.set_ylabel('Number of logins')
        self.c.set_title('Number of logins')
        self.fig1.autofmt_xdate()
        self.fig1.tight_layout(pad=7.0)
        self.canvas_c = FigureCanvasTkAgg(self.fig1, master=self.users_tab)
        self.canvas_c.get_tk_widget().pack()
        self.canvas_c.draw()

        self.plot(self.stuff_tab)



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
        canvas.get_tk_widget().pack()
        canvas.draw()

    def plot0(self, window):
        self.data0 = [DashBoard.nbr_usr, DashBoard.nbr_stf, DashBoard.nbr_std]
        if self.fig0.axes:
            self.fig0.delaxes(self.fig0.axes[0])
            self.canvas_a.get_tk_widget().destroy()
        self.a = self.fig0.add_subplot(111)
        self.a.pie(self.data0, labels=['USERS', 'STUFF', 'STUDENTS'])
        self.canvas = FigureCanvasTkAgg(self.fig0, master=window)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()



    def plot1(self,window):
        self.vals = np.array(
            [[DashBoard.nbr_std_m, DashBoard.nbr_std_w], [DashBoard.nbr_stf_m, DashBoard.nbr_stf_w], [1., 0.]])
        if self.fig1.axes:
            self.fig1.delaxes(self.fig1.axes[0])
            self.canvas_b.get_tk_widget().destroy()
        self.b = self.fig1.add_subplot(111)
        size = 0.3
        self.b.pie(self.vals.sum(axis=1), radius=1, colors=self.outer_colors,
                   wedgeprops=dict(width=size, edgecolor='w'), labels=['STUDENTS', 'STUFF', 'USERS'])

        self.b.pie(self.vals.flatten(), radius=1 - size, colors=self.inner_colors,
                   wedgeprops=dict(width=size, edgecolor='w'), labels=['M', 'W', 'M', 'W', 'M', 'W'])

        self.b.set(aspect="equal", title='Users and genders pie')
        self.canvas_b = FigureCanvasTkAgg(self.fig1, master=window)
        self.canvas_b.get_tk_widget().pack()
        self.canvas_b.draw()

    def update_dashboard(self):
        self.nbr_students.configure(text=DashBoard.nbr_std)
        self.nbr_stuffs.configure(text=DashBoard.nbr_stf)
        self.nbr_users.configure(text=DashBoard.nbr_usr)
        self.plot(self.stuff_tab)
        self.plot0(self.students_tab)
        self.plot1(self.users_tab)

