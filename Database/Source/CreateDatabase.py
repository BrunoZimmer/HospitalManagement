import sqlite3

# conn = sqlite3.connect(':memory:') #memory
conn = sqlite3.connect('Database/table.db') #database itselft

c = conn.cursor() #cursor 

# DECLARATION OF THE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS patients (
        id TEXT PRIMARY KEY,
        name TEXT,
        priority FLOAT,
        arrival DATETIME NOT NULL,
        depart DATETIME,
        stayingTime INT,
        state TEXT NOT NULL,
        type TEXT NOT NULL,
        disease TEXT,
        specs TEXT
        )""")

# # DECLARATION OF THE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS beacons (
        id TEXT PRIMARY KEY,
        bedsTotal INTEGER,
        bedsFree INTEGER,
        price INTEGER,
        reservation INTEGER,
        room TEXT,
        specs TEXT
        )""")

# # DECLARATION OF THE TABLE TO THE connection 
c.execute("""CREATE TABLE IF NOT EXISTS connections (
        id TEXT PRIMARY KEY,
        beac_ID TEXT NOT NULL,
        pat_ID TEXT NOT NULL,
        distance FLOAT,
        FOREIGN KEY(beac_ID) REFERENCES beacons(id),
        FOREIGN KEY(pat_ID) REFERENCES patients(id)
        )""")


conn.commit()