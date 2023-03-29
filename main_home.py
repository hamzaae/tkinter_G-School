import tkinter
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import *
import re


# Initialize main window
window = tk.Tk()
window.title('G-School')
window.geometry('900x550')
window.resizable(False, False)

# Initialize notebook
style0 = ttk.Style(window)
style0.configure('lefttab.TNotebook', tabposition='ws')
style1 = ttk.Style()
style1.configure('Custom.TFrame', background="white")
notebook = ttk.Notebook(window, style='lefttab.TNotebook', width=900, height=550)

# tabs config: creation, icons, add to notebook
home_tab = ttk.Frame(notebook, style='Custom.TFrame')
students_tab = ttk.Frame(notebook, style='Custom.TFrame')
hr_tab = ttk.Frame(notebook, style='Custom.TFrame')
settings_tab = ttk.Frame(notebook, style='Custom.TFrame')
about_tab = ttk.Frame(notebook, style='Custom.TFrame')

t1 = tk.PhotoImage(file='media\\home.png')
t2 = tk.PhotoImage(file='media\\stdt.png')
t3 = tk.PhotoImage(file='media\\tchr.png')
t4 = tk.PhotoImage(file='media\\sett.png')
t5 = tk.PhotoImage(file='media\\hlp.png')

notebook.add(home_tab, text='\n\n\n   HOME    \n\n\n', image=t1, compound='left')
notebook.add(students_tab, text='\n\n\nSTUDENTS\n\n\n', image=t2, compound='left')
notebook.add(hr_tab, text='\n\n\n   STAFFS   \n\n\n', image=t3, compound='left')
notebook.add(settings_tab, text='\n\n\n SETTINGS \n\n\n', image=t4, compound='left')
notebook.add(about_tab, text='\n\n\n   ABOUT   \n\n\n', image=t5, compound='left')

notebook.pack()

## Home tab


# Students tab

students_info_frame = tkinter.LabelFrame(students_tab, text="Student information", font=('Helveticabold', 15), bg="white", fg="crimson", height=200)
students_info_frame.grid(row=0, column=0, padx=10, pady=10)

####################################### Student info #############################################
# Cne
cne_label = tkinter.Label(students_info_frame, text="CNE",width=32,bg="white")
cne_label.grid(row=0,column=0)

cne_label_entry = tkinter.Entry(students_info_frame,bg="#f2f2f2")
cne_label_entry.grid(row=1,column=0, padx=10, pady=10)
# First-Last name
def validate_names(new_value):
    name_pattern = r'^[a-zA-Z\-\s]+$'
    if re.match(name_pattern, new_value) or new_value == '':
        return True
    else:
        return False
vcmd_names = window.register(validate_names)
firs_name_label = tkinter.Label(students_info_frame, text="First Name",bg="white")
firs_name_label.grid(row=0,column=1)
last_name_label =tkinter.Label(students_info_frame, text="Last Name",bg="white")
last_name_label.grid(row=0,column=2)

firs_name_entry = tkinter.Entry(students_info_frame,bg="#f2f2f2",validate="key", validatecommand=(vcmd_names, '%P'))
last_name_entry = tkinter.Entry(students_info_frame,bg="#f2f2f2",validate="key", validatecommand=(vcmd_names, '%P'))
firs_name_entry.grid(row=1,column=1, padx=10, pady=10)
last_name_entry.grid(row=1,column=2, padx=10, pady=10)

# Email
def validate_email(new_value):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, new_value):
        return True
    else:
        return False

#vcmd_email = window.register(validate_email)
email_label = tkinter.Label(students_info_frame, text="Email",bg="white")
email_label.grid(row=0,column=4)

email_label_entry = tkinter.Entry(students_info_frame,bg="#f2f2f2")
email_label_entry.grid(row=1,column=4, padx=10, pady=10)

# Gender combobox
gender_label = tkinter.Label(students_info_frame, text="Gender",bg="white")
gender_combobox = ttk.Combobox(students_info_frame, values=["Man", "Just man"], state="readonly")
gender_label.grid(row=3, column=1,padx=10)
gender_combobox.grid(row=4, column=1,padx=10,pady=30)

