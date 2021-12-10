'''VFI1'''
import random
import math
from tkinter import *


#GLOBAL VARIABLES:
D = {}                          #Dictionary to store all the records with the key value as the class label
e =  2.71828
DMV = {}                        #Dictionary to story the mean and Variance of each class
total = 420                     #The total number of records
train_no = int(0.67*total)      #The number of records taken for training
test_no = total -train_no       #The number of records taken for testing
features_no = 163               #Total number of attributes
class_total = 16                #Total number of class labels
L=[]           
tester =[]                      #List to hold all the test samples
labels=[]                       #List to hold the class labels of the test samples
T=[]                            #List to hold all the predicted labels of the test samples
Endpoints=[]                    #List of lists that holds the endpoints of each feature
Classdist=[]                    #The list which hold the count of all classes in each interval of each feature
k = 10                          #The number of folds for cross validation


#TO CROSS VALIDATE
def crossval(areAllAlgorithmExecuted):
    #Creating a child window to display the accuracy
    child = Tk()
    child.title("VFI1 Accuracy")
    child.geometry("300x300")
    child.configure(background='black')
    dataset()
    accuracy =0
    global train_no
    pos =0
    pos_x=60
    pos_y=50
    j=0
    
    while(pos<=total):
        #To obtain test set in the jth fold of cross validation
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
        #To obtain the trainset
        trainSet = list(set(tuple(x) for x in L) - set(tuple(x) for x in tester1)) 
        train_no = len(trainSet)
        datatrain(trainSet)
        test_data(tester1)
        endpoints()
        countinterval()
        accuracy1 = test()
        accuracy1 = round(accuracy1,2)
        label1 = Label(child, text="Fold "+str(j)+": ", fg="red", background = 'black')
        label1.place(x=pos_x,y=pos_y)
        label2 = Label(child, text=str(accuracy1)+" %", fg="white",background = 'black')
        label2.place(x=pos_x+60, y=pos_y)
        pos_y = pos_y+20
        print('Accuracy of fold ',j, ' is = ' ,accuracy1)
        accuracy+=accuracy1
    #Finds average accuracy of all folds
    accuracy = float(accuracy)/float(n)
    print('Average accuracy of all ', n ,' folds = ', accuracy)
    accuracy = round(accuracy,2)
    label3 = Label(child, text="Average: ",fg="red",background = 'black' )
    label3.place(x=pos_x, y=pos_y)
    label4 = Label(child, text=str(accuracy)+" %", fg="white",background='black')
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
    #To arrange the records in a random order
    random.shuffle(L)

#TO GET TRAIN DATA IN DICTIONARY
def datatrain(L):
    i=0
    f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    #Dictionary D obtained where key is the class label and the value is a list of lists of all the records belonging to that class
    while(i<train_no):
        index = int(((L[i][features_no])-1))
        if(f[index]==0):
            P = [L[i][0:features_no]]
            D.update({index:P})
            f[index]=1
        else:
            D[index].append(L[i][0:features_no])
        i=i+1
    #Assigning an empty list to all those class labels that dont have any records
    for i in range(0,class_total):
        if(f[i]==0):
            P = []
            D.update({i:P})
            f[i]=1

#TO GET ENDPOINTS OF EACH CLASS OF EACH FEATURE
def endpoints():
    global Endpoints
    Endpoints =[]
    for k in range(features_no):
        Endpoints1=[]
        Endpoints1.append(-1000)
        for i in range(class_total):
            L=[]
            for j in range(len(D[i])):
                if(D[i][j][k]!=999):
                    L.append(D[i][j][k])
            #print(L)
            if(len(L)!=0):
                #Finding max and min of each class for the feature k
                Endpoints1.append(min(L))
                Endpoints1.append(max(L))
        Endpoints1.append(max(Endpoints1)+1000)
        Endpoints.append(Endpoints1)
    #Sorting the endpoints in ascending order
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
                        #Condition for value lying on lower bound
                        if(D[i][j][k] == int(Endpoints[k][l]) and l!=min(Endpoints[k])):
                            Classdist1[l][i] = Classdist1[l][i] + 0.5
                            Classdist1[l-1][i] = Classdist1[l-1][i] + 0.5
                        #Condition for value lying completely in the interval
                        elif( D[i][j][k] in range(int(Endpoints[k][l]) , int(Endpoints[k][l+1]))):
                            Classdist1[l][i] = Classdist1[l][i] +1
        Classdist.append(Classdist1)
    #The class count for every interval for every feature must be divied by the total number of instances of that class
    for k in range(features_no):
        for i in range(0,class_total):
            for j in range(0,len(Endpoints[k])):
                if(len(D[i])!=0):
                    Classdist[k][j][i] = float(Classdist[k][j][i])/float( len(D[i]))
    s=[]
    #Normalising the class counts of every interval in every feature
    
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



#TO FIND INTERVAL OF A TEST FEATURE VALUE 
def find_interval(f,ef):
    Endpoints[f][-1]+=1
    for i in range((len(Endpoints[f])-1)):
        #Condition for value lying completely in the interval
        if(ef<Endpoints[f][i+1] and ef>Endpoints[f][i]):
            return [i]
        #Condition for value lying on the lower bound
        elif (ef==Endpoints[f][i]):
            return [i, i-1]




#To classify one test case
def classify(ex):
    Vote=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(class_total):
        for j in range(features_no):
            interval = find_interval(j, ex[j])
            if(ex[j]!=999 and interval!=None):
                for k in range(class_total):
                    if(len(D[k])!=0):
                        if(len(interval) ==1):
                            Vote[k] += float(Classdist[j][int(interval[0])][k]) 
                        elif(len(interval) ==2):
                            Vote[k] += (float(Classdist[j][int(interval[0])][k]) + float(Classdist[j][int(interval[1])][k]))/2.0
    #Finding the class with max votes and returning that class label
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
    #Comparing predicted labels with actual labels to calculate accuracy
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

