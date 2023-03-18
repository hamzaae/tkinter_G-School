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

frame = tk.Frame(root, width=340, height=405,)
frame.place(x=360)

head = tk.Label(frame,text='ENSAH G-SCHOOL LOGIN',font="Times 15 italic bold")
head.place(x=80,y=35)

# Show logo
logo = tk.PhotoImage(file="logo-ensah_50x50.png")
img_logo = tk.Label(frame, image=logo)
img_logo.place(x=10, y=20)




'''l1 = tk.Label(root, text="Login name:", fg="black", bg="white")
l2 = tk.Label(root, text="Password:", fg="black", bg="white")
l1.grid(row=0, column=1)
l2.grid(row=1, column=1)'''





root.mainloop()
