while(True):
    číslo = int(input("zadejte číslo"))
    číslo2 = int(input("zadejte číslo 2"))

    print("1. soucet \n2. součin \n3. rozdíl \n4. podíl")
    operace = int(input("zadjete číslo operace, kterou chcete provést"))

    match operace:
        case 1:
            soucet = číslo + číslo2
            print(soucet)
        case 2:
            součin = číslo * číslo2
            print(součin)
        case 3:
             rozdíl = číslo - číslo2
             print(rozdíl)
        case 4:
            if číslo2 == 0:
                print("nelze dělit nulou")
            else:
                podíl = číslo / číslo2
                print (podíl)

    konec = input("Ukončit program? Y/N")
    if konec.lower() == "y":
        break