import tkinter as tk
from tkinter import ttk

# Initialize main window
window = tk.Tk()
window.title('G-School')
window.geometry('900x550')
window.resizable(False, False)


# Initialize notebook
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='ws')
notebook = ttk.Notebook(window,style='lefttab.TNotebook',width=900,height=550)

# tabs config: creation, icons, add to notebook
home_tab = ttk.Frame(notebook)
students_tab = ttk.Frame(notebook)
hr_tab = ttk.Frame(notebook)
settings_tab = ttk.Frame(notebook)
about_tab = ttk.Frame(notebook)

t1 = tk.PhotoImage(file='media\\home.png')
t2 = tk.PhotoImage(file='media\\stdt.png')
t3 = tk.PhotoImage(file='media\\tchr.png')
t4 = tk.PhotoImage(file='media\\sett.png')
t5 = tk.PhotoImage(file='media\\hlp.png')

notebook.add(home_tab, text='\n\n\n   HOME    \n\n\n',image=t1, compound='left')
notebook.add(students_tab, text='\n\n\nSTUDENTS\n\n\n',image=t2, compound='left')
notebook.add(hr_tab, text='\n\n\n   STAFFS   \n\n\n',image=t3, compound='left')
notebook.add(settings_tab, text='\n\n\n SETTINGS \n\n\n',image=t4, compound='left')
notebook.add(about_tab, text='\n\n\n   ABOUT   \n\n\n',image=t5, compound='left')

notebook.pack()

# Home tab
# Students tab
# HR tab
# Settings tab
# About tab
with open('media\\about_text', 'r') as abt:
    about_text = abt.read()
    abt_lbl = tk.Label(about_tab, text=about_text,fg='black',bg='white',font=('Microsoft YaHei UI Light',11,'bold'),width=900,height=550)
    abt_lbl.pack()




window.mainloop()
