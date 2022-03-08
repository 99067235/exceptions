
from multiprocessing.sharedctypes import Value


def onzinvraag1():
    input("heeft u weleens kattenharen op brood gesmeerd? ")
    antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N ").upper()
    if antwoord =="Y":
        antwoord = input("welk niveau? ")
        if antwoord >= 4:
            pass
        
            

def sollicitatie():
    try:
        name = input("wat is uw naam? ")
        if name == "John":
           print("yes")
        else:
            pass
    except ValueError():
        raise NameError("John is niet geaccepteerd")
        
    antwoord = int(input("Hoelang heeft u praktijkervaring met dieren-dressuur? "))
    antw1 = int(input("Hoelang heeft u ervaring met jongleren? "))
    if antw1 > 5:
        antw1 = True
    else:
        antw1 = False
    antw2 = int(input("Hoelang heeft u praktijkervaring met acrobatiek? "))
    if antw2 > 3:
        antw2 = True
    else:
        antw2 = False
    try:
        geslaagd = False
        if antwoord or antw1 or antw2 == True:
            antwoord = input("Bent u in het bezit van een diploma MBO 4 ondernemen? Y/N ").upper()
            if antwoord =="Y":
                antwoord = input("Bent u in bezit van een geldig vrachtwagenrijbewijs? Y/N ").upper()
                if antwoord =="Y":
                    antwoord = input("Bent u in bezit van een hoge hoed? Y/N ").upper()
                    if antwoord =="Y":
                        antwoord = input("Bent u man of vrouw? M/V ").upper()
                        if antwoord =="M":
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
        print("bok")

    if geslaagd == True:
        print("Gefeliciteerd! U hebt het certificaat: Overleven met gevaarlijk personeel!")
    else:
        print("Sorry, maar u bent niet geschikt voor het beroep ruimtevuilnisman")

sollicitatie()