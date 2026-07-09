import numpy as np

X = np.array([[3.0, 5.0],    # Email 1: 3 links, 5 spelling errors
              [1.0, 1.0],    # Email 2: 1 link, 1 spelling error
              [4.0, 8.0]])   # Email 3: 4 links, 8 spelling errors

y = np.array([1.0, 0.0, 1.0]) # Truth: Email 1 is spam, Email 2 is safe, Email 3 is spam

# lets make it really it alway give the same weight to everythink it still dont know how important it is , os all w = 0.1 
W = np.array([0.1, 0.1])
# and for the bias b (It represents how cynical or trusting you are by nature. 0 <= b<= 1 ) we make it 0.5
b = 0.5
# now we calculate the score of to tell if it is a scam or not Z 

                #z = []
                #for i in range (len(X)):
                #    score = 0.0
                #    for j in range  (len (X[0])):
                #        score = score + X[i][j] * W[j] 
                #    score = score + b
                #
                #    z.append(score)
                #    print ("z de ",i," = ",z[i])
#[________________________________||||_____________________________________]
z = np.matmul(X, W)+b



def sigmoid(z):
    return (1/(1+np.exp(-z)))
print (sigmoid(z)*100,"%")

#so now that we made z into % we got some reasnable result but it can be a lot better becease both the weight W and the bias b are just random number we need to correct 
# to get a more pressice result but how ? we need to make it learn 

def corrwei (X,y,W,sigz,b):
    error = y - sigz


        #if error[i] > 0:
        #    add = 0.1 * np.abs(error[i])
        #elif error[i] < 0:
        #    add = -0.1 * np.abs(error[i])   or u can do
    add = 0.1 * error

    for j in range  (len (W)):
        W[j]= W[j] + (X[j] * add)
        b = b + add
    return W, b
    


for round in range(1000):
    for i in range (len(X)):
    #while np.abs(y[i] - sigmoid(z)[i]) > 0.01:
        
        W, b=corrwei (X[i],y[i],W,sigmoid(z)[i],b)
        z = np.matmul(X, W) + b
    if round % 100 == 0:
        print (round,": ", np.mean(np.abs(y - sigmoid(z))) * 100,"%")
print (W)
print (b)
    