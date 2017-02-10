from svmutil import *

y, x = svm_read_problem('Data/iris.t')

def rekClasses(yOri,xOri,yRestBits):

    #erstellen eines neuen Ausschnits aus yOri
    yOriAusschnitt = []
    xOriAusschnitt = []

    #erstelle Arrays die nur die momentan interessanten Daten enthalten
    for i in range(len(yRestBits)):
        if yRestBits[i] != -1:
            yOriAusschnitt.append(yOri[i])
            xOriAusschnitt.append(xOri[i])



    #als neue Klasse wird der erste Wert des Array verwendet.
    nextClass = int(yOriAusschnitt[0])

    #finde ein weiteres Label. Das erste Label!=nextClass wird als Label für alle Label!=nextClass verwendet.
    restClassThere = True
    restClass = 2
    yOriAusschnitttmp = yOriAusschnitt
    for i in range(len(yOriAusschnitttmp)):
        if yOriAusschnitttmp[i] != nextClass:
            if restClassThere:
                restClassThere = False
                restClass = yOriAusschnitttmp[i]
            else:
                yOriAusschnitttmp[i] = restClass

    #Abbruch erfolgt wenn kein zweites Label gefunden wurde. In diesem Falle ist restClassThere True
    if restClassThere:
        return

    #nextClass wird aus den Restlabels gelöschen. yRestBits wird dann in der Rekurrsion weitergegeben.
    for i in range(len(yRestBits)):
        if yRestBits[i] == nextClass:
            yRestBits[i] = -1

    m = svm_train(yOriAusschnitt, xOriAusschnitt, '-s 0 -t 2')
    mGesamt = []
    mGesamt.append(m)

    rekM = rekClasses(yOri,xOri,yRestBits)
    mGesamt.append(rekM)

    return mGesamt

mGesamt = rekClasses(y,x,y)