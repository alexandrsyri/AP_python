nejvyssi = int(input("zadejte cislo"))
cislo = 0
for i in range(9): 
    cislo = int(input("Zadejte číslo"))
    if cislo > nejvyssi:
        nejvyssi = cislo

print(nejvyssi)