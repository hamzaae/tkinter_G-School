import hashlib
import smtplib
import ssl
import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import Image as pimg, ImageTk
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
import pandas as pd
import os
from tkinter import filedialog


class Home:
    def __init__(self):
        # Creating dataBase and necessary tables and connecting to db
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="g_school"
        )
        self.mycursor = self.mydb.cursor()

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
        self.student_entry_search = StringVar()
        self.student_search = StringVar()
        self.image_student_path = StringVar()
        self.field = StringVar()

        # 0-1 ================ Set all variables for stuff ==========================
        self.cin = StringVar()
        self.stuff_first_name = StringVar()
        self.stuff_last_name = StringVar()
        self.stuff_email = StringVar()
        self.stuff_gender = StringVar()
        self.stuff_phone = StringVar()
        self.stuff_search = StringVar()
        self.stuff_entry_search = StringVar()

        # 0-1 =============== Set all variables for users ===========================
        self.username = StringVar()
        self.user_first_name = StringVar()
        self.user_last_name = StringVar()
        self.user_email = StringVar()
        self.user_gender = StringVar()
        self.user_contact = StringVar()
        self.user_identity = StringVar()
        self.user_password0 = StringVar()
        self.user_password1 = StringVar()

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
        self.stf_img = tkinter.PhotoImage(file='media\\upload_img.png')
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
        # TODO : import and export csv
        # student image
        self.img_student = (pimg.open("db\\admin.jpg")).resize((300, 205), pimg.ANTIALIAS)
        self.img_student = ImageTk.PhotoImage(self.img_student)
        self.img_fr_student= tkinter.Frame(self.students_tab)
        self.img_fr_student.place(x=780, y=23, width=110, height=140)
        self.img_lbl_student = tkinter.Label(self.img_fr_student, image=self.img_student)
        self.img_lbl_student.pack()
        self.img_btn_student = tkinter.Button(self.students_tab, text='  Upload image ',
                                image=self.stf_img, compound='left', bg='#689df2', command=self.upload_student_img)
        self.img_btn_student.place(x=780, y=172)
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
        self.gender_combobox = ttk.Combobox(self.students_info_frame, values=["Man", "Woman"], state="readonly",textvariable=self.gender)
        self.gender_label.grid(row=3, column=1, padx=10)
        self.gender_combobox.grid(row=4, column=1, padx=10, pady=30)
        ## Phone
        self.vcmd_phone = self.window.register(self.validate_phone_number)
        self.phone_label = tkinter.Label(self.students_info_frame, text="Phone", bg="white")
        self.phone_label.grid(row=3, column=0)
        self.phone_label_entry = tkinter.Entry(self.students_info_frame, bg="#f2f2f2", validate="key",textvariable=self.phone,
                                validatecommand=(self.vcmd_phone, '%P'))
        self.phone_label_entry.grid(row=4, column=0, padx=10, pady=30)
        ## field
        self.field_label = tkinter.Label(self.students_info_frame, text="Field", bg="white")
        val_fields = ['AP1','AP2','ID1','ID2','ID3','GI1','GI2','GI-GL','GI-BI','GC1','GC2']
        self.field_combobox = ttk.Combobox(self.students_info_frame, values=val_fields, state="readonly",
                                            textvariable=self.field)
        self.field_label.grid(row=3, column=2, padx=10)
        self.field_combobox.grid(row=4, column=2, padx=10, pady=30)
        ## Address
        self.address_label = tkinter.Label(self.students_info_frame, text="Address", bg="white")
        self.address_label.grid(row=3, column=3)
        self.address_label_entry = Text(self.students_info_frame, width=20, height=2, bg="#f2f2f2")
        self.address_label_entry.grid(row=4, column=3, columnspan=10, rowspan=10, padx=10)
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
        ## import Button
        self.import_csv_button = tkinter.Button(self.students_tab, text="Import from CSV", fg="#001433", bg="#ff0080",
                                                width=15, command=self.clear_stuff)
        self.import_csv_button.place(x=770, y=460)
        ## Export Button
        self.import_csv_button = tkinter.Button(self.students_tab, text="Export to CSV", fg="#001433", bg="#00ff80",
                                                width=15,
                                                command=self.export_student)
        self.import_csv_button.place(x=770, y=500)
        ## Search by (label and button)
        self.student_search_label = tkinter.Label(self.students_tab, text="Search by", fg="crimson", bg="white")
        self.student_search_label.place(x=770, y=250)
        self.student_search_combobox = ttk.Combobox(self.students_tab, values=["Cin", "Phone", "Email"],
                                                    state="readonly",
                                                    textvariable=self.student_search, width=6)
        self.student_search_combobox.place(x=835, y=250)
        self.student_search_combobox.set("Cne")

        self.student_search_entry = tkinter.Entry(self.students_tab, bg="#f2f2f2",
                                                  textvariable=self.student_entry_search)
        self.student_search_entry.place(x=770, y=280)

        self.student_search_button = tkinter.Button(self.students_tab, text="Search", fg="black", bg="#00ff80",
                                                    command=self.search_student)
        self.student_search_button.place(x=848, y=305)
        ## Show all button
        self.student_showAll_button = tkinter.Button(self.students_tab, text="Show all", fg="black", bg="#00ff80",
                                                     command=self.fetch_student_data)
        self.student_showAll_button.place(x=770, y=305)
        #****** Students table
        self.students_table_frame = Frame(self.students_tab, bg="crimson")
        self.students_table_frame.place(x=10, y=250, height=280, width=750)
        self.table_frame = Frame(self.students_table_frame, bd=4, relief=GROOVE, bg="crimson")
        self.table_frame.place(width=750, height=280)
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.table_frame,
                        columns=("Cne", "First name", "Last name", "Email", "Gender", "Phone", "Address", "Field"),
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
        self.student_table.heading("Field", text="Field")
        self.student_table["show"] = 'headings'
        self.student_table.column("Cne", width=80)
        self.student_table.column("First name", width=80)
        self.student_table.column("Last name", width=80)
        self.student_table.column("Email", width=130)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Phone", width=90)
        self.student_table.column("Address", width=140)
        self.student_table.column("Field", width=50)
        self.student_table.pack(fill=BOTH, expand=1)  # To show the table
        #
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_student_data()


        ############# HR Tab #############
        # staff image
        self.img_staff = (pimg.open("db\\admin.jpg")).resize((300, 205), pimg.ANTIALIAS)
        self.img_staff = ImageTk.PhotoImage(self.img_staff)
        self.img_fr_staff = tkinter.Frame(self.hr_tab)
        self.img_fr_staff.place(x=780, y=23, width=110, height=140)
        self.img_lbl_staff = tkinter.Label(self.img_fr_staff, image=self.img_staff)
        self.img_lbl_staff.pack()
        self.img_btn_staff = tkinter.Button(self.hr_tab, text='  Upload image ',
                                image=self.stf_img, compound='left', bg='#689df2', command=self.upload_stuff_img)
        self.img_btn_staff.place(x=780, y=172)
        #****** Info frame
        self.stuff_info_frame = tkinter.LabelFrame(self.hr_tab, text="Stuff information", font=('Helveticabold', 15),
                            bg="white", fg="green", height=200, width=1000)
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
        self.stuff_gender_combobox = ttk.Combobox(self.stuff_info_frame, values=["Man", "Woman"], state="readonly",textvariable=self.stuff_gender,)
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
        self.stuff_button_frame.place(x=40, y=200, height=50, width=980)
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
        self.import_csv_button = tkinter.Button(self.stuff_button_frame, text="Import from CSV", fg="#001433", bg="green", width=20,command=self.clear_stuff)
        self.import_csv_button.grid(row=0, column=4, padx=10, pady=10)
        ## import Button
        self.import_csv_button = tkinter.Button(self.hr_tab, text="Import from CSV", fg="#001433", bg="#00ffff",
                                                width=15, command=self.clear_stuff)
        self.import_csv_button.place(x=770, y=460)
        ## Export Button
        self.import_csv_button = tkinter.Button(self.hr_tab, text="Export to CSV", fg="#001433", bg="#00ff80", width=15,
                                                command=self.export_stuff)
        self.import_csv_button.place(x=770, y=500)
        ## Search by (label and button)
        self.stuff_search_label = tkinter.Label(self.hr_tab, text="Search by", fg="green", bg="white")
        self.stuff_search_label.place(x=770, y=250)
        self.stuff_search_combobox = ttk.Combobox(self.hr_tab, values=["Cin", "Phone", "Email"], state="readonly",
                                                  textvariable=self.stuff_search, width=6)
        self.stuff_search_combobox.place(x=835, y=250)
        self.stuff_search_combobox.set("Cin")

        self.stuff_search_entry = tkinter.Entry(self.hr_tab, bg="#f2f2f2", textvariable=self.stuff_entry_search)
        self.stuff_search_entry.place(x=770, y=280)

        self.stuff_search_button = tkinter.Button(self.hr_tab, text="Search", fg="black", bg="#00ff80",
                                                  command=self.search_stuff)
        self.stuff_search_button.place(x=848, y=305)
        ## Show all button
        self.stuff_showAll_button = tkinter.Button(self.hr_tab, text="Show all", fg="black", bg="#00ff80",
                                                   command=self.fetch_stuff_data)
        self.stuff_showAll_button.place(x=770, y=305)
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
        # user image
        self.img = (pimg.open("db\\admin.jpg")).resize((300, 205), pimg.ANTIALIAS)
        self.curr_img = ImageTk.PhotoImage(self.img)
        self.curr_img_fr = tkinter.Frame(self.frame_user)
        self.curr_img_fr.place(x=815, y=1, width=90, height=100)
        self.curr_img_lbl = tkinter.Label(self.curr_img_fr, image=self.curr_img)
        self.curr_img_lbl.pack()
        # user buttons
        self.add_img_btn = tkinter.Button(self.frame_user, width=20, pady=7, text='add face signin', bg='#3f8ad4', fg='white',
                                      border=0,command=self.add_usr_img)
        self.add_img_btn.place(x=600, y=107)
        self.add_usr_btn = tkinter.Button(self.frame_user, width=20, pady=7, text='Add new user', bg='#54ab1a', fg='white',
                                      border=0, command=self.add_new_usr)
        self.add_usr_btn.place(x=760, y=107)
        self.change_pswrd_btn = tkinter.Button(self.frame_user, width=20, pady=7, text='Change password', bg='#388bc2', fg='white',
                                      border=0)
        self.change_pswrd_btn.place(x=440, y=107)
        self.update_usr_info_btn = tkinter.Button(self.frame_user, width=20, pady=7, text='Update user info', bg='#3c6f91', fg='white',
                                      border=0, command=self.update_user_info)
        self.update_usr_info_btn.place(x=280, y=107)
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

        self.user_info = (login.Login.current_user[0],login.Login.current_user[6],
                          login.Login.current_user[7],login.Login.current_user[3],
                          login.Login.current_user[4],login.Login.current_user[2])
        self.current_user_table.insert('','end',values=self.user_info)
        # ****** Other users table
        self.other_users_label = tkinter.Label(self.frame_user, text="Other users",
                                               font=('Helveticabold', 13, "bold"), bg="white", fg="red")
        self.other_users_label.place(x=0, y=150)
        self.table_frame1 = Frame(self.frame_user, bg="#101433")
        self.table_frame1.place(x=1, y=180, width=790, height=150)
        self.scroll_y = Scrollbar(self.table_frame1, orient=VERTICAL)
        self.other_users_table = ttk.Treeview(self.table_frame1,
                                              columns=("First name", "Last name", "Prev"),
                                              yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.other_users_table.yview)
        self.other_users_table.heading("First name", text="First name")
        self.other_users_table.heading("Last name", text="Last name")
        self.other_users_table.heading("Prev", text="Prev")
        self.other_users_table["show"] = 'headings'
        # Set column width
        self.other_users_table.column("First name", width=100)
        self.other_users_table.column("Last name", width=100)
        self.other_users_table.column("Prev", width=150)
        self.other_users_table.pack(fill=BOTH, expand=1)  # To show the table
        # Call get_stuff_cursor
        self.other_users_table.bind("<ButtonRelease-1>", self.get_other_users_cursor)
        self.fetch_other_users()
        #****** General settings
        # TODO : factory reset
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
        self.factory_btn = tkinter.Button(self.frame_general, width=20, pady=7,
                        text='Factory reset', bg='#f54747', fg='white', border=0,)
        self.factory_btn.place(x=759, y=75)

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
        #dashboard
        self.home.set_light_mode()

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
        #dashboard
        self.home.set_dark_mode()

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
        self.mycursor.execute("UPDATE users SET keepme = false WHERE keepme = true")
        self.mydb.commit()
        subprocess.call(['python', 'G-School.py'])
        #login.Login().start()

    def current_user_fill(self):
        pass

    def start_logfile(self):
        os.startfile("log\\log.txt")

    ## Students main functions

    def add_student(self):

        cne = self.cne.get()
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        gender = self.gender.get()
        phone = self.phone.get()
        address = self.address_label_entry.get('1.0', END)
        field = self.field.get()

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

        if field == "":
            return messagebox.showinfo("Field not determined", "Please try to select field")

        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()

        try:
            sqlInsert = "INSERT INTO student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (cne, first_name, last_name, email, gender, phone, address, field,"")
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            home_dashboard.DashBoard.nbr_std += 1
            if gender == 'Man':
                home_dashboard.DashBoard.nbr_std_m += 1
            else:
                home_dashboard.DashBoard.nbr_std_w += 1
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
        self.field.set("")

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
        self.field.set(row[7])

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
        field = self.field.get()

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

        if field == "":
            return messagebox.showinfo("Field not determined", "Please try to select field")

        try:
            sqlInsert = "UPDATE student_data SET cne = %s, first_name = %s, last_name = %s,email = %s, gender = %s, phone = %s, address = %s, field = %s WHERE cne = %s or phone = %s"
            values = (
            cne, first_name, last_name, email, gender, phone, self.address_label_entry.get('1.0', END), field, cne, phone)
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

    def search_student(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        if self.student_search.get() == "Cne":
            if not self.validate_cne_code(self.student_search_entry.get()):
                return messagebox.showinfo("CNE not valid", "CNE not valid")

        if self.student_search.get() == "Phone":
            if not self.validate_phone(self.student_search_entry.get()):
                return messagebox.showinfo("Phone not valid", "Phone not valid")

        if self.student_search.get() == "Email":
            if not self.validate_email(self.student_search_entry.get()):
                return messagebox.showinfo("Email not valid", "Email not valid")

        cursor.execute(
            f"SELECT * FROM Student_data WHERE {self.student_search.get()} = '{self.student_entry_search.get()}'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            connection.commit()
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
            sqlInsert = "INSERT INTO stuff_data values(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (cin, first_name, last_name, email, gender, phone, address,"")
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            home_dashboard.DashBoard.nbr_stf += 1
            if gender == 'Man':
                home_dashboard.DashBoard.nbr_stf_m += 1
            else:
                home_dashboard.DashBoard.nbr_stf_w += 1
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

    def search_stuff(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        if self.stuff_search.get() == "Cin":
            if not self.validate_cin(self.stuff_search_entry.get()):
                return messagebox.showinfo("CIN not valid", "CIN not valid")

        if self.stuff_search.get() == "Phone":
            if not self.validate_phone(self.stuff_search_entry.get()):
                return messagebox.showinfo("Phone not valid", "Phone not valid")

        if self.stuff_search.get() == "Email":
            if not self.validate_email(self.stuff_search_entry.get()):
                return messagebox.showinfo("Email not valid", "Email not valid")

        cursor.execute(f"SELECT * FROM Stuff_data WHERE {self.stuff_search.get()} = '{self.stuff_entry_search.get()}'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.stuff_table.delete(*self.stuff_table.get_children())
            for row in rows:
                self.stuff_table.insert('', END, values=row)
            connection.commit()
        connection.close()

    # Export function
    def export_stuff(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM g_school.Stuff_data")
        rows = cursor.fetchall()
        file_path = filedialog.askdirectory()
        if os.path.isfile(rf"{file_path}\Stuff_data.csv"):
            os.remove(rf"{file_path}\Stuff_data.csv")

        for row in rows:
            df = pd.read_sql_query("SELECT * FROM Stuff_data", connection)

            df.to_csv(rf'{file_path}\Stuff_data.csv', index=False)

    def export_student(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Student_data")
        rows = cursor.fetchall()
        file_path = filedialog.askdirectory()
        if os.path.isfile(rf"{file_path}\Student_data.csv"):
            os.remove(rf"{file_path}\Student_data.csv")

        for row in rows:
            df = pd.read_sql_query("SELECT * FROM Student_data", connection)

            df.to_csv(rf'{file_path}\Student_data.csv')

    # User functions
    def add_new_usr(self):
        self.register_window = tkinter.Toplevel(self.window)
        self.register_window.geometry("500x500")
        self.register_window.title("registration form")

        lb1 = Label(self.register_window, text="UserName", width=10, font=("arial", 10))
        lb1.place(x=20, y=20)
        en1 = Entry(self.register_window, textvariable=self.username)
        en1.place(x=200, y=20)
        lb2 = Label(self.register_window, text="First Name", width=10, font=("arial", 10))
        lb2.place(x=20, y=60)
        en2 = Entry(self.register_window, textvariable=self.user_first_name)
        en2.place(x=200, y=60)
        lb3 = Label(self.register_window, text="Last Name", width=10, font=("arial", 10))
        lb3.place(x=20, y=120)
        en3 = Entry(self.register_window, textvariable=self.user_last_name)
        en3.place(x=200, y=120)

        lb3 = Label(self.register_window, text="Enter Email", width=10, font=("arial", 10))
        lb3.place(x=19, y=160)
        en4 = Entry(self.register_window, textvariable=self.user_email)
        en4.place(x=200, y=160)

        lb4 = Label(self.register_window, text="Contact Number", width=13, font=("arial", 10))
        lb4.place(x=19, y=200)
        en5 = Entry(self.register_window, textvariable=self.user_contact)
        en5.place(x=200, y=200)

        lb5 = Label(self.register_window, text="Select Gender", width=15, font=("arial", 10))
        lb5.place(x=5, y=240)
        # vars = IntVar()
        ttk.Combobox(self.register_window, values=["Male", "Female"], textvariable=self.user_gender).place(x=200, y=240,
                                                                                                           width=100)

        self.identity_combo = ttk.Combobox(self.register_window,
                                           values=["Admin", "User", "Student", "Teacher", "Administration"],
                                           textvariable=self.user_identity)
        self.identity_combo.place(x=200, y=275, width=100)
        self.identity_combo.set("User")
        lb2 = Label(self.register_window, text="Select Identity", width=13, font=("arial", 10))
        lb2.place(x=14, y=280)

        lb6 = Label(self.register_window, text="Enter Password", width=13, font=("arial", 10))
        lb6.place(x=19, y=320)
        en6 = Entry(self.register_window, show='*', textvariable=self.user_password0)
        en6.place(x=200, y=320)

        lb7 = Label(self.register_window, text="Re-Enter Password", width=15, font=("arial", 10))
        lb7.place(x=21, y=360)
        en7 = Entry(self.register_window, show='*', textvariable=self.user_password1)
        en7.place(x=200, y=360)

        Button(self.register_window, text="Register", width=10, fg="#001433", bg="#00ff80",
               command=self.register_user).place(x=200, y=400)
        self.register_window.attributes('-topmost', 1)  # Makes the window show above all the others
        self.register_window.attributes('-topmost', 0)
        self.register_window.mainloop()

    def register_user(self):
        if not self.validate_fLName(self.user_first_name.get()):
            return messagebox.showinfo("Empty Fields ", "First name not valid")
        if not self.validate_fLName(self.user_last_name.get()):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")
        if not self.validate_email(self.user_email.get()):
            return messagebox.showinfo("Email not valid", "Email not valid")
        if self.user_gender.get() == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")
        if self.user_password0 == "":
            return messagebox.showinfo("Empty field", "try to fill the password field")
        if self.user_password1 == "":
            return messagebox.showinfo("Empty field", "try to fill the password field")
        if self.user_password0.get() != self.user_password1.get():
            return messagebox.showinfo("Password error", "Please try to enter the same password")

        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        try:
            sqlInsert = "INSERT INTO users values(%s,%s,%s,%s,%s,%s,%s,%s)"
            encrypted_password = hashlib.sha256(self.user_password1.get().encode()).hexdigest()
            values = (self.username.get(), encrypted_password, self.user_identity.get(), self.user_email.get(),
                      self.user_contact.get(), False, self.user_first_name.get(), self.user_last_name.get())
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            self.user_password0.set("")
            self.username.set("")
            self.user_first_name.set("")
            self.user_last_name.set("")
            self.user_email.set("")
            self.user_contact.set("")
            self.user_password1.set("")
            self.user_gender.set("")



        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()

        connection.commit()
        self.fetch_other_users()
        connection.close()

    def fetch_other_users(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT username,username,type FROM users")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.other_users_table.delete(*self.other_users_table.get_children())
            for row in rows:
                self.other_users_table.insert('', END, values=row)
            connection.commit()
        connection.close()

    def get_other_users_cursor(self):
        cursor_row = self.other_users_table.focus()
        contents = self.other_users_table.item(cursor_row)
        row = contents['values']
        self.cne.set(row[0])
        self.first_name.set(row[1])
        self.last_name.set(row[2])
        self.email.set(row[3])
        self.gender.set(row[4])
        self.phone.set(row[5])
        self.address_label_entry.delete('1.0', END)
        self.address_label_entry.insert(END, row[6])

    def update_user_info(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE keepme =1")
        result = cursor.fetchall()

        self.register_window = tkinter.Toplevel(self.window)
        self.register_window.geometry("500x500")
        self.register_window.title("registration form")

        lb1 = Label(self.register_window, text="UserName", width=10, font=("arial", 10))
        lb1.place(x=20, y=20)
        en1 = Entry(self.register_window, textvariable=self.username)
        en1.place(x=200, y=20)
        lb2 = Label(self.register_window, text="First Name", width=10, font=("arial", 10))
        lb2.place(x=20, y=60)
        en2 = Entry(self.register_window, textvariable=self.user_first_name)
        en2.place(x=200, y=60)
        lb3 = Label(self.register_window, text="Last Name", width=10, font=("arial", 10))
        lb3.place(x=20, y=120)
        en3 = Entry(self.register_window, textvariable=self.user_last_name)
        en3.place(x=200, y=120)

        lb3 = Label(self.register_window, text="Enter Email", width=10, font=("arial", 10))
        lb3.place(x=19, y=160)
        en4 = Entry(self.register_window, textvariable=self.user_email)
        en4.place(x=200, y=160)

        lb4 = Label(self.register_window, text="Contact Number", width=13, font=("arial", 10))
        lb4.place(x=19, y=200)
        en5 = Entry(self.register_window, textvariable=self.user_contact)
        en5.place(x=200, y=200)

        lb5 = Label(self.register_window, text="Select Gender", width=15, font=("arial", 10))
        lb5.place(x=5, y=240)
        # vars = IntVar()
        ttk.Combobox(self.register_window, values=["Male", "Female"], textvariable=self.user_gender).place(x=200, y=240,
                                                                                                           width=100)

        self.identity_combo = ttk.Combobox(self.register_window,
                                           values=["Admin", "User", "Student", "Teacher", "Administration"],
                                           textvariable=self.user_identity)
        self.identity_combo.place(x=200, y=275, width=100)
        self.identity_combo.set("User")
        lb2 = Label(self.register_window, text="Select Identity", width=13, font=("arial", 10))
        lb2.place(x=14, y=280)

        lb6 = Label(self.register_window, text="Enter Password", width=13, font=("arial", 10))
        lb6.place(x=19, y=320)
        en6 = Entry(self.register_window, show='*', textvariable=self.user_password0)
        en6.place(x=200, y=320)

        lb7 = Label(self.register_window, text="Re-Enter Password", width=15, font=("arial", 10))
        lb7.place(x=21, y=360)
        en7 = Entry(self.register_window, show='*', textvariable=self.user_password1)
        en7.place(x=200, y=360)

        self.username.set(f"{result[0][0]}")
        self.user_password0.set("")
        self.user_password1.set("")
        self.user_identity.set(f"{result[0][2]}")
        self.user_email.set(f"{result[0][3]}")
        self.user_contact.set(f"{result[0][4]}")
        self.user_first_name.set(f"{result[0][6]}")
        self.user_last_name.set(f"{result[0][7]}")

        # self.username.set()

        Button(self.register_window, text="Register", width=10, fg="#001433", bg="#00ff80",
               command=self.update_user).place(x=200, y=400)
        self.register_window.attributes('-topmost', 1)  # Makes the window show above all the others
        self.register_window.attributes('-topmost', 0)
        self.register_window.mainloop()

    def update_user(self):
        if not self.validate_fLName(self.user_first_name.get()):
            return messagebox.showinfo("Empty Fields ", "First name not valid")
        if not self.validate_fLName(self.user_last_name.get()):
            return messagebox.showinfo("Empty Fields ", "Last name not valid")
        if not self.validate_email(self.user_email.get()):
            return messagebox.showinfo("Email not valid", "Email not valid")
        if self.user_gender.get() == "":
            return messagebox.showinfo("Gender not determined", "Please try to select gender")
        if self.user_password0 == "":
            return messagebox.showinfo("Empty field", "try to fill the password field")
        if self.user_password1 == "":
            return messagebox.showinfo("Empty field", "try to fill the password field")
        if self.user_password0.get() != self.user_password1.get():
            return messagebox.showinfo("Password error", "Please try to enter the same password")

        connection = mysql.connector.connect(host="localhost", user="root", password="password123",
                                             database="g_school")
        cursor = connection.cursor()
        try:
            sqlInsert = "UPDATE users SET username=%s,passwordd=%s,type=%s,email=%s,phone=%s,firstname=%s,lastname=%s,gender=%s WHERE keepme=1"
            encrypted_password = hashlib.sha256(self.user_password1.get().encode()).hexdigest()
            global new_user_name
            new_user_name = self.username.get()
            values = (self.username.get(), encrypted_password, self.user_identity.get(), self.user_email.get(),
                      self.user_contact.get(), self.user_first_name.get(), self.user_last_name.get(),
                      self.user_gender.get())
            cursor.execute(sqlInsert, values)
            connection.commit()

            messagebox.showinfo("Information", "Data saved successfully")
            self.user_password0.set("")
            self.username.set("")
            self.user_first_name.set("")
            self.user_last_name.set("")
            self.user_email.set("")
            self.user_contact.set("")
            self.user_password1.set("")
            self.user_gender.set("")
        except Exception as e:
            messagebox.showinfo("sql error:", f"{e}")
            connection.rollback()

        connection.commit()
        cursor.execute("SELECT * FROM users WHERE username = %s ", (new_user_name,))
        login.Login.current_user = cursor.fetchone()
        self.current_user_table.delete(*self.current_user_table.get_children())

        self.user_info = (login.Login.current_user[0], login.Login.current_user[6],
                          login.Login.current_user[7], login.Login.current_user[3],
                          login.Login.current_user[4], login.Login.current_user[2])
        self.current_user_table.insert('', 'end', values=self.user_info)

        connection.close()
        self.register_window.destroy()

    def change_password_gui(self):
        # Create a top-level window
        top = tkinter.Toplevel()
        top.title("Change Password")

        # Add a label for the old password
        old_password_label = tkinter.Label(top, text="Old Password")
        old_password_label.pack()

        # Add an entry for the old password
        old_password_entry = tkinter.Entry(top, show="*")
        old_password_entry.pack()

        # Add a label for the new password
        new_password_label = tkinter.Label(top, text="New Password")
        new_password_label.pack()

        # Add an entry for the new password
        new_password_entry = tkinter.Entry(top, show="*")
        new_password_entry.pack()

        # Add a button to change the password
        change_password_button = tkinter.Button(top, text="Change Password", command=self.change_password)
        change_password_button.pack()

        # Start the tkinter event loop
        top.mainloop()

    def change_password(self):
        pass

    def upload_student_img(self):
        file_types = [('jpg Images', '*.jpg'), ('jpeg Images', '*.jpeg')]
        file = tkinter.filedialog.askopenfilename(filetypes=file_types)
        if file:
            self.image_student_path = file
            self.img_lbl_student.destroy()
            self.img_student = (pimg.open(file)).resize((300, 205), pimg.ANTIALIAS)
            self.img_student = ImageTk.PhotoImage(self.img_student)
            self.img_fr_student = tkinter.Frame(self.students_tab)
            self.img_fr_student.place(x=780, y=23, width=110, height=140)
            self.img_lbl_student = tkinter.Label(self.img_fr_student, image=self.img_student)
            self.img_lbl_student.pack()

            # TODO : import img to db and to frame student

    def upload_stuff_img(self):
        file_types = [('jpg Images', '*.jpg'), ('jpeg Images', '*.jpeg')]
        file = tkinter.filedialog.askopenfilename(filetypes=file_types)
        if file:
            pass
            # TODO : import img to db and to frame stuff



    def start(self):
        self.window.mainloop()
###UT
