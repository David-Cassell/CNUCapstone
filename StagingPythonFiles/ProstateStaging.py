import mysql.connector

import init

stagingDictionary = {}

clinpath = r'stagingTextFiles\clinicalprostateStaging.txt'
pathpath = r'stagingTextFiles\pathologicalProstateStaging.txt'


def getValues(requestDict):
    classification = requestDict.get("type")
    nValue = requestDict.get('Lymph')
    if classification == "c":
        tValue = requestDict.get("Clin-T-Value")
        mets = requestDict.get("Clin-Metas")
    else:
        tValue = requestDict.get("Path-T-Value")
        mets = requestDict.get("Path-Metas")
    Psa = requestDict.get("PSA-Value")
    gleason = requestDict.get("Gleason")
    final_stage = stage(classification, tValue, nValue, mets, Psa, gleason)

    return final_stage


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})

    # print("it was read")
    file.close()


def stage(classification, tValue, nValue, mets, psa, gleason):
    if classification == "p":
        read_in(pathpath)
    elif classification == "c":
        read_in(clinpath)

    if tValue == "T3" or tValue == "T3a" or tValue == "T3b" or tValue == "T4":
        psa = "E"
    if gleason == "5" or nValue == "N1" or mets == "M1":
        psa = "E"

    to_calculate = tValue + nValue + mets + psa + gleason
    istage = stagingDictionary.get(to_calculate, "0")
    stagingDictionary.clear()
    return to_calculate, istage

def input_into_database(requestDict, stage):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database = "capstone"
    )

    mycursor = mydb.cursor()
    hName = requestDict.get("HospitalName")
    hAddress = requestDict.get("HospitalAddress")

    patient_gender = requestDict.get("Gender")
    patient_id = init.patientID

    # that way it always goes up and should not be the same
    init.patientID += 1
    sql_stuff = "insert into Prostate(ProstateClass, breastTValue, breastGrade, breastMets, breastLymph, breastER, " \
                "breastHER2, breastPER, breastStage)" \
                " values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    hospital_sql = "insert into Hospital(hName, hAddress) values (%s,%s)"
    hospital_values = (hName, hAddress)

    patient_sql = "insert into Patient(pGender, pID,hospitalName,hospitalAddress) values(%s,%s,%s,%s)"
    patient_values = (patient_gender, patient_id, hName, hAddress)

    try:
        mycursor.execute(hospital_sql, hospital_values)
    except mysql.connector.errors.IntegrityError:
        pass
    mycursor.execute(patient_sql, patient_values)