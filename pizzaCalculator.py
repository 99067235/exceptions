#Jurrian Schouten
#Pizza calculator

from cmath import pi
from multiprocessing.sharedctypes import Value


small = 3.99
medium = 5.00
large = 6.00

#klant krijgt de prijzen te zien.
print("""Prijzen in euro's
small = 3.99
medium = 5
large = 6""")

def kassabon():
    my_formatter = "{0:.2f}"
    formatted_total = my_formatter.format(aantalSmall * small + aantalMedium * medium + aantalLarge * large)
    print("--------------------------------------")
    print("| Uw bestelling:")
    print(f"| {aantalSmall} small: ","€", formatted_prijssmall)
    print(f"| {aantalMedium} medium: €", formatted_prijsmedium)
    print(f"| {aantalLarge} large: ","€",formatted_prijslarge)
    print("|")
    print("| Totaalprijs = €", formatted_total)
    print("--------------------------------------")
def pizza():
    my_formatter = "{0:.2f}"
    global aantalSmall, aantalMedium, aantalLarge, formatted_prijslarge, formatted_prijsmedium, formatted_prijssmall
    try:
        aantalSmall = float(input("Hoeveel small pizza's wil je? "))
        prijssmall = aantalSmall * small
        formatted_prijssmall = my_formatter.format(prijssmall)
        print("Dit kost", formatted_prijssmall)

        aantalMedium = float(input("Hoeveel medium pizza's wil je? "))
        prijsmedium = aantalMedium * medium
        formatted_prijsmedium = my_formatter.format(prijsmedium)
        print("Dit kost", formatted_prijsmedium)

        aantalLarge = float(input("Hoeveel large pizza's wil je? "))
        prijslarge = aantalLarge * large
        formatted_prijslarge = my_formatter.format(prijslarge)
        print("Dit kost", formatted_prijslarge)

        kassabon()

        
    except ValueError:
        print("Vul a.u.b. een getal in.")
        print()
        pizza()

pizza()