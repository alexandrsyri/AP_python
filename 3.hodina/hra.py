import random
cislo = random.randint(100,500)
unik = False
pokusy = 3

while pokusy > 0 and not unik:

    print("máš", pokusy, "pokusy")
    print("1 - Prohledat stůl")
    print("2 - Kouknout pod koberec")
    print("3 - Otevřít dveře")

    volba = input("Co uděláš?")

    if volba == "1":
        print("našel jsi kód", cislo)
    elif volba == "2" :
        print("nic tu není")
    elif volba == "3":
        kód = float(input("zadejte kód"))
        if kód == cislo:
            unik = True
        else:
           print("špatný kód")
           pokusy=pokusy-1

    else:
        print("neplatná možnost")

if unik == True:
    print("unikl jsi") 
else:
    print("prohrál jsi")       