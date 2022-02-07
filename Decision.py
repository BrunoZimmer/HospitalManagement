import datetime
from decisionClass import Decision as Dec
import Database.Source.DataTypesFunctions as db
from Classes.patient import *
from Classes.beacon import *
from Classes.connection import *
import os
""" So here it going to be user a Decision maker 
    It will utilize the priority level and always search a room to the person with the highest priority

    The priority is going to be actualize in each minute and it will consider the disease, the waiting
    time and the specs.

    For each Decision we will find in the group of the beacons/rooms which one can comply every specs 
    of the person and in these room which is the highest cost-benefit ratio(cheapear)  
 """
 
""" 
pat_aux = Patient(
    "121",
    "Bruno Zimmer",
    0,
    datetime.now(),
    datetime.now()+ timedelta(days = 1),
    2,
    "Waiting",
    "Emergency",
    "influenza H3N2",
    "No specifications"
) """


# def patPriority(Patient pat):
#     return part.waitingTime
time  = datetime.datetime.now()
permission = 1
os.system('cls')

while(1):

    #acquire the keyboard hit if exists
    option = Dec.getKeyboard() 
    
    #if we got a keyboard hit
    if option == False and permission == 1:

        print("Choose the action:")
        #print total of free beds
        print("1 - Show total amount of free beds in the Hospital:")
        #add a patient to the queue
        print("2 - Add a patient in the queue:")
        #send the patient with the greatest priority to the room
            #tentar encontrar uma sala vazia para o paciente 
            #se nao encontrar dizer o tempo que vai demorar pra encontrar baseado no tempo estimado das pessoas que tao no quarto   
        print("3 - Check the queue:")
        #check probably waiting time
        permission = 0

    if option != False:

        #we got the key!
        #because option is a binary, we need to decode to string
        #use the decode() which is part of the binary object
        #by default, decodes via utf8
        #concatenation auto adds a space in between
        print ( option.decode())
    
    #if it does not have a response in 60 seconds it is going to 


        if(option.decode() == str(1)):
            Dec.showTotalFreeBeds()

        if(option.decode() == str(2)):
            Dec.addPatientQueue()

        if(option.decode() == str(3)):
            Dec.checkQueue()

        time = datetime.now()
        permission = 1
        
    if(Dec.attTime(time) > 2):
        Dec.updatePatients(time)
        time = datetime.datetime.now()






# print(pat_aux.typePriority)
# print(pat_aux.waitingPriority)
# print(pat_aux.waitingTime)

# print(db.get_max_priority()[0])
