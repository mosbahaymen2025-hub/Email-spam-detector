i = 0
m = 0
s = 0
while True : 
    if (i % 2 == 0):
        while (1==1):
            m = int (input("player 1 either pick 1 or 2 :"))
            if (m == 1 or m == 2) and (s + m <=5) :
                break
    elif (i % 2 !=0):
        while (1==1):
            m = int (input("player 2 either pick 1 or 2 :"))
            if (m == 1 or m == 2) and (s + m <=5) :
                break
    s = s + m
    if (s == 5):
        if (i % 2 == 0):
            print ("player 1 lose")
            print ("player 2 Win")
        else :
            print ("player 1 Win")
            print ("player 2 lose")
        break
    i = i + 1

