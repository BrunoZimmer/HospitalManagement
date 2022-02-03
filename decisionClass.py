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
        
        for waitingPatient in waitingPatients:
            print(waitingPatient)
            update_depart(waitingPatient.name, waitingPatient.id, waitingPatient.arrival, dt.datetime.now())
            update_priority(waitingPatient.id, waitingPatient.makepriority)
            

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
        
        pat_1 = Patient(id, name, priority, arrive , depart, stayingTime, type, disease, specs)

        insert_pat(pat_1)
        input("Press something to continue")

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
