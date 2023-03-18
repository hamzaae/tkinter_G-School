import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('G-School')
window.geometry('900x550')
window.resizable(False, False)



style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='ws')
notebook = ttk.Notebook(window,style='lefttab.TNotebook',width=900,height=550)
home_tab = ttk.Frame(notebook)
students_tab = ttk.Frame(notebook)
hr_tab = ttk.Frame(notebook)
settings_tab = ttk.Frame(notebook)
about_tab = ttk.Frame(notebook)

notebook.add(home_tab, text='\n\n\n   HOME    \n\n\n')
notebook.add(students_tab, text='\n\n\nSTUDENTS\n\n\n')
notebook.add(hr_tab, text='\n\n\n   STAFFS   \n\n\n')
notebook.add(settings_tab, text='\n\n\n SETTINGS \n\n\n')
notebook.add(about_tab, text='\n\n\n   ABOUT   \n\n\n')

notebook.pack()





window.mainloop()
