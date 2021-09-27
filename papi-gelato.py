print("Welkom bij Papi Gelato je mag alle smaken ijs kiezen zolang het maar vanille ijs is.")

meer = "Hier is uw {} met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)"
error = "Sorry dat snap ik niet..."

while True:
    bolletjes = input("Hoeveel bolletjes wilt u?")
    if int(bolletjes) in range(1,9):
        if int(bolletjes) in range(1,4):
            stap2 = input("Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje".format(bolletjes)).lower()
            if stap2 == "a":
                meer = input(meer.format("hoorntje",bolletjes)).lower()
            elif stap2 == "b":
                meer = input(meer.format("bakje",bolletjes)).lower()
            else:
                print(error)
        elif int(bolletjes) in range(4,9):
            print("Dan krijgt u van mij een bakje met {} bolletjes".format(bolletjes))
            meer = input(meer.format("bakje",bolletjes)).lower()
        if meer == "y":
            continue
        elif meer == "n":
            print("Bedankt en tot ziens!")
            quit()
        else:
            print(error)
    elif int(bolletjes) > 8:
        print("Sorry, zulke grote bakken hebben we niet")
    else:
        print(error)