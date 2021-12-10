print('Loading...')
from tkinter import *
from tkinter import filedialog
import operator

import VFI_single
import KNN_single
import SVM_single
import Naive_single
import VFI5_single
import VFI4_single
import VFI3_single
import VFI2_single
import DT_single
import LDA_single
from collections import OrderedDict
from operator import itemgetter

def Arrhythmia(num):
    if(num==1):
        return 'Normal'
    elif(num==2):
        return 'Coronary Artery Disease'
    elif(num==3):
        return 'Old Anterior Myocardial Infarction'
    elif(num==4):
        return 'Old Inferior Myocardial Infarction'
    elif(num==5):
        return 'Sinus tachycardy'
    elif(num==6):
        return 'Sinus bradycardy'
    elif(num==7):
        return 'Ventricular Premature Contraction (PVC)'
    elif(num==8):
        return 'Supraventricular Premature Contraction'
    elif(num==9):
        return 'Left bundle branch block'
    elif(num==10):
        return 'Right bundle branch block'
    elif(num==11):
        return '1. degree AtrioVentricular block'
    elif(num==12):
        return '2. degree AtrioVentricular block'
    elif(num==13):
        return '3. degree AtrioVentricular block'
    elif(num==14):
        return 'Left ventricule hypertrophy'
    elif(num==15):
        return 'Atrial Fibrillation or Flutter'
    elif(num==16):
        return 'Others'


