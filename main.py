import time

#Grundlæggende matematik.
def basic():
    #Her modtages værdierne
    print("Det her virker kun med helt simple stykker (så ikke mere end 2 forskellige tal)")
    #Note to self: måske kunne man bruge endnu en liste, til at finde operatorenes positioner, og derfra lave længere
    #udregniner mulige. Værd at undersøge.
    regnestykke = input("Skriv regnestykket (med mellemrum mellem symbolerne): ")
    indhold = regnestykke.split(" ")

    #baseret på brugte værdier, udregnes matematikken her.
    if "+" in indhold:
        indhold.remove("+")
        print(float(indhold[0])+float(indhold[1]))
    elif "*" in indhold:
        indhold.remove("*")
        print(float(indhold[0]) * float(indhold[1]))
    elif "-" in indhold:
        indhold.remove("-")
        print(float(indhold[0]) - float(indhold[1]))
    elif "/" in indhold:
        indhold.remove("/")
        print(float(indhold[0]) / float(indhold[1]))


    #print(indhold)
    #Genstart hele programmet
    time.sleep(3)
    print(" ")
    oprtn()

#Etablering af mulige operationer.
def oprtn():
    print("mulige operationer: foreløbigt kun 'basic math'")
    operation = input("Vælg en matematisk operation: ")
    operation = operation.lower() #Reducerer risiko mht. case-sensitivity
    print(operation)

    #Vælg metode til udregning
    if operation == "basic math":
        basic()

#Kør
oprtn()

