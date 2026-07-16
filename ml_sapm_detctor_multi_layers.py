import numpy as np

X = np.array([[3.0, 5.0],    # Email 1: 3 links, 5 spelling errors
              [1.0, 1.0],    # Email 2: 1 link, 1 spelling error
              [4.0, 8.0]])   # Email 3: 4 links, 8 spelling errors

y = np.array([[1.0], [0.0], [1.0]]) # Truth: Email 1 is spam, Email 2 is safe, Email 3 is spam

w1 = np.random.randn(2,3)
b1 = np.array([0.0,0.0,0.0])

def ReLU(z):
    return np.maximum(0.01 * z, z)

w2 = np.random.randn(3, 1)
b2 = 0

def sigmoid (z):
    return (1/(1+np.exp(-z)))

for i in range (1000):
    z1 = np.matmul(X,w1) + b1
    a1 = ReLU(z1)

    z2 = np.matmul(a1,w2) + b2
    a2 = sigmoid (z2)

    error = y - a2

    manager_sensitivity = a2 * ( 1- a2 )

    manger_blame = error * manager_sensitivity

    

    emplye_blame = np.matmul(manger_blame , w2.T) #We have 3 emails and 3 employees. We need to know how much blame each of the 3 employees gets for each of the 3 emails


    Learning_Rate = 0.01

    w2 = w2 + (Learning_Rate * np.matmul(a1.T , manger_blame))
    b2 = b2 + Learning_Rate * np.sum(manger_blame)
    w1 = w1 + (Learning_Rate * np.matmul(X.T , (emplye_blame* np.where(z1 > 0, 1.0, 0.01)))) 
    active_blame = emplye_blame * np.where(z1 > 0, 1.0, 0.01)
    b1 = b1 + Learning_Rate * np.sum(active_blame, axis=0)
    
    if i % 100 == 0 :
        print (i)
        print (error)
        #print ("z1 = ",z1)
        #print ("a1 = ",a1)

        #print ("a2= ",a2)
        #print ("manger_blame = ",manger_blame)
        #print ("emplye_blame = ",emplye_blame)

        #print ("NEW w2 = ",w2)
        #print ("NEW w1 = ",w1)

Xnew = []

test = False
while test == False:
    links1 = int(input("give the nuber of links in your email : "))
    spellings1 = int(input("give the nuber of wrong spelling in your email : "))
    if (0<=links1<=100 and 0<=spellings1<=100) :
        Xnew.append(links1)
        Xnew.append(spellings1)
        test = True
Znew1 = np.matmul(Xnew, w1) + b1
ANew1 = ReLU(Znew1)

Znew2 = np.matmul(ANew1, w2) + b2
ANew2 = sigmoid(Znew2)
if ANew2 < 0.5 :
    print ("safe")
else : 
    print ("spam")