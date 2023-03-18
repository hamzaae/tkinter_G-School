import tkinter as tk


root = tk.Tk()
root.title('G-School LOGIN')
root.geometry('700x405')
root.resizable(False, False)

# Add image file
bg = tk.PhotoImage(file="slide.png")

# Show image using label
img = tk.Label(root, image=bg)
img.place(x=-360, y=0)

frame = tk.Frame(root, width=340, height=405,bg='white')
frame.place(x=360)

head = tk.Label(frame,text='ENSAH G-SCHOOL LOGIN',font=("Helvetica", "16"),bg='white')
head.place(x=68,y=45)

# Show logo
logo = tk.PhotoImage(file="logo-ensah_50x50.png")
img_logo = tk.Label(frame, image=logo,bg='white')
img_logo.place(x=8, y=30)

# Add inputs and ligne decorator
user = tk.Entry(frame, width= 25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
user.place(x=30, y=130)
user.insert(0,'Username')

pswrd = tk.Entry(frame, width= 25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
pswrd.place(x=30, y=200)
pswrd.insert(0,'Password')

tk.Frame(frame,width=295, height=2,bg='black').place(x=25,y=167)
tk.Frame(frame,width=295, height=2,bg='black').place(x=25,y=237)

# Sign in and sign up
signin_btn = tk.Button(frame,width=39,pady=7,text='Sign in',bg='#6cc570',fg='white',border=0)
signin_btn.place(x=35, y=270)
signup_lbl = tk.Label(frame,text="New user? Create your account ",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
signup_lbl.place(x=70, y=310)
signup_btn = tk.Button(frame,cursor='hand2',width=4,border=0,text="here",fg='#3d85c6',bg='white',font=('Microsoft YaHei UI Light',9,'bold'))
signup_btn.place(x=250, y=310)





root.mainloop()
