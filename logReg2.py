# noinspection PyUnresolvedReferences
import numpy, scipy.optimize
import pylab
import math

def sigmoid(X):
    return 1/(1 + math.e ** (-1.0 * X))

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers),1)

def cost(theta,X,y):
    m = X.shape[0]

    Jtmp = []


    for i in range(m):
        Jtmp.append(y[i] * numpy.log(sigmoid(theta.T.dot(X[i]))) + (1-y[i]) * numpy.log(1 - sigmoid(theta.T.dot(X[i]))))
        # print(y[i])

    # for i in range(m):
    #     if Jtmp[i] < 0:
    #         print("kleiner als 0")


    j = mean(Jtmp)

    return -1 *j


def grad(theta,X,y):


    htheta = sigmoid(numpy.dot(X,theta))

    error = htheta - y



    gradient = numpy.dot(error,X) / y.size

    return gradient


data = numpy.loadtxt('Data/ex2data1.txt', delimiter=',')


X = data[:,0:2]
y = data[:,2]

theta = 0.1*numpy.random.randn(3)

X_1 = numpy.append(numpy.ones((X.shape[0], 1)), X, axis=1)

# print(scipy.optimize.fmin_bfgs(cost,theta,fprime=grad,args=(X_1,y)))

X = [1,60,70]

theta = [-25.16133602, 0.20623174,   0.20147162]

def predict(theta, X):
    p_1 = sigmoid(numpy.dot(X, theta))
    return p_1


print(predict(theta,X))