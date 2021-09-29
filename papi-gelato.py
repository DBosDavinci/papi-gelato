print("Welkom bij Papi Gelato")

meer = "Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)"
error = "Sorry dat snap ik niet..."
hoorntje = False
bakje = False
hoorntjeHoeveelheid = 0
bakjeHoeveelheid = 0
bolletjesHoeveelheid = 0

def HoorntjeEind():
    global hoorntje,hoorntjeHoeveelheid,bolletjesHoeveelheid
    hoorntje = True
    hoorntjeHoeveelheid=+1
    bolletjesHoeveelheid=+int(bolletjes)
    
def BakjeEind():
    global bakje,bakjeHoeveelheid,bolletjesHoeveelheid
    bakje = True
    bakjeHoeveelheid=+1
    bolletjesHoeveelheid=+int(bolletjes)

Loop = True

while Loop == True:
    bolletjes = input("Hoeveel bolletjes wilt u?")
    if int(bolletjes) in range(1,9):
        for x in range(1,(int(bolletjes)+1)):
            smaak = input("Welke smaak wilt u voor bolletje nummer {}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?".format(x)).lower()
            if smaak == "a":
                print("Bolletje {} is aardbei".format(x))
            elif smaak == "c":
                print("Bolletje {} is chocolade".format(x))
            elif smaak == "m":
                print("Bolletje {} is munt".format(x))
            elif smaak == "v":
                print("Bolletje {} is vanille".format(x))
            else:
                print(error)
        if int(bolletjes) in range(1,4):
            stap2 = input("Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje".format(bolletjes)).lower()
            if stap2 == "a":
                meer = input(meer.format("hoorntje",bolletjes)).lower()
                HoorntjeEind()
            elif stap2 == "b":
                meer = input(meer.format("bakje",bolletjes)).lower()
                BakjeEind()
            else:
                print(error)
        elif int(bolletjes) in range(4,9):
            print("Dan krijgt u van mij een bakje met {} bolletjes".format(bolletjes))
            meer = input(meer.format("bakje",bolletjes)).lower()
            BakjeEind()
        if meer == "y":
            continue
        elif meer == "n":
            print("Bedankt en tot ziens!")
            Loop = False
        else:
            print(error)
    elif int(bolletjes) > 8:
        print("Sorry, zulke grote bakken hebben we niet")
    else:
        print(error)

print('---------["Papi Gelato"]---------')
bolletjesTotaal = bolletjesHoeveelheid * 1.10
bolletjesTotaal = "{:.2f}".format(bolletjesTotaal)
print('Bolletjes   {} x €1.10  = €{}'.format(bolletjesHoeveelheid,bolletjesTotaal))
if hoorntje == True:
    hoorntjeTotaal = hoorntjeHoeveelheid * 1.25
    Totaal = hoorntjeTotaal + float(bolletjesTotaal)
    print('Hoornje     {} x €1.25  = €{}'.format(hoorntjeHoeveelheid,float(hoorntjeTotaal)))
if bakje == True:
    bakjeTotaal = bakjeHoeveelheid * 0.75
    Totaal = bakjeTotaal + float(bolletjesTotaal)
    print('Bakje       {} x €0.75  = €{}'.format(bakjeHoeveelheid,bakjeTotaal))
print('                          -------- +')
print('Totaal                    = €{}'.format(float(Totaal)))