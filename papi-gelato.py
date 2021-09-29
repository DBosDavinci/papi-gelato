print("Welkom bij Papi Gelato.")
error = "Sorry, dat snap ik niet..."
bolletjes = int(input("Hoeveel bolletjes wilt u?"))
keuze = ""
hoorntje = False
bakje = False
topping = False
hoorntjeHoeveelheid = 0
bakjeHoeveelheid = 0
bolletjesHoeveelheid = 0
toppingsTotaal = 0

def Smaak():
    global bolletjes
    for x in range(1,bolletjes+1):
        smaak = input("Welke smaak wilt u voor bolletje nummer {}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?".format(x)).lower()
        if smaak == "a":
            print("Bolletje {} is aardbei".format(x))
        elif smaak == "c":
            print("Bolletje {} is chocolade".format(x))
        elif smaak == "m":
            print("Bolletje {} is mint".format(x))
        elif smaak == "v":
            print("Bolletje {} is vanilla".format(x))
        else:
            print(error)
            Smaak()
    Stap1()

def Stap1():
    global bolletjes,bakje,bakjeHoeveelheid
    if bolletjes in range(1,4):
        Stap2()
    elif bolletjes in range(3,9):
        print("Dan krijgt u van mij een bakje met {} bolletjes".format(bolletjes))
        bakjeHoeveelheid=+1
        bakje = True
        Toppings()
    elif bolletjes > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        Stap1()
    else:
        print(error)
        Stap1()

def Stap2():
    global bolletjes,keuze,hoorntjeHoeveelheid,hoorntje,bakjeHoeveelheid,bakje
    stap2 = input("Wilt u deze {} bolletje(s) in A) hoorntje of B) een bakje?".format(bolletjes)).lower()
    if stap2 == "a":
        keuze = "hoorntje"
        hoorntjeHoeveelheid=+1
        hoorntje = True
        Toppings()
    elif stap2 == "b":
        keuze = "bakje"
        bakjeHoeveelheid=+1
        bakje = True
        Toppings()
    else:
        print(error)

def Toppings():
    global toppingsTotaal,topping
    toppings = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?").lower()
    if toppings == "a":
        toppingsTotaal=+0
        Stap3()
    elif toppings == "b":
        toppingsTotaal=+0.5
    elif toppings == "c":
        toppingsTotaal=+0.3
    elif toppings == "d":
        if keuze == "hoorntje":
            toppingsTotaal=+0.6
        elif keuze == "bakje":
            toppingsTotaal=+0.9
    else:
        print(error)
        Toppings()
    topping = True
    Stap3()

def Stap3():
    global bolletjesHoeveelheid
    meer = input("Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)".format(keuze,bolletjes)).lower()
    bolletjesHoeveelheid=+int(bolletjes)
    if meer == "y":
        Stap1()
    elif meer == "n":
        print("Bedankt en tot ziens!")
        bon()
    else:
        print(error)

def bon():
    global toppingsTotaal
    print('---------["Papi Gelato"]---------')
    bolletjesTotaal = bolletjesHoeveelheid * 1.10
    bolletjesTotaal = "{:.2f}".format(bolletjesTotaal)
    Totaal=+float(bolletjesTotaal)
    print('Bolletjes       {} x €1.10 = €{}'.format(bolletjesHoeveelheid,bolletjesTotaal))
    if hoorntje == True:
        hoorntjeTotaal = hoorntjeHoeveelheid * 1.25
        Totaal=+hoorntjeTotaal
        print('Hoorntje        {} x €1.25 = €{}'.format(hoorntjeHoeveelheid,hoorntjeTotaal))
    if bakje == True:
        bakjeTotaal = bakjeHoeveelheid * 0.75
        Totaal=+bakjeTotaal
        print('Bakje           {} x €0.75 = €{}'.format(bakjeHoeveelheid,bakjeTotaal))
    if topping == True:
        toppingsTotaal = "{:.2f}".format(toppingsTotaal)
        Totaal=+toppingsTotaal
        print('Topping         1 x €{} = €{}'.format(toppingsTotaal,toppingsTotaal))
    print('                          -------- +')
    print('Totaal                    = €{}'.format(Totaal))

Smaak()