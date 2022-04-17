import mysql.connector
stagingDictionary = {}

path = r'stagingTextFiles\lungStaging.txt'


def getValues(requestDict):
    classification = requestDict.get("type")
    tValue = requestDict.get("T-Value")
    nValue = requestDict.get('Lymph')
    if classification == "c":
        mets = requestDict.get("Clin-Metas")
    else:
        mets = requestDict.get("Path-Metas")
    final_stage = stage(tValue, nValue, mets)

    return final_stage


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})

    # print("it was read")
    file.close()


def stage(tValue, nValue, mets):
    read_in(path)
    to_calculate = tValue + nValue + mets
    istage = stagingDictionary.get(to_calculate, "0")
    # print(istage)
    stagingDictionary.clear()
    return to_calculate, istage

def input_into_database(classs, T_value, Nvalue, metastasis, stage):
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
