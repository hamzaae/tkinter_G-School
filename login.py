import tkinter
import tkinter as tk
import webbrowser
import cv2
from PIL import Image,ImageTk
import util

class App:
    def __init__(self,window):
        self.webcam_label = util.get_img_label(window)
        self.webcam_label.place(x=0, width=365, height=405)
        self.add_webcam(self.webcam_label)
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(1)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def start(self,w):
        w.mainloop()

access = True
# Create the window
root = tk.Tk()
root.title('G-School LOGIN')
root.geometry('700x402')
root.resizable(False, False)

# Add image and frame
bg = tk.PhotoImage(file="media\\slide.png")
img = tk.Label(root, image=bg)
img.place(x=-360, y=0)

frame = tk.Frame(root, width=340, height=405, bg='white')
frame.place(x=360)

# Show logo and heading
head = tk.Label(frame, text='ENSAH G-SCHOOL LOGIN', font=("Helvetica", 16, 'bold'), bg='white')
head.place(x=68, y=45)

logo = tk.PhotoImage(file="media\\logo-ensah_50x50.png")
img_logo = tk.Label(frame, image=logo, bg='white')
img_logo.place(x=8, y=30)


### Username Input behavior
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, 'Username')


def validate_input(new_value):
    if len(new_value) > 15:
        return False
    else:
        return True


vcmd = (root.register(validate_input), '%P')

# Add inputs and ligne decorator
user = tk.Entry(frame, width=25, fg='black', border=0, bg='white',
                font=('Microsoft YaHei UI Light', 18, 'bold'), validate="key", validatecommand=vcmd)
user.place(x=30, y=130)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


### Password Input behavior
def on_enter(e):
    pswrd.delete(0, 'end')


def on_leave(e):
    name = pswrd.get()
    if name == "":
        pswrd.insert(0, 'Password')


pswrd = tk.Entry(frame, width=25, fg='black', border=0, bg='white', validate="key", validatecommand=vcmd,
                 font=('Microsoft YaHei UI Light', 18, 'bold'),show='*')
pswrd.place(x=30, y=200)
pswrd.insert(0, 'Password')
pswrd.bind('<FocusIn>', on_enter)
pswrd.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=167)
tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=237)


def show_and_hide():
    if pswrd['show'] == '*':
        pswrd['show'] = ''
    else:
        pswrd['show'] = '*'


checkBox_showPassword = tkinter.Button(frame, text="👁", bg='white',borderwidth=0,
                                    font=('verdana', 14), command=show_and_hide)
checkBox_showPassword.place(x=280,y=195)

### sign_in behavior
def on_signin():
    username = user.get()
    password = pswrd.get()
    if access:
        pass
    elif ():
        pass
    else:
        pass

def on_face_sign():
    signin_face_btn.configure(text='say cheese')
    app = App(root)
    app.start(root)



# Sign in and sign up buttons
signin_btn = tk.Button(frame, width=39, pady=7, text='Sign in', bg='#6cc570', fg='white', border=0, command=on_signin)
signin_btn.place(x=35, y=270)
signin_face_btn = tk.Button(frame, width=39, pady=7, text='Face Sign in', bg='#5271ff', fg='white', border=0,command=on_face_sign)
signin_face_btn.place(x=35, y=315)
camera_label = tkinter.Label(root)
camera_label.place(x=0)



signup_lbl = tk.Label(frame, text="Visit our site to know more About! ", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 11))
signup_lbl.place(x=65, y=350)

# Define a callback function
def callback(url):
    webbrowser.open_new_tab(url)

# Create a Label to display the link
link = tk.Label(frame, text="https://ensah.ma/", font=('Helveticabold', 10), fg="blue",bg="white",
                cursor="hand2")
link.place(x=120, y=375)
link.bind("<Button-1>", lambda e: callback("https://ensah.ma/"))



root.mainloop()