# Phone
def validate_phone_number(new_value):
    if (new_value.isdigit() or new_value=='') and len(new_value) <= 10:
        return True
    else:
        return False
vcmd_phone = window.register(validate_phone_number)

phone_label = tkinter.Label(students_info_frame, text="Phone",bg="white")
phone_label.grid(row=3,column=0)

phone_label_entry = tkinter.Entry(students_info_frame,bg="#f2f2f2",validate="key", validatecommand=(vcmd_phone, '%P'))
phone_label_entry.grid(row=4,column=0, padx=10, pady=30)

# Address
address_label = tkinter.Label(students_info_frame, text="Address",bg="white")
address_label.grid(row=3,column=2)

address_label_entry = Text(students_info_frame, width=40, height=2,bg="#f2f2f2")
address_label_entry.grid(row=4,column=2,columnspan=10,rowspan=10,padx=10)



#================ Button Frame =================================
button_frame = Frame(students_tab, bg="white")
button_frame.place(x=40,y=200,height=50,width=680)

# Update Button
button = tkinter.Button(button_frame, text="Update", fg="#001433", bg="crimson", width=20)
button.grid(row=0, column=0, padx=10, pady=10)
# Add Button
button = tkinter.Button(button_frame, text="Add", fg="#001433", bg="crimson", width=20)
button.grid(row=0, column=1, padx=10, pady=10)
# Delete Button
button = tkinter.Button(button_frame, text="Delete", fg="#001433", bg="crimson", width=20)
button.grid(row=0, column=2, padx=10, pady=10)
# Clear Button
button = tkinter.Button(button_frame, text="Clear", fg="#001433", bg="crimson", width=20)
button.grid(row=0, column=3, padx=10, pady=10)

#================ Student information table (Frame) =================================
students_table_frame = Frame(students_tab, bg="crimson")
students_table_frame.place(x=10, y=250,height=280,width=750)

table_frame = Frame(students_table_frame,bd=4,relief=GROOVE,bg="crimson")
table_frame.place(width=750,height=280)


scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
student_table = ttk.Treeview(table_frame,columns=("Cne","First name","Last name","Email","Gender","Phone","Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("Cne", text="Cne")
student_table.heading("First name", text="First name")
student_table.heading("Last name", text="Last name")
student_table.heading("Email", text="Email")
student_table.heading("Gender", text="Gender")
student_table.heading("Phone", text="Phone")
student_table.heading("Address", text="Address")
student_table["show"] = 'headings'


        # Set column width
student_table.column("Cne",width=100)
student_table.column("First name",width=100)
student_table.column("Last name",width=100)
student_table.column("Email",width=150)
student_table.column("Gender",width=50)
student_table.column("Phone",width=150)
student_table.column("Address",width=150)
student_table.pack(fill=BOTH,expand=1) # To show the table





## HR tab
# Stuff tab

stuff_info_frame = tkinter.LabelFrame(hr_tab, text="Stuff information", font=('Helveticabold', 15), bg="white", fg="green", height=200)
stuff_info_frame.grid(row=0, column=0, padx=10, pady=10)

####################################### Stuff info #############################################
# Cne
stuff_cne_label = tkinter.Label(stuff_info_frame, text="CNI", width=32, bg="white")
stuff_cne_label.grid(row=0, column=0)

stuff_cne_label_entry = tkinter.Entry(stuff_info_frame, bg="#f2f2f2")
stuff_cne_label_entry.grid(row=1, column=0, padx=10, pady=10)
# First-Last name
stuff_firs_name_label = tkinter.Label(stuff_info_frame, text="First Name", bg="white")
stuff_firs_name_label.grid(row=0, column=1)
stuff_last_name_label =tkinter.Label(stuff_info_frame, text="Last Name", bg="white")
stuff_last_name_label.grid(row=0, column=2)

stuff_firs_name_entry = tkinter.Entry(stuff_info_frame, bg="#f2f2f2",validate="key", validatecommand=(vcmd_names, '%P'))
stuff_last_name_entry = tkinter.Entry(stuff_info_frame, bg="#f2f2f2",validate="key", validatecommand=(vcmd_names, '%P'))
stuff_firs_name_entry.grid(row=1, column=1, padx=10, pady=10)
stuff_last_name_entry.grid(row=1, column=2, padx=10, pady=10)

# Email
stuff_email_label = tkinter.Label(stuff_info_frame, text="Email", bg="white")
stuff_email_label.grid(row=0, column=4)

stuff_email_label_entry = tkinter.Entry(stuff_info_frame, bg="#f2f2f2")
stuff_email_label_entry.grid(row=1, column=4, padx=10, pady=10)

# Gender combobox
stuff_gender_label = tkinter.Label(stuff_info_frame, text="Gender", bg="white")
stuff_gender_combobox = ttk.Combobox(stuff_info_frame, values=["Man", "Just man"], state="readonly")
stuff_gender_label.grid(row=3, column=1, padx=10)
stuff_gender_combobox.grid(row=4, column=1, padx=10, pady=30)

# Phone
stuff_phone_label = tkinter.Label(stuff_info_frame, text="Phone", bg="white")
stuff_phone_label.grid(row=3, column=0)

stuff_phone_label_entry = tkinter.Entry(stuff_info_frame, bg="#f2f2f2",validate="key", validatecommand=(vcmd_phone, '%P'))
stuff_phone_label_entry.grid(row=4, column=0, padx=10, pady=30)

# Address
stuff_address_label = tkinter.Label(stuff_info_frame, text="Address", bg="white")
stuff_address_label.grid(row=3, column=2)

stuff_address_label_entry = Text(stuff_info_frame, width=40, height=2, bg="#f2f2f2")
stuff_address_label_entry.grid(row=4, column=2, columnspan=10, rowspan=10, padx=10)



#================ Button Frame =================================
stuff_button_frame = Frame(hr_tab, bg="white")
stuff_button_frame.place(x=40, y=200, height=50, width=680)

# Update Button
stuff_button = tkinter.Button(stuff_button_frame, text="Update", fg="#001433", bg="green", width=20)
stuff_button.grid(row=0, column=0, padx=10, pady=10)
# Add Button
stuff_button = tkinter.Button(stuff_button_frame, text="Add", fg="#001433", bg="green", width=20)
stuff_button.grid(row=0, column=1, padx=10, pady=10)
# Delete Button
stuff_button = tkinter.Button(stuff_button_frame, text="Delete", fg="#001433", bg="green", width=20)
stuff_button.grid(row=0, column=2, padx=10, pady=10)
# Clear Button
stuff_button = tkinter.Button(stuff_button_frame, text="Clear", fg="#001433", bg="green", width=20)
stuff_button.grid(row=0, column=3, padx=10, pady=10)

#================ Student information table (Frame) =================================
stuff_table_frame = Frame(hr_tab, bg="green")
stuff_table_frame.place(x=10, y=250, height=280, width=750)

stuff_table_frame = Frame(stuff_table_frame, bd=4, relief=GROOVE, bg="green")
stuff_table_frame.place(width=750, height=280)


scroll_x=Scrollbar(stuff_table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(stuff_table_frame, orient=VERTICAL)
stuff__table = ttk.Treeview(stuff_table_frame, columns=("Cne", "First name", "Last name", "Email", "Gender", "Phone", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=stuff__table.xview)
scroll_y.config(command=stuff__table.yview)
stuff__table.heading("Cne", text="Cne")
stuff__table.heading("First name", text="First name")
stuff__table.heading("Last name", text="Last name")
stuff__table.heading("Email", text="Email")
stuff__table.heading("Gender", text="Gender")
stuff__table.heading("Phone", text="Phone")
stuff__table.heading("Address", text="Address")
stuff__table["show"] = 'headings'


        # Set column width
stuff__table.column("Cne", width=100)
stuff__table.column("First name", width=100)
stuff__table.column("Last name", width=100)
stuff__table.column("Email", width=150)
stuff__table.column("Gender", width=50)
stuff__table.column("Phone", width=150)
stuff__table.column("Address", width=150)
stuff__table.pack(fill=BOTH, expand=1) # To show the table













## About tab
with open('media\\about_text', 'r') as abt:
    # open about text and read content then pack it to about tab
    about_text = abt.read()
    abt_lbl = tk.Label(about_tab, text=about_text, fg='black',
                       font=('Microsoft YaHei UI Light', 11, 'bold'), width=900, height=550,bg="white")
    abt_lbl.pack()


    # Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)


    # Create a Label to display the link
    link = tk.Label(about_tab, text="https://ensah.ma/", font=('Helveticabold', 15), fg="blue",bg="white",
                    cursor="hand2")
    link.place(x=320, y=520)
    link.bind("<Button-1>", lambda e: callback("https://ensah.ma/"))

## Settings tab
frame_user = tkinter.LabelFrame(settings_tab, text="User settings", font=('Helveticabold', 15),bg="white",height=200)
frame_user.pack(fill="both", expand=1)
frame_general = tkinter.LabelFrame(settings_tab, text="General settings",font=('Helveticabold', 15),bg="white")
frame_general.pack(fill="both", expand=1)

## Settings tab

# ================ Current user Table =============================

current_user_label = tkinter.Label(frame_user, text="Current user", font=('Helveticabold', 13, "bold"), bg="white", fg="green")
current_user_label.place(x=0, y=0)

table_frame1 = Frame(frame_user, bg="#101433")
table_frame1.place(x=1, y=30, width=790, height=50)

current_user_table = ttk.Treeview(table_frame1,
                                  columns=("Cin", "First name", "Last name","Prev"))
current_user_table.heading("Cin", text="Cin")
current_user_table.heading("First name", text="First name")
current_user_table.heading("Last name", text="Last name")
current_user_table.heading("Prev", text="Prev")
current_user_table["show"] = 'headings'

# Set column width
current_user_table.column("Cin", width=100)
current_user_table.column("First name", width=100)
current_user_table.column("Last name", width=100)
current_user_table.column("Prev", width=150)
current_user_table.pack(fill=BOTH, expand=1)  # To show the table

# ================ Other users Table =============================

other_users_label = tkinter.Label(frame_user, text="Other users", font=('Helveticabold', 13, "bold"), bg="white", fg="red")
other_users_label.place(x=0, y=150)

table_frame1 = Frame(frame_user, bg="#101433")
table_frame1.place(x=1, y=180, width=790, height=150)

scroll_y = Scrollbar(table_frame1, orient=VERTICAL)

other_users_table = ttk.Treeview(table_frame1,
                                 columns=("Cin", "First name", "Last name","Prev"), yscrollcommand=scroll_y.set)

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=other_users_table.yview)

other_users_table.heading("Cin", text="Cin")
other_users_table.heading("First name", text="First name")
other_users_table.heading("Last name", text="Last name")
other_users_table.heading("Prev", text="Prev")
other_users_table["show"] = 'headings'


# Set column width
other_users_table.column("Cin", width=100)
other_users_table.column("First name", width=100)
other_users_table.column("Last name", width=100)
other_users_table.column("Prev", width=150)
other_users_table.pack(fill=BOTH, expand=1)  # To show the table


v = tkinter.StringVar(frame_general, "1")
def set_light_mode():
    style1.configure('Custom.TFrame', background='white')
    frame_general.configure(bg='white',fg='black')
    light_rb.configure(bg="white",fg="black",selectcolor='white')
    dark_rb.configure(bg="white",fg="black",selectcolor='white')
    language_lbl.configure(bg='white', fg='black')
    mail_receive.configure(bg='white', fg='black',selectcolor='white')
    frame_user.configure(bg='white',fg='black')
    abt_lbl.configure(bg='white',fg='black')
    link.configure(bg='white',fg='blue')
    current_user_label.configure(bg="white", fg="red")
    other_users_label.configure(bg="white", fg="green")
    stuff_button_frame.configure(bg="white")
    stuff_info_frame.configure(bg="white")
    stuff_cne_label.configure(fg="black", bg="white")
    stuff_firs_name_label.configure(fg="black", bg="white")
    stuff_last_name_label.configure(fg="black", bg="white")
    stuff_email_label.configure(fg="black", bg="white")
    stuff_gender_label.configure(fg="black", bg="white")
    stuff_phone_label.configure(fg="black", bg="white")
    stuff_address_label.configure(fg="black", bg="white")
    # Student lm
    button_frame.configure(bg="white")
    students_info_frame.configure(bg="white")
    cne_label.configure(fg="black", bg="white")
    firs_name_label.configure(fg="black", bg="white")
    last_name_label.configure(fg="black", bg="white")
    email_label.configure(fg="black", bg="white")
    gender_label.configure(fg="black", bg="white")
    phone_label.configure(fg="black", bg="white")
    address_label.configure(fg="black", bg="white")

def set_dark_mode():
    style1.configure('Custom.TFrame', background='#26242f')
    frame_general.configure(bg='#26242f',fg="white")
    light_rb.configure(bg='#26242f',fg='white',selectcolor='black')
    dark_rb.configure(bg='#26242f',fg='white',selectcolor='black')
    language_lbl.configure(bg='#26242f',fg='white')
    mail_receive.configure(bg='#26242f',fg='white',selectcolor='black')
    frame_user.configure(bg='#26242f', fg="white")
    abt_lbl.configure(bg='#26242f', fg="white")
    link.configure(bg='#26242f', fg="blue")
    current_user_label.configure(bg="#26242f", fg="red")
    other_users_label.configure(bg="#26242f", fg="green")
    stuff_button_frame.configure(bg="#26242f")
    stuff_info_frame.configure(bg="#26242f")
    stuff_cne_label.configure(bg="#26242f", fg="white")
    stuff_firs_name_label.configure(bg="#26242f", fg="white")
    stuff_last_name_label.configure(bg="#26242f", fg="white")
    stuff_email_label.configure(bg="#26242f", fg="white")
    stuff_gender_label.configure(bg="#26242f", fg="white")
    stuff_phone_label.configure(bg="#26242f", fg="white")
    stuff_address_label.configure(bg="#26242f", fg="white")
    # students dm
    button_frame.configure(bg="#26242f")
    students_info_frame.configure(bg="#26242f")
    cne_label.configure(bg="#26242f", fg="white")
    firs_name_label.configure(bg="#26242f", fg="white")
    last_name_label.configure(bg="#26242f", fg="white")
    email_label.configure(bg="#26242f", fg="white")
    gender_label.configure(bg="#26242f", fg="white")
    phone_label.configure(bg="#26242f", fg="white")
    address_label.configure(bg="#26242f", fg="white")


# 1.General settings
light_rb = tkinter.Radiobutton(frame_general, text=" Light mode ", variable=v,
                    value="1",font=('Microsoft YaHei UI Light', 11, 'bold'),bg='white', command=set_light_mode)
light_rb.place(x=15,y=30)
dark_rb = tkinter.Radiobutton(frame_general, text=" Dark mode ", variable=v,
                    value="2",font=('Microsoft YaHei UI Light', 11, 'bold'),bg='white', command=set_dark_mode)
dark_rb.place(x=15,y=80)
language_lbl = tkinter.Label(frame_general, text="     Language ",
              font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white")
language_lbl.place(x=210, y=30)
mail_receive = tkinter.Checkbutton(frame_general,text="I want to receive notifications on my email",
              font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white")
mail_receive.place(x=210, y=80)

n = tk.StringVar()
lang_box = ttk.Combobox(frame_general, width=27, textvariable=n, state="readonly")
lang_box['values'] = (' Arabic', ' English', ' French')

lang_box.place(x=330,y=33)
lang_box.current(1)

signout_btn = tk.Button(frame_general, width=20, pady=7, text='Log out', bg='#db6e6e', fg='white', border=0)
signout_btn.place(x=600,y=75)
hhh_btn = tk.Button(frame_general, width=20, pady=7, text='LOG', bg='#3f8ad4', fg='white', border=0)
hhh_btn.place(x=600,y=28)
# # 2.User settings
# _lbl = tkinter.Label(frame_user, text="      Language ",
#               font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white")
# _lbl.place(x=0, y=230)

# mainloop
window.mainloop()
