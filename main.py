import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# SQL commands
sql_script = '''
CREATE TABLE IF NOT EXISTS player (
    name VARCHAR(250),
    age INT,
    score INT
);

INSERT INTO player (name, age, score) VALUES
('Ramu', 25, 85),
('Balaji', 26, 76),
('Gopi', 27, 96),
('Ganesh', 28, 55);

SELECT * FROM player;
'''

# Execute the script
cursor.executescript(sql_script)

# Fetch and print all records
cursor.execute('SELECT * FROM player')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
