stagingPathological = {}
stagingClinical = {}


def clinical_def():
    return 0


def pathological_def():
    return 0


def size_of_tumor():
    definition = "TX"
    size = " "
    assessed = input("can the tumor be assessed?(y/n) ")
    if assessed == 'n':
        return definition, size
    size = input("What is the size of the tumor: ")
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
    return definition, size


if __name__ == '__main__':
    classification = input("Is it clinical(C) or pathological(P): ")
    classification.lower()
    g = size_of_tumor()
    s = g[0]
    h = g[1]
    if 1.9 >= float(h) > 1.0:
        h = "2"
    if classification == 'c':
        clinical_def()
    elif classification == 'p':
        pathological_def()
    # final classification will be as such: [T, N, M, G, HER2, ER, PR]
    print("Your final classification is a: "+classification+s)
