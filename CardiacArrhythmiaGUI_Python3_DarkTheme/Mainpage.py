from tkinter import *

master = Tk()
master.title("MAINPAGE")
import User_Interface as ofnew
import Page2 as p2
def askOffsets():
    print('Correct till here')
    of = ofnew.ui()
def callpage2():
    print('Correct till here2')
    of = p2.page2()
button1 = Button(master, text="Check type of arrhythmia",font=("Helvetica", 14),  background='white',command = callpage2, height=2, width=50)
button1.place(x=420, y=300)

button2 = Button(master, text="Check accuracies of algorithms", background='white', font=("Helvetica", 14),command = askOffsets, height=2, width=50)
button2.place(x=420, y=400)

label1 = Label(master, text="CLASSIFICATION OF CARDIAC ARRHYTHMIA",font=("Helvetica", 20),background='black',foreground='white', height=7, width=50)
label1.place(x=300, y=50)
w, h = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (w, h))
master.configure(background='black')
mainloop()
