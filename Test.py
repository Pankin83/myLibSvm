from svmutil import *

y, x = svm_read_problem('Data/iris.t')

#eigene Code
class1tmp = y[0]
class1 = []
class2 = []
for yi in y:
    if yi != class1tmp:
        class1.append(0)
        class2.append(yi)
    else:
        class1.append(yi)
        class2.append(0)



def rekClasses(yOri,xOri,yRestBits):

    #erstellen eines neuen Ausschnits aus yOri
    yOriAusschnitt = []
    xOriAusschnitt = []
    return 1
    #erstelle Arrays die nur die momentan interessanten Daten enthalten
    for i in range(len(yRestBits)):
        if yRestBits[i] != -1:
            yOriAusschnitt.append(yOri[i])
            xOriAusschnitt.append(xOri[i])



    #als neue Klasse wird der erste Wert des Array verwendet.
    nextClass = yOriAusschnitt[0]

    #finde ein weiteres Label. Das erste Label!=nextClass wird als Label für alle Label!=nextClass verwendet.
    restClassThere = True
    restClass = 2
    for label in yOriAusschnitt:
        if label != nextClass:
            if restClassThere:
                restClassThere = False
                restClass = label
            else:
                label = restClass

    #Abbruch erfolgt wenn kein zweites Label gefunden wurde. In diesem Falle ist restClassThere True
    if restClassThere:
        return

    #nextClass wird aus den Restlabels gelöschen. yRestBits wird dann in der Rekurrsion weitergegeben.
    for label in yRestBits:
        if label == nextClass:
            label = -1

    m = svm_train(yOriAusschnitt, xOriAusschnitt, '-s 0 -t 2')
    mGesamt = []
    mGesamt.append(m)

    rekM = rekClasses(yOri,xOri,yRestBits)
    mGesamt.append(rekM)

    return mGesamt



######
m = rekClasses(y,x,y)
m = svm_train(y, x, '-s 0 -t 2')
p_label, p_acc, p_val = svm_predict(y, x, m)

# Construct problem in python format
# Dense data
# y, x = [1,-1], [[1,0,1], [-1,0,-1]]
# Sparse data
y, x = [1,-1], [{1:1, 3:1}, {1:-1,3:-1}]
prob  = svm_problem(y, x)
param = svm_parameter('-t 0 -c 4 -b 1')
m = svm_train(prob, param)

# Precomputed kernel data (-t 4)
# Dense data
y, x = [1,-1], [[1, 2, -2], [2, -2, 2]]
# Sparse data
y, x = [1,-1], [{0:1, 1:2, 2:-2}, {0:2, 1:-2, 2:2}]
# isKernel=True must be set for precomputed kernel
prob  = svm_problem(y, x, isKernel=True)
param = svm_parameter('-t 4 -c 4 -b 1')
m = svm_train(prob, param)
# For the format of precomputed kernel, please read LIBSVM README.



