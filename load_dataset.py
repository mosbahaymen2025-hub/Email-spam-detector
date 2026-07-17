import sqlite3

conn = sqlite3.connect("email.db")

cursor = conn.cursor()

cursor.execute("""
    SELECT body,is_spam FROM emails;              
""")

listemails = cursor.fetchall()
X = []
y = []
for row in listemails:
    X.append(row[0])
    print(row[0])
    y.append(row[1])
    print(row[1])


safe_array = []
spam_array = []
ligne_safe = 0
ligne_spam = 0

for col in range (len(X)):
    i = 0
    start = 0
    if y[col] == 1:
        while i != len(X[col]):
            if X[col][i] in ( " ",",",".","!","?"):
                test = False
                for j in spam_array:
                    if X[col][start:i] == j[0]:
                        j[1] = j[1] + 1
                        test = True
                        break
                if test == True :    
                    start = i + 1
                else :
                    spam_array.append([X[col][start:i],1])
                    ligne_spam = ligne_spam + 1
                    start = i + 1
            i = i + 1



    elif y[col] == 0 :
        while i != len(X[col]):
            if X[col][i] in ( " ",",",".","!","?"):
                test = False
                for j in safe_array:
                    if X[col][start:i] == j[0]:
                        j[1] = j[1] + 1
                        test = True
                        break
                if test == True : 
                    start = i + 1
                else :
                    safe_array.append([X[col][start:i],1])
                    ligne_safe = ligne_safe + 1
                    start = i + 1
            i = i + 1

print (spam_array)

print(safe_array)


cursor.execute("""
    CREATE TABLE IF NOT EXISTS vocabulary(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    frequency INTEGER ,
    is_spam INTEGER
 )
""") 
for m in (spam_array):
    cursor.execute(
        "INSERT INTO vocabulary( word, frequency,is_spam ) VALUES (?, ?, ?)",
        (m[0], m[1],1)
    )   
for n in (safe_array):
    cursor.execute(
        "INSERT INTO vocabulary( word, frequency,is_spam ) VALUES (?, ?, ?)",
        (n[0], n[1],0)
    )
    
conn.commit()
conn.close()
