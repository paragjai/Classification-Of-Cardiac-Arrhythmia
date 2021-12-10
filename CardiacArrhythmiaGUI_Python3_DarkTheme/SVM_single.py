import numpy as np
import scipy
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def svm(data):
    text_file = open("data_2.txt", "r")
    x=0
    L=[]
    X=[]
    Y=[]
    D = {}
    f=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while(x<420):
        L.append(list(text_file.readline().split("\t")))
        x=x+1
    text_file.close()
    for i in range(len(L)):
        L[i]=[float(x) for x in L[i]]
    #print(L)
    i=0
    term =[]
    while(i<int(420)):
        X.append(L[i][0:163])
        Y.append(L[i][163])
        i=i+1
    clf=SVC(kernel="linear",C=10000,gamma=100)
    clf.fit(X,Y)
    test= []
    i=0
    pred =[]
	
    ''' Required for when we are passing data of a single patient '''
    if np.array(data).ndim == 1:
        no_of_features = len(data)
        print("---- no of features : ", no_of_features)
        data = np.reshape((np.array(data)), (1,no_of_features))
        print("data.shape (new shape): ", data.shape)
		
    pred = clf.predict(data)
    print(pred[0])
    return pred[0]








    








