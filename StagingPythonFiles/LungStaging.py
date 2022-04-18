import mysql.connector
import init

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

    stagingDictionary.clear()
    return to_calculate, istage


def input_into_database(requestDict, stage):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database="capstone"
    )

    mycursor = mydb.cursor()

    hName = requestDict.get("HospitalName")
    hAddress = requestDict.get("HospitalAddress")

    patient_gender = requestDict.get("Gender")
    patient_id = init.patientID

    # that way it always goes up and should not be the same
    init.patientID += 1

    classs = requestDict.get("type")
    tValue = requestDict.get("T-Value")
    nValue = requestDict.get('Lymph')
    if classs == "c":
        mets = requestDict.get("Clin-Metas")
    else:
        mets = requestDict.get("Path-Metas")
    lung_sql_stuff = "insert into Lung(patientID, lungClass, lungTValue, lungMets, lungLymph, lungStage, " \
                     " values (%s, %s, %s, %s, %s, %s)"
    lung_values = (patient_id, classs, tValue, mets, nValue, stage)
    hospital_sql = "insert into Hospital(hName, hAddress) values (%s,%s)"
    hospital_values = (hName, hAddress)

    patient_sql = "insert into Patient(pGender, pID,hospitalName,hospitalAddress) values(%s,%s,%s,%s)"
    patient_values = (patient_gender, patient_id, hName, hAddress)

    try:
        mycursor.execute(hospital_sql, hospital_values)
    except mysql.connector.errors.IntegrityError:
        pass
    mycursor.execute(patient_sql, patient_values)
    mycursor.execute(lung_sql_stuff, lung_values)

    mydb.commit()
