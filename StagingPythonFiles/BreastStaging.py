import mysql.connector

import init

stagingDictionary = {}

# from stagingTextFiles import
clinical_path = r'stagingTextFiles\clinicalBreastStaging.txt'
pathological_path = r'stagingTextFiles\pathologicalBreastStaging.txt'


def getValues(requestDict):
    tvalue = get_initial_T(requestDict)
    classification = requestDict.get('type')
    if classification == 'c':
        nvalue = requestDict.get('Clin-Lymph')
    else:
        nvalue = requestDict.get('path-Lymph')
    mets = requestDict.get('Metas')
    grade = requestDict.get('Grade')
    HER2 = requestDict.get('Her2')
    ER = requestDict.get('Er')
    PR = requestDict.get('Pr')
    # print(classification + " " + tvalue + " " + nvalue + " " + mets + " " + grade + " " + HER2 + " " + ER + " " + PR)
    stage = calculate(classification, tvalue, nvalue, mets, grade, HER2, ER, PR)
    return stage


def get_initial_T(requestDict):
    size = requestDict.get("T-Value")

    if "chest" in requestDict:
        chest = "y"
    else:
        chest = "n"

    if "skin" in requestDict:
        skin = "y"
    else:
        skin = "n"

    if "infla" in requestDict:
        infla = "y"
    else:
        infla = "n"

    return size_of_tumor(size, chest, skin, infla)


def size_of_tumor(size, chest, skin, infla):
    definition = "TX"
    # my defence against SQL injection, makes it so if you stage something
    # without a size it will stage it as a defaulted TX
    try:
        if float(size) <= 1.0:
            definition = "T1mi"
        elif 1.0 < float(size) <= 5.0:
            definition = "T1a"
        elif 5.0 < float(size) <= 10.0:
            definition = "T1b"
        elif 10 < float(size) <= 20.0:
            definition = "T1c"
        elif 20 < float(size) <= 50:
            definition = "T2"
        elif float(size) > 50.0:
            definition = "T3"

        if chest == "y" and skin == 'n':
            return definition
        else:
            definition = "T4"
            isTA = chest
            isTB = skin
            if isTA == 'y' and isTB == 'n':
                return "T4a"

            elif isTA == 'n' and isTB == 'y':
                return "T4b"

            elif isTA == 'y' and isTB == 'y':
                return "T4c"

            if infla == 'y':
                return "T4d"
    except ValueError:
        return definition


def input_into_database(requestDict, stage):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database="capstone"
    )

    tvalue = get_initial_T(requestDict)
    classification = requestDict.get('type')
    if classification == 'c':
        nvalue = requestDict.get('Clin-Lymph')
    else:
        nvalue = requestDict.get('path-Lymph')
    mets = requestDict.get('Metas')
    grade = requestDict.get('Grade')
    HER2 = requestDict.get('Her2')
    ER = requestDict.get('Er')
    PR = requestDict.get('Pr')

    mycursor = mydb.cursor()

    hName = requestDict.get("HospitalName", "Not given")
    hAddress = requestDict.get("HospitalAddress", "Not Given")

    patient_gender = requestDict.get("Gender")
    patient_id = init.patientID

    # that way it always goes up and should not be the same
    init.patientID += 1
    sql_stuff = """insert into Breast(patientID,breastClass, breastTValue, breastGrade, breastMets, breastLymph, breastER, 
                breastHER2, breastPER, breastStage)
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    breast_values = (patient_id, classification, tvalue, grade, mets, nvalue, ER, HER2, PR, stage)
    patient_sql = "insert into Patient(pGender, pID,hospitalName,hospitalAddress) values(%s,%s,%s,%s)"
    patient_values = (patient_gender, patient_id, hName, hAddress)

    mycursor.execute(patient_sql, patient_values)
    mycursor.execute(sql_stuff, breast_values)

def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})
    file.close()


def calculate(classification, T_value, Nvalue, metastasis, grade, HER2, ER, PR):
    if classification == 'c':
        read_in(clinical_path)
    elif classification == 'p':
        read_in(pathological_path)

    to_calculate = " "
    # final classification will be as such: [T, N, M, G, HER2, ER, PR]
    if T_value.__contains__("T1"):
        T_value = "T1"
    if T_value.__contains__("T4"):
        T_value = "T4"
    if metastasis != "M1":
        if Nvalue == "N3":
            T_value = "T"
        to_calculate = T_value + Nvalue + metastasis + grade + HER2 + ER + PR
        print(to_calculate)
        stage = stagingDictionary.get(to_calculate, "0")
    # print(stage)
    else:
        to_calculate = T_value + Nvalue + metastasis + grade + HER2 + ER + PR
        print(to_calculate)
        stage = "IV"
    stagingDictionary.clear()
    return to_calculate, stage

    # print("Your final classification is a: " + classification + to_calculate
    #      + " which means you are at a stage: " + stage)
