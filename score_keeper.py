import sqlite3

conn = sqlite3.connect("game.db")

cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS scores")

cursor.execute("""       
    CREATE TABLE IF NOT EXISTS scores (
        player TEXT,
        high_score INTEGER        
    )
""")

player_name = input("name :")
player_score = int(input("score:"))

cursor.execute(
    "INSERT INTO scores (player, high_score) VALUES (?, ?)",
    (player_name, player_score)
)

conn.commit()

print("\n--- 🎮 LEADERBOARD ---")
cursor.execute("SELECT player , high_score FROM scores ORDER BY high_score DESC")

all_scores = cursor.fetchall()

for row in all_scores:
    print (f"player: {row[0]} | Score: {row[1]}")
conn.close()

