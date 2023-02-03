import time
import math

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
        print(indhold[0], " + ", indhold[1], " = ", float(indhold[0])+float(indhold[1]))
    elif "*" in indhold:
        indhold.remove("*")
        print(indhold[0], " * ", indhold[1], " = ", float(indhold[0]) * float(indhold[1]))
    elif "-" in indhold:
        indhold.remove("-")
        print(indhold[0], " - ", indhold[1], " = ", float(indhold[0]) - float(indhold[1]))
    elif "/" in indhold:
        indhold.remove("/")
        print(indhold[0], " / ", indhold[1], " = ", float(indhold[0]) / float(indhold[1]))

    #Her genstartes programmet.
    time.sleep(1)
    print("")
    oprtn()

def ekspn():
    print("Input værdier. '+' tages som eksponenter, '-' bruges til rødder, og kan indtil videre kun bruges til kvadratrødder ved enkelte tal. Husk mellemrum mellem symboler")
    #Her splittes inputtet i en liste
    regnestykke = input("værdier: ")
    indhold = regnestykke.split(" ")

    #Her sorteres listen efter brugbare værdier, for at afgøre operationen.
    if "+" in indhold:
        indhold.remove("+")
        print(indhold[0], " ^ ", indhold[1], " = " ,float(indhold[0]) ** float(indhold[1]))
    if "-" in indhold:
        indhold.remove("-")
        print("kvadratroden af ", indhold[0], "er " , math.sqrt(float(indhold[0])))

    #Her genstartes programmet.
    time.sleep(1)
    print("")
    oprtn()


#Etablering af mulige operationer.
def oprtn():
    print("mulige operationer: 'basic math' & 'eksponentielt'")
    operation = input("Vælg en matematisk operation: ")
    operation = operation.lower() #Reducerer risiko mht. case-sensitivity
    print(operation)

    #Vælg metode til udregning
    if operation == "basic math":
        print("")
        basic()
    elif operation == "eksponentielt":
        print("")
        ekspn()
    # "end" afslutter programmet.
    elif operation == "end":
        return
    #Backup, i tilfælde af fejlinput, eller hvis folk bliver for kreative.
    else:
        print("Fejlinput, prøv igen")
        time.sleep(1)
        print("")
        oprtn()

#Kør
oprtn()

