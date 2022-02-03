import sqlite3
import datetime as dt
from Classes.patient import Patient
from Classes.beacon import Beacon
from Classes.connection import Connection
import Database.Source.DataTypesFunctions as db

# conn = sqlite3.connect(':memory:') #memory
conn = sqlite3.connect('Database/table.db') #database itselft

c = conn.cursor() #cursor 

# id text,
# bedsTotal integer,
# bedsFree integer,
# room text
#DECLARING FOUR NEW BEACONS
beac_1 = Beacon("001", 1, 1, 300, 0, "B101", "Regular")
beac_2 = Beacon("002", 1, 1, 400, 0, "B102", "Regular")
beac_3 = Beacon("003", 1, 1, 200, 0, "B103", "Covid")
beac_4 = Beacon("004", 1, 1, 800, 0, "B104", "Covid-19")

db.insert_beacons(beac_1)
db.insert_beacons(beac_2)
db.insert_beacons(beac_3)
db.insert_beacons(beac_4)


# name text
# id text
# arrival datetime
# depart datetime
# disease text
# specifications text

#DECLARING FOUR NEW PATIENT ALOCATEDS
pat_1 = Patient(
        "121", 
        "Bruno Zimmer", 
        0.4,
        dt.datetime.now(),
        dt.datetime.now(),
        1,
        "Waiting",
        "Regular",
        "influenza H3N2",
        "No specifications"
        )
pat_2 = Patient("122",
         "Klaus Gamer",
         0.5,
         dt.datetime.now(),
         dt.datetime.now(),
        1,
         "Waiting",
         "Emergency",
         "influenza H1N1",
         "No specifications")
pat_3 = Patient("123",
          "Gilberto Xaissem",
         0.55,
         dt.datetime.now(),
         dt.datetime.now(),
        1,
         "Waiting",
         "Regular",
         "influenza H3N2",
         "AIDS")
pat_4 = Patient("124",
          "Deco Leleco",
         0.6,
         dt.datetime.now(),
         dt.datetime.now(),
        1,
         "Waiting",
         "Covid-19",
         "Covid-19",
         "Diabetes ")

db.insert_pat(pat_1)
db.insert_pat(pat_2)
db.insert_pat(pat_3)
db.insert_pat(pat_4)


# con_ID TEXT PRIMARY KEY,
# beac_ID TEXT,
# pat_ID TEXT,
# distance FLOAT
#DECLARING TWO NEW PATIENT NOT ALOCATEDS
connec_1 = Connection(
         '111',
         '001',
         '122',
          1.2
        )
connec_2 = Connection(
         '112',
         '001',
         '124',
          3.1
        )

db.insert_connection(connec_1)
db.insert_connection(connec_2)

conn.commit()