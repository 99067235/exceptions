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
def pizza():
    try:
        aantalSmall = float(input("Hoeveel small pizza's wil je? "))
        print("Dit kost", aantalSmall * small)

        aantalMedium = float(input("Hoeveel medium pizza's wil je? "))
        print("Dit kost", aantalMedium * medium)

        aantalLarge = float(input("Hoeveel large pizza's wil je? "))
        print("Dit kost", aantalLarge * large)

        print("--------------------------------------")
        print("| Uw bestelling:")
        print(f"| {aantalMedium} medium: €", aantalMedium * medium)
        print(f"| {aantalSmall} small: ","€", aantalSmall * small)
        print(f"| {aantalLarge} large: ","€", aantalLarge * large)
        print("|")
        print("| Totaalprijs = €", aantalSmall * small + aantalMedium * medium + aantalLarge * large)
        print("--------------------------------------")
        
    except ValueError:
        print("Vul a.u.b. een getal in.")
        print()
        pizza()

pizza()