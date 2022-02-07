import datetime as dt
from Database.Source.DataTypesFunctions import *
import sys ,os
from ctypes import *
from Classes.patient import *
from Classes.beacon import *
from Classes.connection import *

import msvcrt

class Decision:
    """A class of functions to decision"""
    def updatePatients(time):
        waitingPatients = get_pat_waiting("Waiting")
        freeRooms = get_beac_free()

        patients= []
        
        for patientList in waitingPatients:
            patients.append(CreatePatient(patientList))
        patients.sort(key=lambda patient: patient.priority)


        rooms= []
        
        for roomList in freeRooms:
            rooms.append(CreateBeacon(roomList))
        rooms.sort(key=lambda room: room.price)

        #make the two calls ordered
        if patients:
            for waitingPatient in patients:
                #print(waitingPatient)
                update_depart(waitingPatient.id, waitingPatient.arrival, dt.datetime.now())
                waitingPatient.priority = waitingPatient.makePriority
                update_priority(waitingPatient.id, waitingPatient.priority)
                if rooms:
                    for freeRoom in rooms:
                        if(waitingPatient.specs == freeRoom.specs and freeRoom.bedsFree - freeRoom.reservation >0):
                            print("The patient "+ waitingPatient.name + "can go to the room " + freeRoom.room)
                            input("Press something to continue")
                            #Here we need to add the exception to when the receptionist disagree the program
                            update_state(waitingPatient.id, "Alocated")
                            update_reservation(freeRoom.id, freeRoom.reservation+1)
            

    def timeWaitingName(name):
        pat = get_pat_by_name(name)
        beaconsCompatibles = get_beac_specs(pat.specs)

        beaconsCompatibles.sort(key=lambda beaconAvai: beaconAvai.depart, reverse=True)

        beacon = CreateBeacon(beaconsCompatibles[0])

        connec = get_connec_by_BeacID(beacon.id)
        patient = get_pat_by_ID(connec.pat_ID)

        return (beaconsCompatibles[0].depart.timestamp() + patient.stayingTime)-  dt.datetime.now().timestamp()

    def attTime(time):
        return (dt.datetime.now().timestamp() - time.timestamp())
        
    def showTotalFreeBeds():
        beacons = get_beac_all()
        
        freeBeds = 0
        for beacon in beacons:
            newBeac = CreateBeacon(beacon)
            freeBeds = freeBeds + newBeac.bedsFree
            print( "Room: " + newBeac.room + ' '*(30-len(newBeac.room)) + "Free beds:" + str(newBeac.freeBeds))

        print('\n' + "The total amount of free beds in the hospital is: " + str(freeBeds) + '\n')
        input("Press something to continue")
        os.system('cls')

    def addPatientQueue():
        print("Ask the patient informations"+"\n")
        id = input("ID of the Patient: ")
        name = input("Name of the Patient: ")
        priority = 0.0
        arrive = dt.datetime.now()
        depart = dt.datetime.now()
        stayingTime = input("How many days is he staying: ")
        type = input("Type of the Patient(Regular, Urgency, Covid-19): ")
        disease = input("Disease of the Patient(influenza H3N2, Covid-19): ")
        specs = input("Specifications of the Patient(diabetes, high pressure): ")
        
        pat_aux = Patient(id, name, priority, arrive , depart, stayingTime, "Waiting", type, disease, specs)

        insert_pat(pat_aux)
        input("Press something to continue")

    def checkQueue():
        patients = get_pat_all()
        
        sorted(patients, key=lambda patient: patient[2])
        for patient in patients:
            print( "Name: " + patient[1] + ' '*(30-len(patient[1])) + "Arrive time:" + str(patient[3]) )
        print('\n')
        input("Press something to continue")
        os.system('cls')
        
    def checkQueue():
        patients = get_pat_all()
        
        sorted(patients, key=lambda patient: patient[2])
        for patient in patients:
            print( "Name: " + patient[1] + ' '*(30-len(patient[1])) + "Arrive time:" + str(patient[3]) )
        print('\n')
        input("Press something to continue")
        os.system('cls')
    
    def getKeyboard():
        #this is boolean for whether the keyboard has bene hit
        x = msvcrt.kbhit()
        if x:
            #getch acquires the character encoded in binary ASCII
            ret = msvcrt.getch()
        else:
            ret = False
        return ret
