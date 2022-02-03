import sqlite3
import datetime
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
beac_1 = Beacon("005", 2, 2, 100, 0, "B105")

db.insert_beacons(beac_1)


# name text
# id text
# arrival datetime
# depart datetime
# disease text
# specifications text

#DECLARING FOUR NEW PATIENT ALOCATEDS
pat_1 = Patient("125", "Alisson Dreher",  0.5, datetime.datetime.now(), datetime.datetime.now(), "Regular", "influenza H3N1", "No specifications")

db.insert_pat(pat_1)

# con_ID TEXT PRIMARY KEY,
# beac_ID TEXT,
# pat_ID TEXT,
# distance FLOAT
#DECLARING TWO NEW PATIENT NOT ALOCATEDS
connec_1 = Connection('113', '002','123', 1.6)

db.insert_connection(connec_1)

conn.commit()