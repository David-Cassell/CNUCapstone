stagingDictionary = {}

#from stagingTextFiles import
clinical_path = r'stagingTextFiles\clinicalBreastStaging.txt'
pathological_path = r'stagingTextFiles\pathologicalBreastStaging.txt'


def getValues(requestDict):
    size = requestDict.get("T-Value")
    if "chest" in requestDict:
        chest = "y"
    else:
        chest = "n"

    if "skin" in requestDict:
        skin = "y"
    else:
        skin = "n"

    if "suffix" in requestDict:
        suffix = "pos"
    else:
        suffix = "neg"

    if "infla" in requestDict:
        infla = "y"
    else:
        infla = "n"
    tvalue = size_of_tumor(size, chest, skin, infla)
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
    stage = calculate(classification,tvalue,nvalue, mets,grade,HER2, ER, PR)
    return stage


def size_of_tumor(size, chest, skin, infla):
    definition = "TX"
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

    return definition


def input_into_database():
    pass


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})
    file.close()


def calculate(classification, T_value, Nvalue, metastasis, grade, HER2, ER, PR):
    pass

    if classification == 'c':
        read_in("clinicalBreastStaging.txt")
    elif classification == 'p':
        read_in("pathologicalBreastStaging.txt")

    to_calculate = " "
    # final classification will be as such: [T, N, M, G, HER2, ER, PR]
    if T_value.__contains__("T1"):
        T_value = "T1"
    if metastasis != "M1":
        if Nvalue == "N3":
            T_value = "T"
        to_calculate = T_value + Nvalue + metastasis + grade + HER2 + ER + PR
    # print(to_calculate)
        stage = stagingDictionary.get(to_calculate, "0")
    # print(stage)
    else:
        stage = "IV"
    return stage
    # input_into_database()
    # print("Your final classification is a: " + classification + to_calculate
    #      + " which means you are at a stage: " + stage)
