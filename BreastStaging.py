stagingPathological = {}
stagingClinical = {}


def clinical_def():
    return 0


def pathological_def():
    return 0


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


def clinical_lymph_node():
    category = "cNX"

    return category


if __name__ == '__main__':
    classification = input("Is it clinical(C) or pathological(P): ")
    classification.lower()
    g = size_of_tumor()
    T_value = g[0]
    h = g[1]
    if 1.9 >= float(h) > 1.0:
        h = "2"
    if classification == 'c':
        clinical_def()
    elif classification == 'p':
        pathological_def()
    Nvalue = input("please input the lymphNode value: ")
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
        to_calculate = (T_value, Nvalue, metastasis, grade, HER2, ER, PR)
        stage = stagingPathological.get(to_calculate, "0")
    else:
        stage = "IV"
    print("Your final classification is a: " + classification + T_value + Nvalue + metastasis + grade
          + HER2 + ER + PR + " which means you are at a stage: " + stage)
