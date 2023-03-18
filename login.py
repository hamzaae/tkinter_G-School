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

head = tk.Label(frame,text='ENSAH G-SCHOOL LOGIN',font="Times 15 italic bold",bg='white')
head.place(x=75,y=45)

# Show logo
logo = tk.PhotoImage(file="logo-ensah_50x50.png")
img_logo = tk.Label(frame, image=logo,bg='white')
img_logo.place(x=10, y=30)

#
user = tk.Entry(frame, width= 25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
user.place(x=30, y=120)
user.insert(0,'Username')

pswrd = tk.Entry(frame, width= 25, fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',18,'bold'))
pswrd.place(x=30, y=190)
pswrd.insert(0,'Password')

tk.Frame(frame,width=295, height=2,bg='black').place(x=25,y=157)
tk.Frame(frame,width=295, height=2,bg='black').place(x=25,y=227)







root.mainloop()
