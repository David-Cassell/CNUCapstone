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
    print("it was read")
    file.close()


def stage(TValue, NValue, MValue):
    read_in(path)
    to_calculate = TValue + NValue + MValue
    print(to_calculate)
    stage = stagingDictionary.get(to_calculate, "0")
    print(stage)
    stagingDictionary.clear()
    return to_calculate, stage

def input_into_database(requestDict, stage):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database="capstone"
    )
    if mydb.is_connected():
        print("Connected")
    else:
        print("Not connected")
    mycursor = mydb.cursor()

    hName = requestDict.get("HospitalName")
    print(hName)
    hAddress = requestDict.get("HospitalAddress")
    print(hAddress)
    hospital_sql = "insert into Hospital(hName, hAddress) values (%s,%s)"
    hospital_values = (hName,hAddress)
    bladder_sql_stuff = "insert into Prostate(ProstateClass, breastTValue, breastGrade, breastMets, breastLymph, breastER, " \
                "breastHER2, breastPER, breastStage)" \
                " values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(hospital_sql,hospital_values)
    mydb.commit()

    mycursor.execute("Select * from hospital")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
