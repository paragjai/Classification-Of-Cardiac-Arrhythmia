import numpy as np
import scipy
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
from tkinter import *

def decision_tree(areAllAlgorithmExecuted):
    text_file = open("data_2.txt", "r")
    child = Tk()
    child.title("Decision Tree Accuracy")
    child.geometry("300x300")
    child.configure(background='black')
    x=0
    L=[]
    K=[]
    offset = 0
    k = 10
    test_data_end=420
    new_data = 420
    test_size = int(test_data_end/k)
    X = []
    Y = []
    i = 0
    j = 0
    Z = []
    c = 163
    q = 0
    t = 0
    sum1 = 0
    extra = test_data_end%k
    pos_x=60
    pos_y=50
    while(x<test_data_end):
        L.append(list(text_file.readline().split("\t")))
        x=x+1
    text_file.close()
    for i in range(len(L)):
        L[i]=[float(x) for x in L[i]]
    random.shuffle(L)
    for n in range(extra):
        np.delete(L,new_data,0)
        new_data = new_data-1
    for offset in range(0,new_data,test_size):
        X = L[:new_data+1]
        Z = []
        K = []
        q = 0
        j = 0
        Y = []
        while(j<new_data):
            Y.append(L[j][c]) ##Selecting the Training Label set
            j=j+1
        for q in range(test_size):
            X = np.delete(X,[offset],0)
            Y = np.delete(Y,[offset],0)
            Z.append(L[offset+q][c])
        t = t+1
        X = np.delete(X,np.s_[c],1)
        K = L[offset:offset+test_size]
        K = np.delete(K,np.s_[c],1)
        clf = DecisionTreeClassifier(random_state=0)
        clf.fit(X,Y)
        pred=(clf.predict(K)) ##L[X:Y] selects the test data from x to y patients
        acc = (accuracy_score(pred,Z)*100)
        acc = round(acc,2)
        print ("Fold ", t," Accuracy: ",acc)
        sum1 = sum1 + acc
        label1 = Label(child, text="Fold "+str(t)+": ", fg="red",background = 'black')
        label1.place(x=pos_x,y=pos_y)
        label2 = Label(child, text=str(acc)+" %", fg="white",background='black')
        label2.place(x=pos_x+60, y=pos_y)
        pos_y = pos_y+20
    avgAccuracy = (sum1/k)
    print("Average Accuracy for ", k, " folds is ", avgAccuracy)
    label3 = Label(child, text="Average: ",fg="red",background = 'black')
    label3.place(x=pos_x, y=pos_y)
    label4 = Label(child, text=str(avgAccuracy)+" %", fg="white",background='black')
    label4.place(x=pos_x+60, y=pos_y)
    
    if not areAllAlgorithmExecuted:
	     mainloop()









    









