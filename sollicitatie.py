geslaagd = False

def man():
    global geslaagd
    try:
        antwoord = input("Heeft u een snor? Y/N ").upper()
        if antwoord =="Y":
            antwoord = int(input("Hoe breed bent u met snor? "))
            if antwoord >= 10:
                antwoord = int(input("Hoelang bent u in cm? "))
                if antwoord >= 150:
                    antwoord = int(input("Hoeveel weegt u in kg? "))
                    if antwoord >= 90:
                        antwoord = float(input("Welke schoenmaat heeft u? "))
                        if antwoord >= 40:
                            antwoord = int(input("Hoeveel huisdieren heeft u? "))
                            if antwoord <= 4:
                                antwoord = (input("Welke kleur vind u mooier: blauw of oranje? "))
                                if antwoord == "blauw":
                                    antwoord = int(input("Hoever kunt u springen in cm? "))
                                    if antwoord >= 100:
                                        geslaagd = True
    except ValueError():
        print("Daar snap ik niks van, we beginnen even opnieuw.")
        man()

def vrouw():
    global geslaagd
    try:
        if antwoord =="V":
            antwoord = input("heeft u rood krulhaar? Y/N ").upper()
            if antwoord =="Y":
                antwoord = int(input("Hoelang is uw rode krulhaar in cm? "))
                if antwoord >= 20:
                    antwoord = int(input("Hoelang bent u in cm? "))
                    if antwoord >= 150:
                        antwoord = int(input("Hoeveel weegt u in kg? "))
                        if antwoord >= 90:
                            antwoord = float(input("Welke schoenmaat heeft u? "))
                            if antwoord >= 40:
                                antwoord = int(input("Hoeveel huisdieren heeft u? "))
                                if antwoord <= 4:
                                    antwoord = (input("Welke kleur vind u mooier: blauw of oranje? "))
                                    if antwoord == "blauw":
                                        antwoord = int(input("Hoever kunt u springen in cm? "))
                                        if antwoord >= 100:
                                            geslaagd = True
    except ValueError():
        print("Daar snap ik niks van, we beginnen even opnieuw.")
        vrouw()

def mboDiploma():
    input("heeft u weleens kattenharen op brood gesmeerd? ")
    try:
        antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N ").upper()
        if antwoord =="Y":
            antwoord = int(input("welk niveau? "))
            if antwoord >= 4:
                pass
    except ValueError():
        raise NameError("ik wist het wel")
    try:
        antwoord = input("Bent u in bezit van een hoge hoed? Y/N ").upper()
        if antwoord == "Y":
            antwoord = input("Bent u man of vrouw? M/V ").upper()
            if antwoord == "M":
                man()
            else:
                vrouw()
    except ValueError():
        print("daar snap ik niks van")
        mboDiploma()

def sollicitatie():
    global geslaagd
    try:
        name = input("wat is uw naam? ")
        if name == "John":
            raise NameError("John is niet geaccepteerd")
        else:
            pass

        antw1 = int(input("Hoelang heeft u ervaring met jongleren? "))
        if antw1 == 5:
            antw1 = True
        elif antw1 == 69:
            raise NameError("Dat meent u niet!")
        else:
            antw1 = False
        antw2 = int(input("Hoelang heeft u praktijkervaring met acrobatiek? "))
        if antw2 > 3:
            antw2 = True
        else:
            antw2 = False
    except ValueError():
        print("Dat is geen nummer")
        sollicitatie()


    geslaagd = False
    if antw1 or antw2 == True:
        mboDiploma()

sollicitatie()

if geslaagd == True:
    print("Gefeliciteerd! U hebt het certificaat: Overleven met gevaarlijk personeel!")
else:
    print("Sorry, maar u bent niet geschikt voor het beroep ruimtevuilnisman")