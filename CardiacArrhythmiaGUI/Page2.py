from Tkinter import *
def page2():
    content =[]
    import VFI_single
    import KNN_single
    def gettext():
        print 'Correct till here 3'
        global content
        content1 = entry.get()
        content = list(content1.split('\t'))
        content = [float(x) for x in content]
        vfi1 = VFI_single.vfi(content)
        vfi1 = 'The predicted class by VFI1 is: '+str(vfi1)
        print vfi1
        knn = KNN_single.knn(content)
        knn = 'The predicted class by KNN is: '+str(knn)
        label2.config(text=vfi1)
        label3.config(text=knn)

    master = Tk()
    label1 = Label(master, text="Enter the data:", height=7, width=50)
    label1.place(x=500, y=100)
    label2 = Label(master, text='ok', height=7, width=50)
    label2.place(x=500, y=300)
    label3 = Label(master, text='ok', height=7, width=50)
    label3.place(x=500, y=400)
    entry = Entry(master, width=200)
    entry.place(x=50, y = 200)
    button1 = Button(master, text="Done",command = gettext,height=2, width=50)
    button1.place(x=500, y=250)
    w, h = master.winfo_screenwidth(), master.winfo_screenheight()
    master.geometry("%dx%d+0+0" % (w, h))