def page2():
    content=[]
    entry = Entry()

    def gettext():
        def predict():
            pred =[]
            print('Correct till here 3')
            global content
            global entry
            content1 = entry.get()
            content = list(content1.split('\t'))
            content = [float(x) for x in content]
            vfi1 = Arrhythmia(VFI_single.vfi(content)) # Passing the prediction integer label and returning corresponding string value
            pred.append(vfi1)
            vfi1 = 'The class predicted by VFI1 is: '+ (vfi1)
            print(vfi1)
            knn = Arrhythmia(KNN_single.knn(content))
            pred.append(knn)
            knn = 'The class predicted by KNN is: '+(knn)
            svm = Arrhythmia(SVM_single.svm(content))
            pred.append(svm)
            svm = 'The class predicted by by SVM is: '+ (svm)
            nb = Arrhythmia(Naive_single.nb(content))
            pred.append(nb)
            nb = 'The class predicted by Naive Bayes is: '+ (nb)
            Vfi5 = Arrhythmia(VFI5_single.vfi5(content))
            pred.append(Vfi5)
            Vfi5 = 'The class predicted by VFI5 is: '+ (Vfi5)
            dt = Arrhythmia(DT_single.Dt(content))
            pred.append(dt)
            dt = 'The class predicted by Decision Tree is: '+ (dt)
            Vfi2 = Arrhythmia(VFI2_single.vfi2(content))
            pred.append(Vfi2)
            Vfi2 = 'The class predicted by VFI2 is: '+ (Vfi2)
            Vfi3 = Arrhythmia(VFI3_single.vfi3(content))
            pred.append(Vfi3)
            Vfi3 = 'The class predicted by VFI3 is: '+ (Vfi3)
            Vfi4 = Arrhythmia(VFI4_single.vfi4(content))
            pred.append(Vfi4)
            Vfi4 = 'The class predicted by VFI4 is: '+(Vfi4)
            Lda = Arrhythmia(LDA_single.lda(content))
            pred.append(Lda)
            Lda = 'The class predicted by LDA is: '+(Lda)
            label3.config(text=vfi1)
            label6.config(text=knn)
            label4.config(text=svm)
            label2.config(text=nb)
            label10.config(text=Vfi5)
            label5.config(text=dt)
            label7.config(text=Vfi2)
            label8.config(text=Vfi3)
            label9.config(text=Vfi4)
            label11.config(text=Lda)
            count={}
            for i in range(len(pred)):
                if(i not in count.keys()):
                    count.update({pred[i]:pred.count(pred[i])})
            print(count)
            m = max(count.items(), key=operator.itemgetter(1))[0]
            message = 'FINAL RESULT: ' + m
            label12.config(text=message)

        child = Tk()
        global entry
        label1 = Label(child, text="Enter the data in tab seperated format:",font=("Helvetica", 20),background='black',foreground='white', height=7, width=50)
        label1.place(x=300, y=50)
        label2 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label2.place(x=550, y=325)
        label3 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label3.place(x=550, y=425)
        label4 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label4.place(x=550, y=350)
        label5 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label5.place(x=550, y=375)
        label6 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label6.place(x=550, y=400)
        label7 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label7.place(x=550, y=450)
        label8 = Label(child, text='', font=("Helvetica", 8),background='black',foreground='white',height=2, width=70)
        label8.place(x=550, y=475)
        label9 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label9.place(x=550, y=500)
        label10 = Label(child, text='',font=("Helvetica", 8),background='black',foreground='white', height=2, width=70)
        label10.place(x=550, y=525)
        label11 = Label(child, text='', font=("Helvetica", 8),background='black',foreground='white',height=2, width=70)
        label11.place(x=550, y=550)
        label12 = Label(child, text='',font=("Helvetica", 12),background='black',foreground='white', height=2, width=70)
        label12.place(x=470, y=625)
        entry = Entry(child, width=200)
        entry.place(x=50, y = 200)
        button1 = Button(child, text="SHOW RESULT",font=("Helvetica", 14),background='white',foreground='black',command = predict,height=2, width=20)
        button1.place(x=575, y=250)
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        child.title('MANUALLY ENTER DATA')
        child.geometry("%dx%d+0+0" % (w, h))
        child.configure(background='black')
        mainloop()

    def upload():
        def upload_bunch():
            def find():
                nm=entry.get()
                nm = nm.lower()
                f=0
                start = '1.0'
                T=''
                while 1:
                    pos = text1.search(nm, start, stopindex=END)
                    if not pos:
                        if(f==0):
                            LabelRes.config(text='Name not found')
                        break
                    print(pos)
                    f=1
                    x,z=pos.split('.')
                    print(x)
                    print(z)
                    #z=float(z)+len(y)
                    z=str(z)
                    if(float(z)==0):
                        epos = '.'.join((x,'end'))
                        print(epos)
                        '''print type(pos)
                        epos=str(float(pos)+(0.1*len(y)))
                        print epos'''
                        T=text1.get(pos,epos)
                        LabelRes.config(text=T)
                        '''text.tag_add("epos", pos, epos)
                        text.tag_config("epos", background="blue", foreground="white")'''
                    start = pos +"+1c"

            fileName = filedialog.askopenfilename(parent=master)
            print(fileName, type(fileName))
            record = open(fileName, 'r')
            Message=''
            child=Tk()
            child.title("RESULTS FOR BUNCH UPLOAD")
            scrollbar = Scrollbar(child)
            #scrollbar.pack(side=RIGHT, fill=Y)
            w, h = master.winfo_screenwidth(), master.winfo_screenheight()
            child.geometry("%dx%d+0+0" % (w, h))
            child.configure(background = 'black')
            label2=Label(child,text='RESULTS', bg='black' ,font=("Helvetica", 20), fg ='white',width=50, height=2)
            label2.place(x=300,y=10)
            entry = Entry(child, width=20)
            entry.place(x=460, y = 90)
            button = Button(child,text='Search Name',bg='white' ,font=("Helvetica", 10), fg ='black',command = find)
            button.place(x=600, y=90)
            LabelRes= Label(child,text='', bg='black' ,font=("Helvetica", 10), fg ='white',width=50, height=2, anchor=W)
            LabelRes.place(x=730,y=80)
            text1=Text(child, bg='azure3' ,font=("Helvetica", 10), fg ='black',width=55,height = 30, yscrollcommand=scrollbar.set)
            text1.place(x=450,y=125)
            label1=Label(child,text = 'ok', bg='black' ,font=("Helvetica", 10), fg ='white',width=170,height=5, anchor = W ,wraplength=child.winfo_screenwidth())
            label1.place(x=5,y=600)
            l=[]
            c=0
            tot=0
            instanceNo=0
            totCorrect=0
            Resultcount = {'Normal':0,'Coronary Artery Disease':0,'Old Anterior Myocardial Infarction':0,'Old Inferior Myocardial Infarction':0, 'Sinus tachycardy':0,'Sinus bradycardy':0,'Ventricular Premature Contraction (PVC)':0,'Supraventricular Premature Contraction':0,'Left bundle branch block':0,'Right bundle branch block':0,'1. degree AtrioVentricular block':0, '2. degree AtrioVentricular block':0,'3. degree AtrioVentricular block':0,'Left ventricule hypertrophy':0,'Atrial Fibrillation or Flutter':0, 'Others':0}
            text1.insert(INSERT, '\t\tALL RESULTS\n')
            while(fileName):
                print("fileName: ", fileName)
                print("Instance number : ", instanceNo)
                content= list(record.readline().split("\t"))
                print(content)
                print("--- content length 0 : ", len(content))
                nm = content[0]
                nm=nm.lower()
                '''if(nm!=''):
                    del content[0]'''
                content[-1]=str(content[-1]).strip('\\n')
                #print content
                if(content[-1]!=''):
                    instanceNo+=1
                    cl=float(content[-1]) # True Float Label 
                    print("True float lable: ", cl)
                    print("True string lable: ", Arrhythmia(int(cl)))
                else:
                    print("Reached the end of file. Breaking out")
                    break
                del content[-1]
                #print content
                #print'here2'
                if(content ==[]):
                    break
                if(content[0] == ''):
                    break
                content = [float(x) for x in content]
                print("--- content length : --- ", len(content))
                pred=[]
                vfi1 = Arrhythmia(VFI_single.vfi(content))
                pred.append(vfi1)
                #print vfi1
                knn = Arrhythmia(KNN_single.knn(content)) # Passing predicted integer label here.
                pred.append(knn) # Prediction from KNN. Here it is a string.
                knn = 'The class predicted by KNN is: '+(knn)
                print(knn)
                svm = Arrhythmia(SVM_single.svm(content))
                pred.append(svm)
                svm = 'The class predicted by by SVM is: '+ (svm)
                print(svm)
                nb = Arrhythmia(Naive_single.nb(content))
                pred.append(nb)
                nb = 'The class predicted by Naive Bayes is: '+ (nb)
                print(nb)
                Vfi5 = Arrhythmia(VFI5_single.vfi5(content))
                pred.append(Vfi5)
                Vfi5 = 'The class predicted by VFI5 is: '+ (Vfi5)
                dt = Arrhythmia(DT_single.Dt(content))
                pred.append(dt)
                dt = 'The class predicted by Decision Tree is: '+ (dt)
                Vfi2 = Arrhythmia(VFI2_single.vfi2(content))
                pred.append(Vfi2)
                Vfi2 = 'The class predicted by VFI2 is: '+ (Vfi2)
                Vfi3 = Arrhythmia(VFI3_single.vfi3(content))
                pred.append(Vfi3)
                Vfi3 = 'The class predicted by VFI3 is: '+ (Vfi3)
                Vfi4 = Arrhythmia(VFI4_single.vfi4(content))
                pred.append(Vfi4)
                Vfi4 = 'The class predicted by VFI4 is: '+(Vfi4)
                Lda = Arrhythmia(LDA_single.lda(content))
                pred.append(Lda)
                Lda = 'The patients predicted by LDA is: '+(Lda)
                print(Lda)
                count = {}
                for i in range(len(pred)): #Going through the string predictions for each of the algorithms
                    if(i not in count.keys()): # count is a key value pair with key being an integer
                            count.update({pred[i]:pred.count(pred[i])})
                    print("count : ", count)
                    m = max(count.items(), key=operator.itemgetter(1))[0] # Predicted String Label
                    '''if(m == 'Normal'):
                        message= 'CONGRATULATIONS! YOU ARE NORMAL'
                    elif(m=='Others'):
                        message= 'INCONCLUSIVE'
                    else:
                        message= 'You are suffering from ' + (m)'''
                print(m)
                Resultcount[m]+=1
                #print cl
                trueStringLabel = Arrhythmia(int(cl))
                if(trueStringLabel == m):
                    print("True label and predicted labels are same. It is " + m)
                    totCorrect+=1
                else:
                    print("True label(",trueStringLabel,") is not same as predicted label(",m,")")
                '''z= Arrhythmia(int(cl))
                print z
                if(m==z):
                    c+=1
                    #print c,'OUT OF',i
                tot+=1'''
                Message = nm+' : '+ m+'\n\n'
                text1.insert(INSERT, Message)
            print(Message)
            print("Number of correct classifications by ensemble approach: ", totCorrect,"/",instanceNo)
            #text.insert(END, "")
            #print float(c)/float(tot)
            #label1.config(text=Message)
            R = OrderedDict(sorted(Resultcount.items(), key=itemgetter(1),reverse=True))
            for i in R.keys():
                tot = tot + R[i]
            Res='NUMBER OF PATIENTS IN EACH CLASS IN THE UPLOADED FILE\nTotal: ' + str(tot) + '\n'
            for i in R.keys():
                Res+= i + ' : ' + str(R[i])+'   '
            label1.config(text=Res)
            text1.bind("<Key>", lambda e: "break")
            mainloop()
			
        upload_bunch()
        '''child2=Tk()
        child2.title("UPLOAD")
        child2.configure(background='black')
        label = Label(child2, text="CHOOSE MODE", font=("Helvetica", 20),background='black',foreground='white',height=3, width=50)
        label.place(x=300, y=100)
        button1 = Button(child2, text="Search from a file by patient name", font=("Helvetica", 12),background='white',command = upload_byname,foreground='black',height=2, width=50)
        button1.place(x=500, y=300)
        button2 = Button(child2, text="Upload and classify for full file",  font=("Helvetica", 12),background='white',foreground='black',command = upload_bunch, height=2, width=50)
        button2.place(x=500, y=400)
        w, h = child2.winfo_screenwidth(), master.winfo_screenheight()
        child2.geometry("%dx%d+0+0" % (w, h))
        mainloop()'''

    

    master = Tk()
    master.title("CHECK TYPE OF ARRHYTHMIA FOR SINGLE PATIENT")
    master.configure(background='black')
    label = Label(master, text="CHOOSE MODE", font=("Helvetica", 20),background='black',foreground='white',height=3, width=50)
    label.place(x=300, y=100)
    button1 = Button(master, text="Manually enter data", font=("Helvetica", 14),background='white',foreground='black',command = gettext,height=2, width=50)
    button1.place(x=420, y=300)
    button2 = Button(master, text="Upload",  font=("Helvetica", 14),background='white',foreground='black',command = upload, height=2, width=50)
    button2.place(x=420, y=400)
    w, h = master.winfo_screenwidth(), master.winfo_screenheight()
    master.geometry("%dx%d+0+0" % (w, h))
    mainloop()
