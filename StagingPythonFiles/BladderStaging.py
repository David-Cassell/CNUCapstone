stagingDictionary = {}

path = r'stagingTextFiles\bladderStaging.txt'
def getValues(requestDict):
    #print("This triggered")
    Tvalue = requestDict.get('T-Value')
    Mvalue = requestDict.get('Metas')
    Nvalue = requestDict.get('Lymph')
    final_stage = stage(Tvalue,Nvalue,Mvalue)
    return final_stage


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})
        #print(stagingDictionary)
    print("it was read")
    file.close()


def stage(TValue, NValue, MValue):
    read_in(path)
    to_calculate = TValue+NValue+MValue
    print(to_calculate)
    stage = stagingDictionary.get(to_calculate, "0")
    print(stage)
    return stage

