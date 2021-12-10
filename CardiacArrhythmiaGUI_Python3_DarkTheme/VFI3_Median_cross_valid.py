'''VFI3: MODIFICATION OF LOWER BOUND CONDITIONS AND FINAL NORMALISATION'''
import random
import math
from tkinter import *
    
#GLOBAL VARIABLES:
D = {}
e =  2.71828
DMV = {}
total = 420
train_no = int(0.9*total)
test_no = total -train_no
features_no = 163
class_total = 16
L=[]
prior=[]
P ={}
tester =[]
labels=[]
T=[]
Endpoints=[]
Classdist=[]
E=[]            #3D List to store max and min of each class for each feature
k = 10

#TO CROSS VALIDATE
def crossval(areAllAlgorithmExecuted):
    child = Tk()
    child.title("VFI3 Accuracy")
    child.geometry("300x300")
    child.configure(background='black')
    dataset()
    accuracy =0
    global train_no
    pos =0
    j=0
    pos_x=60
    pos_y=50
    while(pos<=total):
        if((pos+int(total/k)) > total ):
            if(total-pos)<10:
                break
            tester1 = L[pos:total]
            n=k+1
            pos = total+1
        else:
            tester1 = L[pos:(((j+1)*(int(total/k))))]
            pos=int(((j+1)*(total/k)))
            n=k
        j+=1
        trainSet = list(set(tuple(x) for x in L) - set(tuple(x) for x in tester1))
        train_no = len(trainSet)
        datatrain(trainSet)
        test_data(tester1)
        endpoints()
        countinterval()
        accuracy1 = test()
        accuracy1 = round(accuracy1,2)
        label1 = Label(child, text="Fold "+str(j)+": ", fg="red",background = 'black')
        label1.place(x=pos_x,y=pos_y)
        label2 = Label(child, text=str(accuracy1)+" %", fg="white",background ='black')
        label2.place(x=pos_x+60, y=pos_y)
        pos_y = pos_y+20
        print('Accuracy of fold ',j, ' is = ' ,accuracy1)
        accuracy+=accuracy1
    accuracy = float(accuracy)/float(n)
    print('Average accuracy of all ', n ,' folds = ', accuracy)
    accuracy = round(accuracy,2)
    label3 = Label(child, text="Average: ",fg="red",background ='black')
    label3.place(x=pos_x, y=pos_y)
    label4 = Label(child, text=str(accuracy)+" %", fg="white", background ='black')
    label4.place(x=pos_x+60, y=pos_y)
   
    if not areAllAlgorithmExecuted:
       mainloop()

#TO GET TEST DATASET IN FORM OF LIST
def dataset():
    text_file = open("data_2.txt", "r")
    x=0
    X=[]
    Y=[]
    while(x<total):
        L.append(list(text_file.readline().split("\t")))
        x=x+1
    text_file.close()
    for i in range(len(L)):
        L[i]=[float(x) for x in L[i]]
    random.shuffle(L)

#TO GET TRAIN DATA IN DICTIONARY
def datatrain(L):
    i=0
    f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while(i<train_no):
        index = int(((L[i][features_no])-1))
        if(f[index]==0):
            P = [L[i][0:features_no]]
            D.update({index:P})
            f[index]=1
        else:
            D[index].append(L[i][0:features_no])
        i=i+1
    for i in range(0,class_total):
        if(f[i]==0):
            P = []
            D.update({i:P})
            f[i]=1

#TO GET ENDPOINTS OF EACH CLASS OF EACH FEATURE
def endpoints():
    global Endpoints
    Endpoints =[]
    global E
    E =[]
    for k in range(features_no):
        Endpoints1=[]
        Endpoints1.append(-1000)
        E2=[]
        for i in range(class_total):
            L=[]
            for j in range(len(D[i])):
                if(D[i][j][k]!=999):
                    L.append(D[i][j][k])
            if(len(L)!=0):
                E1=[]
                Endpoints1.append(min(L))
                Endpoints1.append(max(L))
                E1.append(min(L))
                E1.append(max(L))
            E2.append(E1)
        Endpoints1.append(max(Endpoints1)+1000)
        Endpoints.append(Endpoints1)
        E.append(E2)
    for i in range(features_no):
        Endpoints[i] = list(set(Endpoints[i]))
        Endpoints[i].sort()

