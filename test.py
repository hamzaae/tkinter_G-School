from tkinter import *
import cv2
from PIL import Image, ImageTk

def on_facesignin():
    signin_face_btn.configure(text="Say cheese")
    cap = cv2.VideoCapture(1)
    cv2.namedWindow('camera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('camera', 640, 480)

    # Create a canvas to display the video
    canvas = Canvas(root, width=640, height=480)
    canvas.pack()

    while (True):
        ret, frame = cap.read()
        if ret:
            # Convert the frame to an Image object
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)

            # Convert the Image object to a PhotoImage object
            imgtk = ImageTk.PhotoImage(image=img)

            # Use the canvas as a display for the video frames
            canvas.create_image(0, 0, image=imgtk, anchor=NW)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

root = Tk()
root.title("Face Sign In")

signin_face_btn = Button(root, text="Sign In with Face", command=on_facesignin)
signin_face_btn.pack()

root.mainloop()
