def getal():
    try:
        FirstNumber = int(input("geef een getal op: "))
        SecondNumber = int(input("geef een tweede getal op: "))
    except ValueError:
        print("dat is geen getal...")
        getal()
    else:
        calculation = FirstNumber * SecondNumber
        print(calculation)
getal()