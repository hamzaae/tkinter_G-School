import tkinter
import os.path
import datetime
import subprocess
import cv2
import mysql.connector
from PIL import Image, ImageTk
import login
import util
import home
from tkinter import messagebox


class App_face:
    def __init__(self):
        # DB connection
        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="g_school"
        )
        self.mycursor = self.mydb.cursor()


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

    def login(self):
        unkown_img= './tmp.jpg'
        cv2.imwrite(unkown_img, self.most_recent_capture_arr)
        output = str(subprocess.check_output(['face_recognition',self.db_dir,unkown_img]))
        name = output.split(',')[1].replace('\\r\\n\'','')

        if name in ['unknown_person','no_persons_found']:
            util.msg_box('Ups...','Unknown user')
        else:
            self.end_video()
            util.msg_box('welcome',f'hello {name}')
            self.mycursor.execute("SELECT * FROM users WHERE username = %s",
                                  (name,))
            login.Login.current_user = self.mycursor.fetchone()
            if login.Login.current_user == None:
                messagebox.showerror('Error', 'Invalid Username or Password!')
            else:
                with open(login.Login.log_path, 'a') as f:
                    f.write('{}{}{}\n'.format(login.Login.current_user[1], " logged in using face signin at ",
                                              datetime.datetime.now()))
                    f.close()
                login.Login.root.destroy()
                main_home = home.Home()
                main_home.start()
        os.remove(unkown_img)


    def end_video(self):
        if 'cap' in self.__dict__:
            self.cap.release()
            cv2.destroyAllWindows()
            self._label.destroy()
            del self.__dict__["cap"]

    def register_new_user(self,window,btn):
        self.submit_button_register_new_user_window = tkinter.Button(window,
                        text='Submit', bg='blue', width=20,
                        command=lambda: self.accept_register_new_user(window))
        self.submit_button_register_new_user_window.place(x=450, y=300)
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(1)
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        self.capture_label = util.get_img_label(window)
        self.capture_label.place(x=0, y=0, width=450, height=520)
        self.add_img_to_label(self.capture_label)
        btn.configure(text="Try again")

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self, window, x, y):
        self.webcam_label = util.get_img_label(window)
        self.webcam_label.place(x=0, width=x, height=y)

        self.add_webcam(self.webcam_label)
        window.mainloop()

    def accept_register_new_user(self,window):

        name = login.Login.current_user[1]
        cv2.imwrite(os.path.join(self.db_dir,f'{name}.jpg'),self.register_new_user_capture)

        util.msg_box('Success!', 'User was registered successfully !')
        self.end_video()
        window.destroy()

