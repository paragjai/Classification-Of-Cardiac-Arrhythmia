from tkinter import *
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




import tkinter as tk
	
def ui():

    def naive_bayes():
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

        mainloop()


    def t(i):
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

        mainloop()
    
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    Example(root).pack(side="top", fill="both", expand=True)
    root.configure(background='black')
    root.mainloop()
    
	
# ************************
# Scrollable Frame Class
# ************************
class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background="black")                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.


# ********************************
# Example usage of the above class
# ********************************

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
        
        # Now add some controls to the scrollframe. 
        # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
        
			
        label1 = Label(self.scrollFrame.viewPort, text="CHOOSE THE ALGORITHM", font=("Helvetica", 18),background='black',foreground='white',  height=2, width=50).grid(row=1, column=0)
		
        button1 = Button(self.scrollFrame.viewPort, text="NAIVE BAYES", font=("Helvetica", 12),background='white',foreground='black', command=lambda :nb.naive_bayes(False), height=2, width=40).grid(row=2, column=0)
		
        button2 = Button(self.scrollFrame.viewPort, text="K NEAREST NEIGHBOUR", font=("Helvetica", 12),background='white',foreground='black',command=lambda :knn.knn(False), height=2, width=40).grid(row=3, column=0)
		
        button3 = Button(self.scrollFrame.viewPort, text="SUPPORT VECTOR MACHINE",font=("Helvetica", 12),background='white',foreground='black', command=lambda :svm.svm(False), height=2, width=40).grid(row=4, column=0)

        button4 = Button(self.scrollFrame.viewPort, text="DECISION TREES", font=("Helvetica", 12),background='white',foreground='black',command=lambda :dt.decision_tree(False), height=2, width=40).grid(row=5, column=0)

        button5 = Button(self.scrollFrame.viewPort, text="VOTING FEATURE INTERVAL", font=("Helvetica", 12),background='white',foreground='black',command=lambda :vfi1.vfi(False), height=2, width=40).grid(row=6, column=0)

        button6 = Button(self.scrollFrame.viewPort, text="VOTING FEATURE INTERVAL 2",font=("Helvetica", 12),background='white',foreground='black', command=lambda :vfi2.vfi(False), height=2, width=40).grid(row=7, column=0)

        button7 = Button(self.scrollFrame.viewPort, text="VOTING FEATURE INTERVAL 3", font=("Helvetica", 12),background='white',foreground='black',command=lambda :vfi3.vfi(False), height=2, width=40).grid(row=8, column=0)

        button8 = Button(self.scrollFrame.viewPort, text="VOTING FEATURE INTERVAL 4", font=("Helvetica", 12),background='white',foreground='black',command=lambda :vfi4.vfi(False), height=2, width=40).grid(row=9, column=0)

        button9 = Button(self.scrollFrame.viewPort, text="VOTING FEATURE INTERVAL 5", font=("Helvetica", 12),background='white',foreground='black',command=lambda :vfi5.vfi(False), height=2, width=40).grid(row=10, column=0)

        button10 = Button(self.scrollFrame.viewPort, text="LDA",font=("Helvetica", 12),background='white',foreground='black', command=lambda :lda.lda_main(), height=2, width=40).grid(row=11, column=0)
	
    
		
        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
    
    def printMsg(self, msg):
        print(msg)

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    Example(root).pack(side="top", fill="both", expand=True)
    root.configure(background='black')
    root.mainloop()

