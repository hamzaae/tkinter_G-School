import os
import smtplib
import ssl
import tkinter
from tkinter import ttk
import webbrowser
from tkinter import *
import re
from email.message import EmailMessage
import datetime
import subprocess
import login
import home_dashboard
from tkinter import messagebox
import mysql.connector


class Home:
    def __init__(self):
        # Creating dataBase and necessary tables

        # Initialize main window
        self.window = tkinter.Tk()
        self.window.title('G-School')
        self.window.geometry('1020x550')
        self.window.resizable(False, False)

        # Initialize notebook
        self.style0 = ttk.Style(self.window)
        self.style0.configure('lefttab.TNotebook', tabposition='ws')
        self.style1 = ttk.Style()
        self.style1.configure('Custom.TFrame', background="white")
        self.notebook = ttk.Notebook(self.window, style='lefttab.TNotebook', width=1020, height=550)

        # 0 ================ Set all variables for students ==========================
        self.cne = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.phone = StringVar()

        # 0-1 ================ Set all variables for stuff ==========================
        self.cin = StringVar()
        self.stuff_first_name = StringVar()
        self.stuff_last_name = StringVar()
        self.stuff_email = StringVar()
        self.stuff_gender = StringVar()
        self.stuff_phone = StringVar()

        # tabs config: creation, icons, add to notebook
        ## 1-creation
        self.home_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        self.students_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        self.hr_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        self.settings_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        self.about_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        ## 2-icons
        self.t1 = tkinter.PhotoImage(file='media\\home.png')
        self.t2 = tkinter.PhotoImage(file='media\\stdt.png')
        self.t3 = tkinter.PhotoImage(file='media\\tchr.png')
        self.t4 = tkinter.PhotoImage(file='media\\sett.png')
        self.t5 = tkinter.PhotoImage(file='media\\hlp.png')
        ## 3- adding and packing
        self.notebook.add(self.home_tab, text='\n\n\n   HOME    \n\n\n', image=self.t1, compound='left')
        self.notebook.add(self.students_tab, text='\n\n\nSTUDENTS\n\n\n', image=self.t2, compound='left')
        self.notebook.add(self.hr_tab, text='\n\n\n   STAFFS   \n\n\n', image=self.t3, compound='left')
        self.notebook.add(self.settings_tab, text='\n\n\n SETTINGS \n\n\n', image=self.t4, compound='left')
        self.notebook.add(self.about_tab, text='\n\n\n   ABOUT   \n\n\n', image=self.t5, compound='left')
        self.notebook.pack()
        ############# HOME Tab #############
        #0
        self.home = home_dashboard.DashBoard(self.home_tab)

        ############# STUDENTS Tab #############
        #****** Info frame
        self.students_info_frame = tkinter.LabelFrame(self.students_tab, text="Student information",
                                font=('Helveticabold', 15), bg="white", fg="crimson", height=200)
        self.students_info_frame.grid(row=0, column=0, padx=10, pady=10)
        ## Cne
        self.cne_label = tkinter.Label(self.students_info_frame, text="CNE", width=32, bg="white")
        self.cne_label.grid(row=0, column=0)
        self.cne_label_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2",textvariable=self.cne)
        self.cne_label_entry.grid(row=1, column=0, padx=10, pady=10)
        ## First-Last name
        self.vcmd_names = self.window.register(self.validate_names)
        self.firs_name_label = tkinter.Label(self.students_info_frame, text="First Name", bg="white")
        self.firs_name_label.grid(row=0, column=1)
        self.last_name_label = tkinter.Label(self.students_info_frame, text="Last Name", bg="white")
        self.last_name_label.grid(row=0, column=2)
        self.firs_name_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2", validate="key",textvariable=self.first_name,
                                validatecommand=(self.vcmd_names, '%P'))
        self.last_name_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2", validate="key",textvariable=self.last_name,
                                validatecommand=(self.vcmd_names, '%P'))
        self.firs_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.last_name_entry.grid(row=1, column=2, padx=10, pady=10)
        ## Email
        self.email_label = tkinter.Label(self.students_info_frame, text="Email", bg="white")
        self.email_label.grid(row=0, column=4)
        self.email_label_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2",textvariable=self.email)
        self.email_label_entry.grid(row=1, column=4, padx=10, pady=10)
        ## Gender
        self.gender_label = tkinter.Label(self.students_info_frame, text="Gender", bg="white")
        self.gender_combobox = ttk.Combobox(self.students_info_frame, values=["Man", "Just man"], state="readonly",textvariable=self.gender)
        self.gender_label.grid(row=3, column=1, padx=10)
        self.gender_combobox.grid(row=4, column=1, padx=10, pady=30)
        ## Phone
        self.vcmd_phone = self.window.register(self.validate_phone_number)
        self.phone_label = tkinter.Label(self.students_info_frame, text="Phone", bg="white")
        self.phone_label.grid(row=3, column=0)
        self.phone_label_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2", validate="key",textvariable=self.phone,
                                validatecommand=(self.vcmd_phone, '%P'))
        self.phone_label_entry.grid(row=4, column=0, padx=10, pady=30)
        ## Address
        self.address_label = tkinter.Label(self.students_info_frame, text="Address", bg="white")
        self.address_label.grid(row=3, column=2)
        self.address_label_entry = Text(self.students_info_frame, width=40, height=2, bg="#f2f2f2")
        self.address_label_entry.grid(row=4, column=2, columnspan=10, rowspan=10, padx=10)
        #****** Buttons frame
        self.button_frame = Frame(self.students_tab, bg="white")
        self.button_frame.place(x=40, y=200, height=50, width=680)
        ## Update Button
        self.button = tkinter.Button(self.button_frame, text="Update", fg="#001433", bg="crimson", width=20,command=self.update_student)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        ## Add Button
        self.button = tkinter.Button(self.button_frame, text="Add", fg="#001433", bg="crimson", width=20,command=self.add_student)
        self.button.grid(row=0, column=1, padx=10, pady=10)
        ## Delete Button
        self.button = tkinter.Button(self.button_frame, text="Delete", fg="#001433", bg="crimson", width=20,command=self.delete_student)
        self.button.grid(row=0, column=2, padx=10, pady=10)
        ## Clear Button
        self.button = tkinter.Button(self.button_frame, text="Clear", fg="#001433", bg="crimson", width=20,command=self.clear_student)
        self.button.grid(row=0, column=3, padx=10, pady=10)
        #****** Students table
        self.students_table_frame = Frame(self.students_tab, bg="crimson")
        self.students_table_frame.place(x=10, y=250, height=280, width=750)
        self.table_frame = Frame(self.students_table_frame, bd=4, relief=GROOVE, bg="crimson")
        self.table_frame.place(width=750, height=280)
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.table_frame,
                        columns=("Cne", "First name", "Last name", "Email", "Gender", "Phone", "Address"),
                        xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Cne", text="Cne")
        self.student_table.heading("First name", text="First name")
        self.student_table.heading("Last name", text="Last name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table["show"] = 'headings'
        self.student_table.column("Cne", width=100)
        self.student_table.column("First name", width=100)
        self.student_table.column("Last name", width=100)
        self.student_table.column("Email", width=150)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Phone", width=150)
        self.student_table.column("Address", width=150)
        self.student_table.pack(fill=BOTH, expand=1)  # To show the table
        #
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_student_data()


        ############# HR Tab #############
        #****** Info frame
        self.stuff_info_frame = tkinter.LabelFrame(self.hr_tab, text="Stuff information", font=('Helveticabold', 15),
                            bg="white", fg="green", height=200)
        self.stuff_info_frame.grid(row=0, column=0, padx=10, pady=10)
        ## Cne
        self.stuff_cne_label = tkinter.Label(self.stuff_info_frame, text="CNI", width=32, bg="white")
        self.stuff_cne_label.grid(row=0, column=0)
        self.stuff_cne_label_entry = tkinter.Entry(self.stuff_info_frame, bg="#f2f2f2",textvariable=self.cin)
        self.stuff_cne_label_entry.grid(row=1, column=0, padx=10, pady=10)
        ## First-Last name
        self.stuff_firs_name_label = tkinter.Label(self.stuff_info_frame, text="First Name", bg="white")
        self.stuff_firs_name_label.grid(row=0, column=1)
        self.stuff_last_name_label = tkinter.Label(self.stuff_info_frame, text="Last Name", bg="white")
        self.stuff_last_name_label.grid(row=0, column=2)
        self.stuff_firs_name_entry = tkinter.Entry(self.stuff_info_frame, bg="#f2f2f2", validate="key",textvariable=self.stuff_first_name,
                                validatecommand=(self.vcmd_names, '%P'))
        self.stuff_last_name_entry = tkinter.Entry(self.stuff_info_frame, bg="#f2f2f2", validate="key",textvariable=self.stuff_last_name,
                                validatecommand=(self.vcmd_names, '%P'))
        self.stuff_firs_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.stuff_last_name_entry.grid(row=1, column=2, padx=10, pady=10)
        ## Email
        self.stuff_email_label = tkinter.Label(self.stuff_info_frame, text="Email", bg="white")
        self.stuff_email_label.grid(row=0, column=4)
        self.stuff_email_label_entry = tkinter.Entry(self.stuff_info_frame, bg="#f2f2f2",textvariable=self.stuff_email)
        self.stuff_email_label_entry.grid(row=1, column=4, padx=10, pady=10)
        ## Gender combobox
        self.stuff_gender_label = tkinter.Label(self.stuff_info_frame, text="Gender", bg="white")
        self.stuff_gender_combobox = ttk.Combobox(self.stuff_info_frame, values=["Man", "Just man"], state="readonly",textvariable=self.stuff_gender,)
        self.stuff_gender_label.grid(row=3, column=1, padx=10)
        self.stuff_gender_combobox.grid(row=4, column=1, padx=10, pady=30)
        ## Phone
        self.stuff_phone_label = tkinter.Label(self.stuff_info_frame, text="Phone", bg="white")
        self.stuff_phone_label.grid(row=3, column=0)
        self.stuff_phone_label_entry = tkinter.Entry(self.stuff_info_frame, bg="#f2f2f2", validate="key",textvariable=self.stuff_phone,
                                validatecommand=(self.vcmd_phone, '%P'))
        self.stuff_phone_label_entry.grid(row=4, column=0, padx=10, pady=30)
        ## Address
        self.stuff_address_label = tkinter.Label(self.stuff_info_frame, text="Address", bg="white")
        self.stuff_address_label.grid(row=3, column=2)
        self.stuff_address_label_entry = Text(self.stuff_info_frame, width=40, height=2, bg="#f2f2f2")
        self.stuff_address_label_entry.grid(row=4, column=2, columnspan=10, rowspan=10, padx=10)
        #****** Buttons frame
        self.stuff_button_frame = Frame(self.hr_tab, bg="white")
        self.stuff_button_frame.place(x=40, y=200, height=50, width=680)
        ## Update Button
        self.stuff_button = tkinter.Button(self.stuff_button_frame, text="Update", fg="#001433", bg="green", width=20,command=self.update_stuff)
        self.stuff_button.grid(row=0, column=0, padx=10, pady=10)
        ## Add Button
        self.stuff_button = tkinter.Button(self.stuff_button_frame, text="Add", fg="#001433", bg="green", width=20,command=self.add_stuff)
        self.stuff_button.grid(row=0, column=1, padx=10, pady=10)
        ## Delete Button
        self.stuff_button = tkinter.Button(self.stuff_button_frame, text="Delete", fg="#001433", bg="green", width=20,command=self.delete_stuff)
        self.stuff_button.grid(row=0, column=2, padx=10, pady=10)
        ## Clear Button
        self.stuff_button = tkinter.Button(self.stuff_button_frame, text="Clear", fg="#001433", bg="green", width=20,command=self.clear_stuff)
        self.stuff_button.grid(row=0, column=3, padx=10, pady=10)
        #****** Stuff table
        self.stuff_table_frame = Frame(self.hr_tab, bg="green")
        self.stuff_table_frame.place(x=10, y=250, height=280, width=750)
        self.stuff_table_frame = Frame(self.stuff_table_frame, bd=4, relief=GROOVE, bg="green")
        self.stuff_table_frame.place(width=750, height=280)
        self.scroll_x = Scrollbar(self.stuff_table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.stuff_table_frame, orient=VERTICAL)
        self.stuff_table = ttk.Treeview(self.stuff_table_frame,
                                        columns=("Cne", "First name", "Last name", "Email", "Gender", "Phone", "Address"),
                                        xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.stuff_table.xview)
        self.scroll_y.config(command=self.stuff_table.yview)
        self.stuff_table.heading("Cne", text="Cne")
        self.stuff_table.heading("First name", text="First name")
        self.stuff_table.heading("Last name", text="Last name")
        self.stuff_table.heading("Email", text="Email")
        self.stuff_table.heading("Gender", text="Gender")
        self.stuff_table.heading("Phone", text="Phone")
        self.stuff_table.heading("Address", text="Address")
        self.stuff_table["show"] = 'headings'
        ## Set column width
        self.stuff_table.column("Cne", width=100)
        self.stuff_table.column("First name", width=100)
        self.stuff_table.column("Last name", width=100)
        self.stuff_table.column("Email", width=150)
        self.stuff_table.column("Gender", width=50)
        self.stuff_table.column("Phone", width=150)
        self.stuff_table.column("Address", width=150)
        self.stuff_table.pack(fill=BOTH, expand=1)  # To show the table
        # Call get_stuff_cursor
        self.stuff_table.bind("<ButtonRelease-1>", self.get_stuff_cursor)
        self.fetch_stuff_data()


        ############# SETTINGS Tab #############
        self.frame_user = tkinter.LabelFrame(self.settings_tab, text="User settings", font=('Helveticabold', 15),
                            bg="white", height=200)
        self.frame_user.pack(fill="both", expand=1)
        self.frame_general = tkinter.LabelFrame(self.settings_tab, text="General settings",
                            font=('Helveticabold', 15), bg="white")
        self.frame_general.pack(fill="both", expand=1)
        #****** Current user table
        self.current_user_label = tkinter.Label(self.frame_user, text="Current user",
                            font=('Helveticabold', 13, "bold"), bg="white", fg="green")
        self.current_user_label.place(x=0, y=0)
        self.table_frame1 = Frame(self.frame_user, bg="#101433")
        self.table_frame1.place(x=1, y=30, width=790, height=50)
        self.current_user_table = ttk.Treeview(self.table_frame1,
                columns=("User Name", "First name", "Last name", "Email","Phone","Identity"))
        self.current_user_table.heading("User Name", text="User Name")
        self.current_user_table.heading("First name", text="First name")
        self.current_user_table.heading("Last name", text="Last name")
        self.current_user_table.heading("Email", text="Email")
        self.current_user_table.heading("Phone", text="Phone")
        self.current_user_table.heading("Identity", text="Identity")
        self.current_user_table["show"] = 'headings'
        self.add_img_btn = tkinter.Button(self.frame_user, width=20, pady=7, text='add face signin', bg='#3f8ad4', fg='white',
                                      border=0,command=self.add_usr_img)
        self.add_img_btn.place(x=600, y=100)
        # Set column width
        self.current_user_table.column("User Name", width=70)
        self.current_user_table.column("First name", width=70)
        self.current_user_table.column("Last name", width=70)
        self.current_user_table.column("Email", width=90)
        self.current_user_table.column("Phone", width=60)
        self.current_user_table.column("Identity", width=80)
        self.current_user_table.pack(fill=BOTH, expand=1)  # To show the table
        # fill table -->
        #0

        self.user_info = (login.Login.current_user[1],login.Login.current_user[1],
                          login.Login.current_user[1],login.Login.current_user[4],
                          login.Login.current_user[5],login.Login.current_user[3])
        self.current_user_table.insert('','end',values=self.user_info)
        #****** Other users table
        self.other_users_label = tkinter.Label(self.frame_user, text="Other users",
                            font=('Helveticabold', 13, "bold"), bg="white", fg="red")
        self.other_users_label.place(x=0, y=150)
        self.table_frame1 = Frame(self.frame_user, bg="#101433")
        self.table_frame1.place(x=1, y=180, width=790, height=150)
        self.scroll_y = Scrollbar(self.table_frame1, orient=VERTICAL)
        self.other_users_table = ttk.Treeview(self.table_frame1,
                            columns=("Cin", "First name", "Last name", "Prev"),
                            yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.other_users_table.yview)
        self.other_users_table.heading("Cin", text="Cin")
        self.other_users_table.heading("First name", text="First name")
        self.other_users_table.heading("Last name", text="Last name")
        self.other_users_table.heading("Prev", text="Prev")
        self.other_users_table["show"] = 'headings'
        # Set column width
        self.other_users_table.column("Cin", width=100)
        self.other_users_table.column("First name", width=100)
        self.other_users_table.column("Last name", width=100)
        self.other_users_table.column("Prev", width=150)
        self.other_users_table.pack(fill=BOTH, expand=1)  # To show the table
        #****** General settings
        self.v = tkinter.StringVar(self.frame_general, "1")
        self.light_rb = tkinter.Radiobutton(self.frame_general, text=" Light mode ", variable=self.v,
                        value="1", font=('Microsoft YaHei UI Light', 11, 'bold'), bg='white',
                        command=self.set_light_mode)
        self.light_rb.place(x=15, y=30)
        self.dark_rb = tkinter.Radiobutton(self.frame_general, text=" Dark mode ", variable=self.v,
                        value="2", font=('Microsoft YaHei UI Light', 11, 'bold'), bg='white',
                        command=self.set_dark_mode)
        self.dark_rb.place(x=15, y=80)
        self.language_lbl = tkinter.Label(self.frame_general, text="     Language ",
                        font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white")
        self.language_lbl.place(x=210, y=30)
        self.mail_receive = tkinter.Checkbutton(self.frame_general, text="I want to receive notifications on my email",
                        font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white",command=self.mail_receive)
        self.mail_receive.place(x=210, y=80)
        self.n = tkinter.StringVar()
        self.lang_box = ttk.Combobox(self.frame_general, width=27, textvariable=self.n, state="readonly")
        self.lang_box['values'] = (' Arabic', ' English', ' French')
        self.lang_box.place(x=330, y=33)
        self.lang_box.current(1)
        self.signout_btn = tkinter.Button(self.frame_general, width=20, pady=7, text='Log out',
                            bg='#db6e6e', fg='white', border=0,command=self.signout)
        self.signout_btn.place(x=600, y=75)
        self.log_btn = tkinter.Button(self.frame_general, width=20, pady=7,
                        text='LOG', bg='#3f8ad4', fg='white', border=0,
                        command=self.start_logfile)
        self.log_btn.place(x=600, y=28)

        ############# ABOUT Tab #############
        # Create a Label to display the link
        with open('media\\about_text', 'r') as abt:
            # open about text and read content then pack it to about tab
            about_text = abt.read()
            self.abt_lbl = tkinter.Label(self.about_tab, text=about_text, fg='black',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), width=900, height=550, bg="white")
            self.abt_lbl.pack()
        self.link = tkinter.Label(self.about_tab, text="https://ensah.ma/",
                    font=('Helveticabold', 12), fg="blue", bg="white", cursor="hand2")
        self.link.place(x=330, y=524)
        self.link.bind("<Button-1>", lambda e: self.callback("https://ensah.ma/"))

        ########### Other
        self.email_sender = 'tkinter.gschool@gmail.com'
        self.email_password = 'tkinterPassword123'

    def validate_names(self, new_value):
        name_pattern = r'^[a-zA-Z\-\s]+$'
        if re.match(name_pattern, new_value) or new_value == '':
            return True
        else:
            return False

    def validate_email(self, new_value):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, new_value):
            return True
        else:
            return False

    def validate_phone_number(self, new_value):
        if (new_value.isdigit() or new_value.isalpha() or new_value == '') and len(new_value) <= 10:
            return True
        else:
            return False

    # Fields validity
    def validate_fLName(self, fLName):
        name_pattern = r'^[a-zA-Z\-\s]+$'
        if re.match(name_pattern, fLName) :
            return True
        else:
            return False

    def validate_phone(self,pValue):
        pattern =r'^0[567][0-9]{8}$'
        return re.match(pattern, pValue)

    def validate_cne_code(self, cValue):
        cne_pattern = r'^[A-Z]\d{9}$'
        if re.match(cne_pattern, cValue):
            return True
        else:
            return False

    def validate_cin(self,cValue):
        pattern = r'^[A-Z]{1,2}[0-9]{6}$'
        return re.match(pattern,cValue)

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def set_light_mode(self):
        self.style1.configure('Custom.TFrame', background='white')
        self.frame_general.configure(bg='white', fg='black')
        self.light_rb.configure(bg="white", fg="black", selectcolor='white')
        self.dark_rb.configure(bg="white", fg="black", selectcolor='white')
        self.language_lbl.configure(bg='white', fg='black')
        self.mail_receive.configure(bg='white', fg='black', selectcolor='white')
        self.frame_user.configure(bg='white', fg='black')
        self.abt_lbl.configure(bg='white', fg='black')
        self.link.configure(bg='white', fg='blue')
        self.current_user_label.configure(bg="white", fg="red")
        self.other_users_label.configure(bg="white", fg="green")
        self.stuff_button_frame.configure(bg="white")
        self.stuff_info_frame.configure(bg="white")
        self.stuff_cne_label.configure(fg="black", bg="white")
        self.stuff_firs_name_label.configure(fg="black", bg="white")
        self.stuff_last_name_label.configure(fg="black", bg="white")
        self.stuff_email_label.configure(fg="black", bg="white")
        self.stuff_gender_label.configure(fg="black", bg="white")
        self.stuff_phone_label.configure(fg="black", bg="white")
        self.stuff_address_label.configure(fg="black", bg="white")
        # Student lm
        self.button_frame.configure(bg="white")
        self.students_info_frame.configure(bg="white")
        self.cne_label.configure(fg="black", bg="white")
        self.firs_name_label.configure(fg="black", bg="white")
        self.last_name_label.configure(fg="black", bg="white")
        self.email_label.configure(fg="black", bg="white")
        self.gender_label.configure(fg="black", bg="white")
        self.phone_label.configure(fg="black", bg="white")
        self.address_label.configure(fg="black", bg="white")

    def set_dark_mode(self):
        self.style1.configure('Custom.TFrame', background='#26242f')
        self.frame_general.configure(bg='#26242f', fg="white")
        self.light_rb.configure(bg='#26242f', fg='white', selectcolor='black')
        self.dark_rb.configure(bg='#26242f', fg='white', selectcolor='black')
        self.language_lbl.configure(bg='#26242f', fg='white')
        self.mail_receive.configure(bg='#26242f', fg='white', selectcolor='black')
        self.frame_user.configure(bg='#26242f', fg="white")
        self.abt_lbl.configure(bg='#26242f', fg="white")
        self.link.configure(bg='#26242f', fg="#c1c6e8")
        self.current_user_label.configure(bg="#26242f", fg="red")
        self.other_users_label.configure(bg="#26242f", fg="green")
        self.stuff_button_frame.configure(bg="#26242f")
        self.stuff_info_frame.configure(bg="#26242f")
        self.stuff_cne_label.configure(bg="#26242f", fg="white")
        self.stuff_firs_name_label.configure(bg="#26242f", fg="white")
        self.stuff_last_name_label.configure(bg="#26242f", fg="white")
        self.stuff_email_label.configure(bg="#26242f", fg="white")
        self.stuff_gender_label.configure(bg="#26242f", fg="white")
        self.stuff_phone_label.configure(bg="#26242f", fg="white")
        self.stuff_address_label.configure(bg="#26242f", fg="white")
        # students dm
        self.button_frame.configure(bg="#26242f")
        self.students_info_frame.configure(bg="#26242f")
        self.cne_label.configure(bg="#26242f", fg="white")
        self.firs_name_label.configure(bg="#26242f", fg="white")
        self.last_name_label.configure(bg="#26242f", fg="white")
        self.email_label.configure(bg="#26242f", fg="white")
        self.gender_label.configure(bg="#26242f", fg="white")
        self.phone_label.configure(bg="#26242f", fg="white")
        self.address_label.configure(bg="#26242f", fg="white")

    #0
    def mail_receive(self,Subject, To, Message):
        email_user = login.Login.current_user[4]
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = To
        em['Subject'] = Subject
        em.set_content(Message)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender,self.email_password)
            smtp.sendmail(self.email_sender,email_user,em.as_string())

    #0
    def add_usr_img(self):
        self.register_new_user_window = tkinter.Toplevel(self.window)
        self.register_new_user_window.geometry("600x520")
        self.register_new_user_window.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.ok_button_register_new_user_window = tkinter.Button(self.register_new_user_window,
                    text='OK',bg='green',width=20,
                    command=lambda:login.Login.app.register_new_user(self.register_new_user_window,self.ok_button_register_new_user_window))
        self.ok_button_register_new_user_window.place(x=450, y=200)
        self.close_button_register_new_user_window = tkinter.Button(self.register_new_user_window,
                    text='CLOSE',bg='red',width=20,
                    command=self.close_event)
        self.close_button_register_new_user_window.place(x=450, y=100)
        login.Login.app.start(self.register_new_user_window,450,520)

    def disable_event(self):
        pass

    def close_event(self):
        self.register_new_user_window.destroy()
        login.Login.app.end_video()

    #0
    def signout(self):
        self.window.destroy()
        with open(login.Login.log_path, 'a') as f:
            f.write('{}{}{}\n'.format(login.Login.current_user[1], " logged out at ", datetime.datetime.now()))
            f.close()
        login.Login.current_user = None
        subprocess.call(['python', 'G-School.py'])
        login.Login().start()

    def current_user_fill(self):
        pass

    def start_logfile(self):
        os.startfile("log.txt")

    ## Students main functions

    def add_student(self):

        cne = self.cne.get()
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        gender = self.gender.get()
        phone = self.phone.get()
        address = self.address_label_entry.get('1.0', END)

        if not self.validate_fLName(first_name):
            return messagebox.showinfo("Empty Fields ", "First name not valid")

        if not self.validate_fLName(last_name):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")

        if not self.validate_cne_code(cne):
            return messagebox.showinfo("CNE not valid", "CNE not valid")

        if not self.validate_email(email):
            return messagebox.showinfo("Email not valid", "Email not valid")

        if not self.validate_phone(phone):
            return messagebox.showinfo("Phone number not valid", "Phone number not valid")

        if gender == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")

        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()

        try:
            sqlInsert = "INSERT INTO student_data values(%s,%s,%s,%s,%s,%s,%s)"
            values = (cne, first_name, last_name, email, gender, phone, address)
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            home_dashboard.DashBoard.nbr_std += 1
            self.home.update_dashboard()
            self.clear_student()

        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()

        connection.commit()
        self.fetch_student_data()
        connection.close()

    def fetch_student_data(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Student_data")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            connection.commit()
        connection.close()

    def clear_student(self):
        self.cne.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.email.set("")
        self.gender.set("")
        self.phone.set("")
        self.address_label_entry.delete('1.0', END)
        self.cne_label_entry.focus_set()

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.cne.set(row[0])
        self.first_name.set(row[1])
        self.last_name.set(row[2])
        self.email.set(row[3])
        self.gender.set(row[4])
        self.phone.set('0'+str(row[5]))
        self.address_label_entry.delete('1.0', END)
        self.address_label_entry.insert(END, row[6])

    def update_student(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cne = self.cne.get()
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        gender = self.gender.get()
        phone = self.phone.get()

        if not self.validate_fLName(first_name):
            return messagebox.showinfo("Empty Fields ", "First name not valid")

        if not self.validate_fLName(last_name):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")

        if not self.validate_cne_code(cne):
            return messagebox.showinfo("CNE not valid", "CNE not valid")

        if not self.validate_email(email):
            return messagebox.showinfo("Email not valid", "Email not valid")

        if not self.validate_phone(phone):
            return messagebox.showinfo("Phone number not valid", "Phone number not valid")

        if gender == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")

        try:
            sqlInsert = "UPDATE student_data SET cne = %s, first_name = %s, last_name = %s,email = %s, gender = %s, phone = %s, address = %s WHERE cne = %s or phone = %s"
            values = (
            cne, first_name, last_name, email, gender, phone, self.address_label_entry.get('1.0', END), cne, phone)
            cursor.execute(sqlInsert, values)
            connection.commit()
            self.fetch_student_data()
            messagebox.showinfo("Information", "Data updated successfully")

            # self.clear_student()


        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()
        connection.commit()
        self.fetch_student_data()
        connection.close()

    def delete_student(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()

        try:
            sqlInsert = "delete FROM student_data where cne= %s"
            cursor.execute(sqlInsert, (self.cne.get(),))
            connection.commit()
            self.fetch_student_data()
            self.clear_student()
            messagebox.showinfo("Information", "Student deleted successfully")
            home_dashboard.DashBoard.nbr_std -= 1
            self.home.update_dashboard()
        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()
        connection.commit()
        self.fetch_student_data()
        connection.close()

    ## Stuff main functions
    def add_stuff(self):

        cin = self.cin.get()
        first_name = self.stuff_first_name.get()
        last_name = self.stuff_last_name.get()
        email = self.stuff_email.get()
        gender = self.stuff_gender.get()
        phone = self.stuff_phone.get()
        address = self.stuff_address_label_entry.get('1.0', END)

        if not self.validate_cin(cin):
            return messagebox.showinfo("CIN not valid", "CIN not valid")

        if not self.validate_fLName(first_name):
            return messagebox.showinfo("Empty Fields ", "First name not valid")

        if not self.validate_fLName(last_name):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")

        if not self.validate_email(email):
            return messagebox.showinfo("Email not valid", "Email not valid")

        if not self.validate_phone(phone):
            return messagebox.showinfo("Phone number not valid", "Phone number not valid")

        if gender == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")

        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()

        try:
            sqlInsert = "INSERT INTO stuff_data values(%s,%s,%s,%s,%s,%s,%s)"
            values = (cin, first_name, last_name, email, gender, phone, address)
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            home_dashboard.DashBoard.nbr_stf += 1
            self.home.update_dashboard()
            self.clear_student()

        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()

        connection.commit()
        self.fetch_stuff_data()
        connection.close()

    def fetch_stuff_data(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Stuff_data")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.stuff_table.delete(*self.stuff_table.get_children())
            for row in rows:
                self.stuff_table.insert('', END, values=row)
            connection.commit()
        connection.close()
        pass

    def clear_stuff(self):
        self.cin.set("")
        self.stuff_first_name.set("")
        self.stuff_last_name.set("")
        self.stuff_email.set("")
        self.stuff_gender.set("")
        self.stuff_phone.set("")
        self.stuff_address_label_entry.delete('1.0', END)
        #self.stuff_cin_label_entry.focus_set()

    def get_stuff_cursor(self, ev):
        cursor_row = self.stuff_table.focus()
        contents = self.stuff_table.item(cursor_row)
        row = contents['values']
        self.cin.set(row[0])
        self.stuff_first_name.set(row[1])
        self.stuff_last_name.set(row[2])
        self.stuff_email.set(row[3])
        self.stuff_gender.set(row[4])
        self.stuff_phone.set('0'+str(row[5]))
        self.stuff_address_label_entry.delete('1.0', END)
        self.stuff_address_label_entry.insert(END, row[6])

    def update_stuff(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cin = self.cin.get()
        first_name = self.stuff_first_name.get()
        last_name = self.stuff_last_name.get()
        email = self.stuff_email.get()
        gender = self.stuff_gender.get()
        phone = self.stuff_phone.get()

        if not self.validate_cin(cin):
            return messagebox.showinfo("CIN not valid", "CIN not valid")

        if not self.validate_fLName(first_name):
            return messagebox.showinfo("Empty Fields ", "First name not valid")

        if not self.validate_fLName(last_name):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")

        if not self.validate_email(email):
            return messagebox.showinfo("Email not valid", "Email not valid")

        if not self.validate_phone(phone):
            return messagebox.showinfo("Phone number not valid", "Phone number not valid")

        if gender == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")

        try:
            sqlInsert = "UPDATE stuff_data SET cin = %s, first_name = %s, last_name = %s,email = %s, gender = %s, phone = %s, address = %s WHERE cin = %s or phone = %s"
            values = (
            cin, first_name, last_name, email, gender, phone, self.stuff_address_label_entry.get('1.0', END), cin,
            phone)
            cursor.execute(sqlInsert, values)
            connection.commit()
            self.fetch_stuff_data()
            messagebox.showinfo("Information", "Data updated successfully")

        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            print(e)
            connection.rollback()
        connection.commit()
        self.fetch_stuff_data()
        connection.close()

    def delete_stuff(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()

        try:
            sqlInsert = "delete FROM stuff_data where cin= %s"
            cursor.execute(sqlInsert, (self.cin.get(),))
            connection.commit()
            self.fetch_stuff_data()
            self.clear_stuff()
            messagebox.showinfo("Information", "Stuff deleted successfully")
            home_dashboard.DashBoard.nbr_stf -= 1
            self.home.update_dashboard()
        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()
        connection.commit()
        self.fetch_stuff_data()
        connection.close()

    # creating db and tables


    def start(self):
        self.window.mainloop()
