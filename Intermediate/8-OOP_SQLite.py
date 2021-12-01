import sqlite3

class Person:
    def __init__(self, id_person=-1, first="", last="", age=-1):
        self.id_person = id_person
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()
    
    def load_person(self, id_person):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_person))

        results = self.cursor.fetchone()

        self.id_person = id_person
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.id_person, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()
        
p1 = Person()
p1.load_person(1)
print(p1.first)
print(p1.last)
print(p1.age)
print(p1.id_person)

p2 = Person(4, "Alex", "Robbins", 30)
p2.insert_person()

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close()

