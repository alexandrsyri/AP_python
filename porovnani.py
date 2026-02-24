x = float(input("Zadejte prvni cislo "))
y = float(input("Zadejte druhé číslo "))
if x > y:
    #print(x +"je větší" +y ) nefunkcni
    #print(x, "je větší než", y)
    print(f"{x} je větší než {y}")
elif x==y:
    print("čísla jsou stejná")
else:
    print(f"{y} je větší než {x}")

    


