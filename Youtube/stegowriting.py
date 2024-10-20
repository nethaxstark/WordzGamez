from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
import webbrowser



#creating a main tkinter frame
window = tk.Tk()

#seting the window size to full screen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Stegowriting - Hide a Msg In An Image!")
window.resizable(YES, YES)
window.configure(bg="#000000")

#Load the background image
backgroundimage = PhotoImage(file="")
Label(window, image=backgroundimage, bg="#0000FF").place(x=0, y=0)

#Resize the background image
smaller_image = backgroundimage.subsample(2, 2)

#Function to show the selected image
def showimage():
    global filename # Declare filename as a global variable.
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image',
                                          filetypes=(("Png File", "*.png"),
                                                     ("JPG File", "*.jpg"), ("All File", "*.txt")))

    img = Image.open(filename)
    img.thumbnail((500, 300))

    img = ImageTk.PhotoImage(img)

#Label to display the image in the area you want
    lbl_image.configure(image=img)
    lbl_image.image = img

#function to hide the data in the image

def hide():
    global filename, secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

#function to retreve the data from the image
    
def show():
    global filename
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

#function to save the hidden image
    
def save():
    global secret
    secret.save("Hidden.png")  #The image will be saved by name of hidden.png

#function for About Me!
    
def aboutme():
    global aboutdev
    messagebox.showinfo('About Me!','I am a program developed by Ajay Kumar Chaudhary. I can hide text into the images and can also show the text hidden into the images. I am a college project on StegnoGraphy!')

#Function for the social media links
    
def sociallinks():
    url = "https://wwww.instagram.com/ajay_01.xx/"
    webbrowser.open_new_tab(url)

#You can give other links also

#Label text for the background image

Label(window, text="Stegowriting", bg="#000000", fg="white", font="courier 25 bold").place(x=565, y=40)
Label(window, text="Image Here!", bg="#000000", fg="white", font="courier 25 bold").place(x=250, y=100)
Label(window, text="Msg Here!", bg="#000000", fg="white", font="courier 25 bold").place(x=1000, y=100)

f = Frame(window, bd=3, width=500,height=300, relief=GROOVE)
f.place(x=70, y=140)

lbl_image = Label(f, bg="white",width=400)
lbl_image.place(x=40, y=10)

#The right box frame second

f2=Frame(window,bd=3,width=500,height=300,relief=GROOVE,bg="white")
f2.place(x=800,y=140)

lbl=Label(f,bg="black")
lbl.place(x=210, y=400)

text1=Text(f2,font="courier 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=800,height=200)

#creating the slidebar

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=800,y=0,height=280)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#creating third frame
f3=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f3.place(x=70,y=570)

Button(f3,text="Open Image",width=10,height=2, font="courier 14 bold",command=showimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2, font="courier 14 bold",command=save).place(x=360,y=30)
Label(f3,text="Any Image Format!",font="courier",bg="#2f4155",fg="yellow").place(x=165,y=20)

#Creating the fourth frame

f4=Frame(window,bd=3,bg="#0000ff",width=500,height=100,relief=GROOVE)
f4.place(x=800,y=570)

Button(f4,text="Hide Data",width=10,height=2, font="courier 14 bold",command=hide).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2, font="courier 14 bold",command=show).place(x=360,y=30)
Label(f4,text="Any Image Format!",font="courier",bg="#2f4155",fg="yellow").place(x=165,y=20)

# Now extra Features Will be added at night!

#window.config(menu = menubar)
window.mainloop()






