import tkinter
import tkinter as tk
from tkinter import ttk
import webbrowser

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

# Home tab
# Students tab
# HR tab
## Settings tab


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
frame_user = tkinter.LabelFrame(settings_tab, text="User settings", font=('Helveticabold', 15),bg="white")
frame_user.pack(fill="both", expand=1)
frame_general = tkinter.LabelFrame(settings_tab, text="General settings",font=('Helveticabold', 15),bg="white")
frame_general.pack(fill="both", expand=1)


v = tkinter.StringVar(frame_general, "1")
def set_light_mode():
    style1.configure('Custom.TFrame', background='white')
    frame_general.configure(bg='white',fg='black')
    light_rb.configure(bg="white",fg="black")
    dark_rb.configure(bg="white",fg="black")
    language_lbl.configure(bg='white', fg='black')
    frame_user.configure(bg='white',fg='black')
    abt_lbl.configure(bg='white',fg='black')
    link.configure(bg='white',fg='blue')

def set_dark_mode():
    style1.configure('Custom.TFrame', background='#26242f')
    frame_general.configure(bg='#26242f',fg="white")
    light_rb.configure(bg='#26242f',fg='white')
    dark_rb.configure(bg='#26242f',fg='white')
    language_lbl.configure(bg='#26242f',fg='white')
    frame_user.configure(bg='#26242f', fg="white")
    abt_lbl.configure(bg='#26242f', fg="white")
    link.configure(bg='#26242f', fg="blue")

light_rb = tkinter.Radiobutton(frame_general, text=" Light mode ", variable=v,
                    value="1",font=('Microsoft YaHei UI Light', 11, 'bold'),bg='white', command=set_light_mode)
light_rb.place(x=0,y=30)
dark_rb = tkinter.Radiobutton(frame_general, text=" Dark mode ", variable=v,
                    value="2",font=('Microsoft YaHei UI Light', 11, 'bold'),bg='white', command=set_dark_mode)
dark_rb.place(x=0,y=70)
language_lbl = tkinter.Label(frame_general, text="      Language ",
              font=('Microsoft YaHei UI Light', 11, 'bold'), bg="white")
language_lbl.place(x=0, y=110)


# mainloop
window.mainloop()
