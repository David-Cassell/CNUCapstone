import init

import mysql.connector

stagingDictionary = {}

path = r'stagingTextFiles\bladderStaging.txt'


def getValues(requestDict):
    Ttype = requestDict.get('type')
    Tvalue = requestDict.get('T-Value')
    if Ttype == "c":
        Mvalue = requestDict.get('Clin-Metas')
    else:
        Mvalue = requestDict.get('Path-Metas')
    if Mvalue == "M1":
        Mvalue = "M1a"
    Nvalue = requestDict.get('Lymph')
    final_stage = stage(Tvalue, Nvalue, Mvalue)
    return final_stage


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})
        # print(stagingDictionary)
    #print("it was read")
    file.close()


def stage(TValue, NValue, MValue):
    read_in(path)
    to_calculate = TValue + NValue + MValue
    #print(to_calculate)
    stage = stagingDictionary.get(to_calculate, "0")
    #print(stage)
    stagingDictionary.clear()
    return to_calculate, stage


def input_into_database(requestDict, stage):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database="capstone"
    )

    mycursor = mydb.cursor()

    hName = requestDict.get("HospitalName", "Not given")
    hAddress = requestDict.get("HospitalAddress", "Not Given")

    Ttype = requestDict.get('type')
    Tvalue = requestDict.get('T-Value')
    if Ttype == "c":
        Mvalue = requestDict.get('Clin-Metas')
    else:
        Mvalue = requestDict.get('Path-Metas')
    if Mvalue == "M1":
        Mvalue = "M1a"
    Nvalue = requestDict.get('Lymph')

    patient_gender = requestDict.get("Gender")
    patient_id = init.patientID

    # that way it always goes up and should not be the same
    init.patientID += 1

    bladder_values = (patient_id,Ttype, Tvalue, Mvalue, Nvalue, stage)
    bladder_sql_stuff = """insert into Bladder(patientID,BladderClass, bladderTValue, bladderMets, bladderLymph, bladderStage) 
    values (%s, %s, %s, %s, %s, %s) """

    patient_sql = "insert into Patient(pGender, pID,hospitalName,hospitalAddress) values(%s,%s,%s,%s)"
    patient_values = (patient_gender,patient_id,hName,hAddress)

    mycursor.execute(patient_sql,patient_values)
    mycursor.execute(bladder_sql_stuff, bladder_values)

    mydb.commit()

