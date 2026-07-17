import sqlite3

conn = sqlite3.connect("email.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        body TEXT,
        is_spam INTEGER          
    )
""")

cursor.execute("""
    INSERT INTO emails (subject ,body ,is_spam) VALUES 
    ('Meeting Tomorrow ','Hey, let us meet tomorrow at 10 AM to review the project details.','0'),
    ('URGENT!!! Win Free Cash Now ','You have been selected to win a free cash prize of $5000! Click here now!','1'),
    ('Weekly Report Details ','Attached is the weekly progress report for the team. Please review.','0'),
    ('Super Cheap Pharmacy Offers ','Get cheap meds without a prescription! Limited time offer buy now.','1'),
    ('Hey buddy ','Are you free for a football game tonight? Let me know.','0')
""")

conn.commit()
conn.close()

print("Email database created and populated successfully!")