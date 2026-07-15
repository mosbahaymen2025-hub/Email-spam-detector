import numpy as np

X = np.array([[3.0, 5.0],    # Email 1: 3 links, 5 spelling errors
              [1.0, 1.0],    # Email 2: 1 link, 1 spelling error
              [4.0, 8.0]])   # Email 3: 4 links, 8 spelling errors

y = np.array([[1.0],[0.0],[1.0]])    # Truth: Email 1 is spam, Email 2 is safe, Email 3 is spam



def sigmoid (z):
    return (1/(1+np.exp(-z)))




#W1 = np.array([[ np.random.randn(),np.random.randn() ,np.random.randn() ]
#               [ np.random.randn(),np.random.randn() ,np.random.randn() ]])

# |__________________________\/___________________________________|
w1 = np.random.randn(2, 3)
b1 = np.array([0, 0, 0])

w2 = np.random.randn(3, 1)
b2 = 0

z1 = np.matmul(X , w1) + b1
a1 = np.maximum(0 , z1)


z2 = np.matmul(a1 , w2) + b2
a2 = sigmoid(z2)


error = y - a2
sensitivity = a2 *(1-a2)
delta2 = error * sensitivity

delta1 = np.matmul(delta2 , w2.T) * (z1>0)

w2 = w2 + (0.1 * np.matmul(a1.T , delta2))
b2 = b2 + np.sum(delta2)
print(w2)
print(b2)
w1 = w1 + (0.1 * np.matmul(X.T , delta1))
b1 = b1 + np.sum(delta1)
print(w1)
print(b1)