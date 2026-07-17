-- sqlite

-- 1. First, delete all the rows inside the table
DELETE FROM notes;

-- 2. Second, reset the ticket machine counter back to 0
DELETE FROM sqlite_sequence WHERE name = 'notes';

-- 3. Now, the table is empty AND the counter is 0, so we can insert cleanly!
CREATE TABLE IF NOT EXISTS notes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	content TEXT
);

INSERT INTO notes(title, content)
VALUES
('Shopping List','Buy milk,eggs, and bread.'),
('ML Idea','Try using Leaky ReLU for the neural network.'),
('Git Reminder','Always run git status before committing!');

-- 4. Let's see the clean result!
SELECT * FROM notes WHERE id > 1;