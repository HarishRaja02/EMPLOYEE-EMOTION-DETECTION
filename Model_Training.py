import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# ------------------------ Load Model ------------------------
emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))

# Load weights
try:
    emotion_model.load_weights('emotion_model.h5')
except:
    print("Error loading model weights. Please check the file path.")
    exit()

# ------------------------ Emotion Mapping ------------------------
emotion_dict = {
    0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ",
    3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"
}

emoji_dist = {
    0: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/angry.png",
    1: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/disgusted.png",
    2: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/fearful.png",
    3: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/happy.png",
    4: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/neutral.png",
    5: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/sad.png",
    6: "H:/MINI PROJECTS/emoji-creator-project-code/emojis/emojis/surprised.png"
}

# ------------------------ Globals ------------------------
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
show_text = [0]
cap1 = cv2.VideoCapture(0)

# ------------------------ Video Function ------------------------
def show_vid():
    if not cap1.isOpened():
        print("Camera not found.")
        return
    
    ret, frame1 = cap1.read()
    if not ret:
        return

    frame1 = cv2.resize(frame1, (600, 500))
    gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y-50), (x + w, y + h + 10), (255, 0, 0), 2)
        roi_gray = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = emotion_model.predict(cropped_img)
        show_text[0] = int(np.argmax(prediction))

    global last_frame1
    last_frame1 = frame1.copy()
    pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, show_vid)  # update every 100ms

# ------------------------ Emoji Function ------------------------
def show_vid2():
    try:
        emoji_path = emoji_dist.get(show_text[0], "")
        emoji_img = cv2.imread(emoji_path)
        if emoji_img is None:
            raise Exception("Emoji image not found.")

        pic2 = cv2.cvtColor(emoji_img, cv2.COLOR_BGR2RGB)
        img2 = Image.fromarray(pic2)
        imgtk2 = ImageTk.PhotoImage(image=img2)

        lmain2.imgtk2 = imgtk2
        lmain2.configure(image=imgtk2)
        lmain3.configure(text=emotion_dict[show_text[0]], font=('arial', 45, 'bold'))
    except Exception as e:
        print(f"Error in show_vid2: {e}")

    lmain2.after(100, show_vid2)  # update every 100ms

# ------------------------ On Close ------------------------
def on_closing():
    cap1.release()
    root.destroy()

# ------------------------ GUI ------------------------
root = tk.Tk()
root.title("Photo To Emoji")
root.geometry("1400x900+100+10")
root.configure(bg='black')

try:
    header_img = ImageTk.PhotoImage(Image.open("H:/MINI PROJECTS/emoji-creator-project-code/images.jpg"))
    heading = Label(root, image=header_img, bg='black')
    heading.pack()
except:
    print("Header image not found.")
    heading = Label(root, text="Emoji App", bg='black', fg='white', font=('arial', 30, 'bold'))
    heading.pack()

heading2 = Label(root, text="Photo to Emoji", pady=20, font=('arial', 45, 'bold'), bg='black', fg='#CDCDCD')
heading2.pack()

lmain = Label(root, padx=50, bd=10)
lmain2 = Label(root, bd=10)
lmain3 = Label(root, bd=10, fg="#CDCDCD", bg='black')

lmain.place(x=50, y=250)
lmain2.place(x=900, y=350)
lmain3.place(x=960, y=250)

Button(root, text='Quit', fg="red", command=on_closing, font=('arial', 25, 'bold')).pack(side=BOTTOM)

# Start
show_vid()
show_vid2()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
