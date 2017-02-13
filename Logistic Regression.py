# noinspection PyUnresolvedReferences
import numpy, scipy.optimize
import pylab
import math


def sigmoid(X):
    '''Compute the sigmoid function '''
    # d = zeros(shape=(X.shape))

    den = 1.0 + math.e ** (-1.0 * X)

    d = 1.0 / den

    return d


def compute_cost(theta, X, y):  # computes cost given predicted and actual values
    m = X.shape[0]  # number of training examples
    theta = reshape(theta, (len(theta), 1))

    # y = reshape(y,(len(y),1))

    J = (1. / m) * (
    -transpose(y).dot(log(sigmoid(X.dot(theta)))) - transpose(1 - y).dot(log(1 - sigmoid(X.dot(theta)))))

    grad = transpose((1. / m) * transpose(sigmoid(X.dot(theta)) - y).dot(X))
    # optimize.fmin expects a single value, so cannot return grad
    return J[0][0]  # ,grad


def compute_grad(theta, X, y):
    # print theta.shape
    m = X[0].shape
    theta.shape = (1, 3)

    grad = numpy.zeros(3)

    h = sigmoid(X.dot(theta.T))

    delta = h - y

    l = grad.size

    for i in range(l):
        sumdelta = delta.T.dot(X[:, i])
        grad[i] = (1.0 / m) * sumdelta * - 1

    theta.shape = (3,)

    return grad

data = numpy.loadtxt('Data/ex2data.txt', delimiter=',')

theta = 0.1*numpy.random.randn(3)

X = data[:,1:3]
y = data[:,0]

X_1 = numpy.append(numpy.ones((X.shape[0], 1)), X, axis=1)

theta_1 = scipy.optimize.fmin_bfgs(compute_cost,theta, fprime=compute_grad,args=(X_1, y))
