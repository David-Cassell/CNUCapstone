stagingDictionary = {}


def clinical_lymph_def():
    category = "NX"
    assessed = input("can the lymph nodes be assessed (y/n)?")
    if assessed == "n":
        return category
    are_they_there = input("Has there been any presence of a lymph node metastasis by "
                           "either imaging or clinical examination(y/n)?")
    if are_they_there == "n":
        category = "N0"
        return category

    check_if_n1 = input("Is the metastasis movable ipsilateral in Level I or II axillary lymph nodes (y/n)?")
    if check_if_n1 == "y":
        category = "N1"
        check_mi = input("Are there any micrometastises (around 200 cells but none larger than 2mm) (y/n)?")
        if check_mi == "y":
            category = "N1mi"
        return category

    return category


def pathological_lymph_def():
    category = "NX"

    return category


def t_suffix(definition):
    # not worrying about the suffix yet
    # var = input("Are there synchronous tumors found in a single organ?(y/n) ")
    # var.lower()
    # if var == "y":
    # return definition+" suffix(m)"
    return definition


def size_of_tumor():
    definition = "TX"
    size = 0
    assessed = input("can the tumor be assessed?(y/n) ")
    if assessed == 'n':
        return t_suffix(definition), float(size)
    size = input("What is the size of the tumor in mm?: ")
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

    isTFour = input("Does the tumor directly extend to into the chest wall and/or the skin?(y/n) ")
    if isTFour == "n":
        return t_suffix(definition), float(size)
    else:
        definition = "T4"
        isTA = input("Does it extend into the chest wall?(y/n) ")
        isTB = input("Does it extend into the skin?(y/n) ")
        if isTA == 'y' and isTB == 'n':
            return t_suffix("T4a"), float(size)

        elif isTA == 'n' and isTB == 'y':
            return t_suffix("T4b"), float(size)

        elif isTA == 'y' and isTB == 'y':
            return t_suffix("T4c"), float(size)

        isTD = input("is it an inflammatory carcinoma?")
        if isTD == 'y':
            return t_suffix("T4d"), float(size)

    return t_suffix(definition), float(size)


def input_into_database():
    pass


def read_in(fileToRead):
    file = open(fileToRead, encoding="utf-8")

    for line in file:
        dictStage = line.split(":")
        stagingDictionary.update({dictStage[0]: dictStage[1]})
    file.close()


if __name__ == '__main__':
    classification = input("Is it clinical(C) or pathological(P): ")
    classification.lower()
    Nvalue = " "
    if classification == 'c':
        read_in("clinicalBreastStaging.txt")
        Nvalue = clinical_lymph_def()
    elif classification == 'p':
        read_in("pathologicalBreastStaging.txt")
        Nvalue = pathological_lymph_def()
    g = size_of_tumor()
    T_value = g[0]
    final_size = g[1]
    if 1.9 >= float(final_size) > 1.0:
        final_size = "2"
    to_calculate = " "
    metastasis = input("please input the metastasis value: ")
    grade = input('please input the grade (G1, G2, G3): ')
    HER2 = input('please input the HER2 (+/-): ')
    ER = input('please input the ER (+/-): ')
    PR = input('please input the PR (+/-): ')
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

    input_into_database()
    print("Your final classification is a: " + classification + to_calculate
          + " which means you are at a stage: " + stage)
