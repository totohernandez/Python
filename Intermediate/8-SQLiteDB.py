import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)""")

cursor.execute("""
INSERT INTO persons VALUES
(1, 'Paul', 'Smith', 24),
(2, 'Mark', 'Johnson', 42),
(3, 'Anna', 'Smith', 45)
""")

cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()