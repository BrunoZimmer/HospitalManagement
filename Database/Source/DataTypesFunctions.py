import sqlite3

# conn = sqlite3.connect(':memory:') #memory
conn = sqlite3.connect('Database/table.db') #database itselft

c = conn.cursor() #cursor 


""" #   Name
# 	Arrival time (arrival in the reception)
# 	Depart time (depart from reception to the room)
# 	Disease
# 	Specifications """

## DECLARING SOME FUNCTIONS TO THE WAITING PEOPLE
def insert_pat(pat):
    with conn:
        c.execute("INSERT OR REPLACE INTO patients VALUES (:id, :name, :priority, :arrival, :depart, :stayingTime, :state, :type, :disease, :specs)", 
            {'id': pat.id, 'name': pat.name, 'priority': pat.priority, 'arrival': pat.arrival, 'depart': pat.depart, 'stayingTime': pat.stayingTime,  'state': pat.state,  'type': pat.type, 'disease': pat.disease, 'specs': pat.specs}
            )

def get_pat_all():
    c.execute("SELECT * FROM patients ")
    return c.fetchall()

def get_pat_waiting(state):
    c.execute("SELECT * FROM patients WHERE state = ?", (state, ))
    return c.fetchall()

def get_pat_by_name(name):
    c.execute("SELECT * FROM patients WHERE name = ?", (name, ))
    return c.fetchall()
        
def get_pat_by_ID(id):
    c.execute("SELECT * FROM patients WHERE id = ?", (id, ))
    return c.fetchall()
    
def get_max_priority():
    c.execute("SELECT max(priority) FROM patients")
    return c.fetchone()

def update_depart(id, arrival, depart):
    with conn:
        c.execute("""UPDATE patients SET depart = :depart WHERE id = :id""",
                {'id':id, 'arrival':arrival, 'depart': depart})

def update_priority(id, priority):
    with conn:
        c.execute("""UPDATE patients SET priority = :priority WHERE id = :id""",
                {'id':id, 'priority': priority})

def remove_pat(id):
    with conn:
        c.execute("DELETE FROM patients WHERE id = :id",
                {'id':id})

""" # id
# bedsTotal
# bedsFree
price INTEGER,
reservation INTEGER,
# room """
#DECLARING SOME FUNCTIONS TO THE BEACONS

def insert_beacons(beac):
    with conn:
        c.execute("INSERT OR REPLACE INTO beacons VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (beac.id, beac.bedsTotal, beac.bedsFree, beac.price, beac.reservation, beac.room, beac.specs)
            )

def get_beac_all():
    c.execute("SELECT * FROM beacons ")
    return c.fetchall()

def get_beacon_by_room(room):
    c.execute("SELECT * FROM beacons WHERE room = ?", (room, ))
    return c.fetchone()

def get_room_by_disease_specs(room):
    c.execute("SELECT * FROM beacons WHERE room = ?", (room, ))
    return c.fetchone()

def update_beds(id, room, reservation, bedsFree):
    with conn:
        c.execute("""UPDATE beacons SET reservation = :reservation AND bedsFree = :bedsFree
            WHERE id = :id AND room = :room""",
            {'id':id, 'room':room, 'reservation':reservation, 'bedsFree':bedsFree}    
            )

def remove_beacon(id, room):
    with conn:
        c.execute("DELETE FROM beacons WHERE id = :id",
            {'id':id, 'room':room})

""" 
# con_ID TEXT PRIMARY KEY,
# beac_ID TEXT,
# pat_ID TEXT,
# distance FLOAT """

#DECLARING SOME FUNCTIONS TO THE CONNEXION BETWEEN THE BEACON AND THE PATIENT
def insert_connection(connec):
        with conn:
                c.execute("INSERT OR REPLACE INTO connections VALUES (?, ?, ?, ?)", 
                        (connec.con_ID, connec.beac_ID, connec.pat_ID, connec.distance)
                    )

def get_room_by_ID(beac_ID):
        c.execute("SELECT * FROM connections WHERE beac_ID = ?", (beac_ID, ))
        return c.fetchone()

def update_connec(con_id, pat_id):
        with conn:
                c.execute("""UPDATE connections SET pat_id = :pat_id
                            WHERE con_id = :con_id""",
                            {'con_id':con_id, 'pat_id':pat_id}    
                        )

def remove_connec(con_id, pat_id):
        with conn:
                c.execute("DELETE FROM connections WHERE con_id = :con_id",
                        {'con_id':con_id, 'pat_id':pat_id})


conn.commit()