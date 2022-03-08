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
    except ValueError:
        print("Daar snap ik niks van, we gaan even een stukje terug.")
        man()

def vrouw():
    global geslaagd
    global antwoord
    try:
        if antwoord =="V":
            antwoord = input("heeft u rood krulhaar? Y/N ").upper()
            if antwoord =="Y":
                antwoord = int(input("Hoelang is uw rode krulhaar in cm? "))
                if antwoord >= 20:
                    antwoord = int(input("Hoelang bent u in cm? "))
                    if antwoord >= 150:
                        input("hoevaak heeft u aan uw grote teen gelikt? ")
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
    except ValueError:
        print("Daar snap ik niks van, we beginnen even opnieuw.")
        vrouw()

def mboDiploma():
    global antwoord
    input("heeft u weleens kattenharen op brood gesmeerd? ")
    try:
        antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N ").upper()
        if antwoord =="Y":
            antwoord = int(input("welk niveau? "))
            if antwoord >= 4:
                pass
    except ValueError:
        raise NameError("Ziet u wel! U hebt wel een raam van hout!")
    try:
        antwoord = input("Bent u in bezit van een hoge hoed? Y/N ").upper()
        if antwoord == "Y":
            antwoord = input("Bent u man of vrouw? M/V ").upper()
            if antwoord == "M":
                man()
            elif antwoord == "V":
                vrouw()
            else:
                print("Dat snap ik niet, we gaan even een stukje terug.")
                mboDiploma()
    except:
        print("daar snap ik niks van")
        mboDiploma()

def sollicitatie():
    global geslaagd, antw1, antw2, name
    try:
        name = input("wat is uw naam? ")
        if name == "De enderdraak":
            raise NameError("De enderdraak is niet geaccepteerd")
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
    except:
        print("Dat snap ik niet, we gaan even een stukje terug.")
        sollicitatie()


    geslaagd = False
    if antw1 or antw2 == True:
        mboDiploma()

sollicitatie()

if geslaagd == True:
    print("Gefeliciteerd", name, "! U hebt het certificaat: Overleven met gevaarlijk personeel!")
else:
    print("Sorry", name, ", maar u bent niet geschikt voor het beroep ruimtevuilnisman")