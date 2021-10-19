def afisatiDacasegaseste():
    '''
    determina daca un sir se gaseste in lista
    :return: da,daca se gaseste si nu,in caz contrar
    '''
def stringPalindrome(l):
    '''
    determina daca un string este palindrom
    :return: daca sirurile sunt palindroame
    '''

def citireLista():
    l = []
    givenString = input("dati lista")
    numbersAsStrings= givenString.split(",")
    for x in numbersAsStrings:
        l.append(x)
    return l
def main():
    l = []
    while True:
        print("1.citirea listei")
        print("x.afisare lista")
        print("3.string palindrom")
        print("a.iesire")
        optiune = input("dati optiunea:")
        if optiune == "1":
            l = citireLista()
        if optiune == "x":
            print(l)
        if optiune == "a":
            break
main()