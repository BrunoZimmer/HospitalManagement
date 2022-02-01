import sqlite3
import datetime
from patient import Patient
from beacon import Beacon
from connection import Connection

# conn = sqlite3.connect(':memory:') #memory
conn = sqlite3.connect('table.db') #database itselft

c = conn.cursor() #cursor 

# DECLARATION OF THE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS patients (
        pat_ID TEXT PRIMARY KEY,
        name TEXT,
        arrival DATETIME NOT NULL,
        depart DATETIME,
        disease TEXT NOT NULL,
        specifications TEXT
        )""")

# # DECLARATION OF THE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS beacons (
        beac_ID TEXT PRIMARY KEY,
        bedsTotal INTEGER,
        bedsFree INTEGER,
        room TEXT
        )""")

# # DECLARATION OF THE TABLE TO THE connection 
c.execute("""CREATE TABLE IF NOT EXISTS connections (
        con_ID TEXT PRIMARY KEY,
        beac_ID TEXT,
        pat_ID TEXT,
        distance FLOAT
        )""")

#   Name
# 	Arrival time (arrival in the reception)
# 	Depart time (depart from reception to the room)
# 	Disease
# 	Specifications

#DECLARING SOME FUNCTIONS TO THE WAITING PEOPLE
def insert_pat(pat):
        with conn:
                c.execute("INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?)", 
                    (pat.pat_ID, pat.name, pat.arrival, pat.depart, pat.disease, pat.specs)
                    )


def get_pat_by_name(name):
        c.execute("SELECT * FROM patients WHERE name = ?", (name, ))
        return c.fetchall()
        
def get_pat_by_ID(pat_ID):
        c.execute("SELECT * FROM patients WHERE pat_ID = ?", (pat_ID, ))
        return c.fetchall()

def update_depart(name, pat_ID, arrival, depart, disease, specs):
        with conn:
                c.execute("""UPDATE patients SET depart = :depart
                             WHERE name = :name AND pat_ID = :pat_ID""",
                        {'name':name, 'pat_ID':pat_ID, 'arrival':arrival, 'depart': depart, 'disease': disease, 'specs': specs})

def remove_pat(name, pat_ID):
        with conn:
                c.execute("DELETE FROM patients WHERE name = :name AND pat_ID = :pat_ID",
                        {'first':name, 'pat_ID':pat_ID})

# id
# bedsTotal
# bedsFree
# room
#DECLARING SOME FUNCTIONS TO THE BEACONS
def insert_beacons(beac):
        with conn:
                c.execute("INSERT INTO beacons VALUES (?, ?, ?, ?)", 
                        (beac.beac_ID, beac.bedsTotal, beac.bedsFree, beac.room)
                    )

def get_beacon_by_room(room):
        c.execute("SELECT * FROM beacons WHERE room = ?", (room, ))
        return c.fetchone()

def update_beds(beac_ID, room, bedsFree):
        with conn:
                c.execute("""UPDATE beacons SET bedsFree = :bedsFree
                             WHERE beac_ID = :beac_ID AND room = :room""",
                            {'beac_ID':beac_ID, 'room':room, 'bedsFree':bedsFree}    
                        )

def remove_beacon(beac_ID, room):
        with conn:
                c.execute("DELETE FROM beacons WHERE beac_ID = :beac_ID",
                        {'beac_ID':beac_ID, 'room':room})


# con_ID TEXT PRIMARY KEY,
# beac_ID TEXT,
# pat_ID TEXT,
# distance FLOAT

#DECLARING SOME FUNCTIONS TO THE CONNEXION BETWEEN THE BEACON AND THE PATIENT
def insert_connexion(beac):
        with conn:
                c.execute("INSERT INTO connections VALUES (?, ?, ?, ?)", 
                        (beac.con_ID, beac.beac_ID, beac.pat_ID, beac.distance)
                    )

def get_room_by_ID(beac_ID):
        c.execute("SELECT * FROM connections WHERE beac_ID = ?", (beac_ID, ))
        return c.fetchone()

def update_pat(con_id, pat_id):
        with conn:
                c.execute("""UPDATE connections SET pat_id = :pat_id
                            WHERE con_id = :con_id""",
                            {'con_id':con_id, 'pat_id':pat_id}    
                        )

def remove_pat(con_id, pat_id):
        with conn:
                c.execute("DELETE FROM connections WHERE con_id = :con_id",
                        {'con_id':con_id, 'pat_id':pat_id})




# id text,
# bedsTotal integer,
# bedsFree integer,
# room text
#DECLARING FOUR NEW BEACONS
beac_1 = Beacon('001', 1, 1, 'B101')
beac_2 = Beacon('002', 1, 1, 'B102')
beac_3 = Beacon('003', 1, 1, 'B103')
beac_4 = Beacon('004', 1, 1, 'B104')


# name text
# id text
# arrival datetime
# depart datetime
# disease text
# specifications text

#DECLARING FOUR NEW PATIENT ALOCATEDS
pat_1 = Patient('Bruno Zimmer', '121',  datetime.datetime.now(), datetime.datetime.now(), 'influenza', 'No specifications')
pat_2 = Patient('Klaus Gamer', '122',  datetime.datetime.now(), datetime.datetime.now(), 'H1N1', 'No specifications')
pat_3 = Patient('Gilberto Xaissem', '123',  datetime.datetime.now(), datetime.datetime.now(), 'influenza', 'No specifications')
pat_4 = Patient('Deco Leleco', '124',  datetime.datetime.now(), datetime.datetime.now(), 'Covid-19', {'AIDS', 'Diabetes'})

# ID
# room
# Distance
# Patient
#DECLARING TWO NEW PATIENT NOT ALOCATEDS
connex_1 = Connection('001', 'B101', 1.2,'Gilberto Xaissem')
connex_2 = Connexion('003', 'B103', 3.1,'Deco Leleco')

conn.close()