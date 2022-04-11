stagingDictionary = {}

path = r'stagingTextFiles\colonStaging.txt'


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
