from Tkinter import *
from PIL import ImageTk, Image
import Naive_CV as nb
import KNN_CV as knn
import SVM_CV as svm
import Decision_Trees_CV as dt
import VFI_Median_cross_valid as vfi1
import VFI2_Median_cross_valid as vfi2
import VFI3_Median_cross_valid as vfi3
import VFI4_Median_cross_valid as vfi4
import VFI5_Median_cross_valid as vfi5
import LDA_crossvalid as lda

'''def naive_bayes():
    print("Naive Bayes")
    child = Tk()
    child.title("NB")

    label1 = Label(child, text="FOLD1:", fg="red")
    label2 = Label(child, text="48%")
    label3 = Label(child, text="FOLD2:", fg="red")
    label4 = Label(child, text="50%")
    label5 = Label(child, text="FOLD3:", fg="red")
    label6 = Label(child, text="52%")
    label1.place(x=60, y=50)
    label2.place(x=120, y=50)
    label3.place(x=60, y=70)
    label4.place(x=120, y=70)
    label5.place(x=60, y=90)
    label6.place(x=120, y=90)

    mainloop()'''


'''def t(i):
    print(i)
    
def svm():
    child = Tk()
    child.title("SVM Accuracy")
    l = []
    x_pos=60
    y_pos=50
    for i in range(10):
        l.append(Button(child, text="Fold "+str(i+1), command=lambda: t(i+1)))
        l[i].place(x=x_pos,y=y_pos)
        y_pos = y_pos+20

    mainloop()'''

master = Tk()
master.title("Cardiac Arrhythmia")
path = "C:\Users\Parag Jain\Desktop\Capture1.PNG"

img = ImageTk.PhotoImage(Image.open(path))
l = Label(master, image = img)
l.place(x=1000, y=50)

path1 = "C:\Python27\CardiacArrhythmia\MicrosoftLogo.PNG"

img = ImageTk.PhotoImage(Image.open(path1))
l2 = Label(master, image = img)
l2.place(x=1300, y=20)


button1 = Button(master, text="Naive Bayes", command=nb.naive_bayes, height=2, width=10)
button1.place(x=50, y=50)

button2 = Button(master, text="KNN", command=knn.knn, height=2, width=10)
button2.place(x=50, y=100)

button3 = Button(master, text="SVM", command=svm.svm, height=2, width=10)
button3.place(x=50, y=150)

button3 = Button(master, text="Decision Tree", command=dt.decision_tree, height=2, width=10)
button3.place(x=50, y=200)

button4 = Button(master, text="VFI", command=vfi1.vfi, height=2, width=10)
button4.place(x=50, y=250)

button5 = Button(master, text="VFI2", command=vfi2.vfi, height=2, width=10)
button5.place(x=50, y=300)

button6 = Button(master, text="VFI3", command=vfi3.vfi, height=2, width=10)
button6.place(x=50, y=350)

button7 = Button(master, text="VFI4", command=vfi4.vfi, height=2, width=10)
button7.place(x=50, y=400)

button8 = Button(master, text="VFI5", command=vfi5.vfi, height=2, width=10)
button8.place(x=50, y=450)

button8 = Button(master, text="LDA", command=lda.lda_main, height=2, width=10)
button8.place(x=50, y=500)


master.geometry("800x800")

mainloop()
