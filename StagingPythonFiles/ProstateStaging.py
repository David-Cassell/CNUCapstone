#import mysql.connector
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
        password="R5eu12o$"
    )
    if mydb.is_connected():
        print("Connected")
    else:
        print("Not connected")
    mycursor = mydb.cursor()
    mycursor.execute("use capstone")

    sql_stuff = "insert into Prostate(ProstateClass, breastTValue, breastGrade, breastMets, breastLymph, breastER, " \
                "breastHER2, breastPER, breastStage)" \
                " values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql_stuff, (classs, T_value, metastasis, Nvalue, stage))