#To count no of instances of each class in each interval of each feature
def countinterval():
    global Classdist, Ptdist
    Ptdist =[]
    Classdist =[]
    for k in range(features_no):
        Classdist1 =[]
        for i in range(0, len(Endpoints[k])):
            Classdist1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        for i in range(class_total):
            for j in range (len(D[i])):
                for l in range(len(Endpoints[k])-1):
                    if(D[i][j][k]!=999):
                        if(D[i][j][k] == int(Endpoints[k][l]) and l!=min(Endpoints[k])):
                            #Condition for when the value is the minimum value of feature k of class i
                            if(D[i][j][k]==E[k][i][0]):
                                Classdist1[l][i] = Classdist1[l][i] +1
                            #Condition for when the value is the maximum value of feature k of class i
                            elif(D[i][j][k]==E[k][i][1]):
                                Classdist1[l-1][i] = Classdist1[l-1][i] +1
                            #Condition for when the value is neither the maximum nor the minimum value of feature k of class i
                            else:
                                Classdist1[l][i] = Classdist1[l][i] + 0.5
                                Classdist1[l-1][i] = Classdist1[l-1][i] + 0.5
                        elif( D[i][j][k] in range(int(Endpoints[k][l]) , int(Endpoints[k][l+1]))):
                            Classdist1[l][i] = Classdist1[l][i] +1
        Classdist.append(Classdist1)
    for k in range(features_no):
        for i in range(0,class_total):
            for j in range(0,len(Endpoints[k])):
                if(len(D[i])!=0):
                    Classdist[k][j][i] = float(Classdist[k][j][i])/float( len(D[i]))
    s=[]
    for k in range(features_no):
        s1=[]
        for i in range(0,len(Endpoints[k])):
            s1.append(sum(Classdist[k][i]))
        s.append(s1)

    for k in range(features_no):
        for i in range(0,class_total):
            for j in range(0,len(Endpoints[k])):
                if(s[k][j]!=0):
                    Classdist[k][j][i] = float(Classdist[k][j][i])/float(s[k][j])

#TO FIND INTERVAL OF A TEST FEATURE
def find_interval(f,ef):
    Endpoints[f][-1]+=1
    for i in range((len(Endpoints[f])-1)):
        if(ef<Endpoints[f][i+1] and ef>Endpoints[f][i]):
            return [i]
        elif (ef==Endpoints[f][i]):
            for l in range(class_total):
                #Condition for when the value is the minimum value of feature f of class l
                if(ef == E[f][l][0]):
                    return [i]
                #Condition for when the value is the maximum value of feature f of class l
                elif (ef==E[f][l][1]):
                    return [i-1]
                #Condition for when the value is neither the maximum nor the minimum value of feature f of class l
                else:
                    return [i, i-1]

#To classify one test case
def classify(ex):
    Vote=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(class_total):
        for j in range(features_no):
            Vote1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            interval = find_interval(j, ex[j])
            if(ex[j]!=999 and interval!=None):
                for k in range(class_total):
                    if(len(D[k])!=0):
                        if(len(interval) ==1):
                            Vote1[k] += float(Classdist[j][int(interval[0])][k])
                        elif(len(interval) ==2):
                            Vote1[k] += (float(Classdist[j][int(interval[0])][k]) + float(Classdist[j][int(interval[1])][k]))/2.0
                x= sum(Vote1)
                for m in range(class_total):
                    if(sum(Vote1)!=0):
                        Vote1[m]=float(Vote1[m])/float(x)
                for m in range(class_total):
                    Vote[m]+=Vote1[m]
    m = max(Vote)
    for i in range(class_total):
        if Vote[i] == m:
            pos =i
    return pos+1

#TO CLASSIFY ALL TEST CASES
def test():
    T=[]
    for i in range(len(tester)):
        T.append(classify(tester[i]))
    count =0
    for i in range(len(T)):
        if(T[i] == int(labels[i])):
            count= count+1
    accuracy = (float(count)/ float(len(labels)))*100
    return accuracy              
                   
#TO GET TEST DATA SET
def test_data(L):
    global labels
    labels =[]
    global tester
    tester =[]
    for i in range(len(L)):
        tester.append(L[i][:features_no])
        labels.append(L[i][features_no])

def vfi(areAllAlgorithmExecuted):
    crossval(areAllAlgorithmExecuted)
