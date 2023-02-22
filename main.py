import time
import math

#en failsafe, der kan genstarte programmet, i tilfælde af ugyldigt input. Mere effektivt end at skulle køre det igen.
def failsafe(reason):
    #Fejlbesked. Hvis en funktion aktiverer failsafe, giver det også en forsimplet error-message.
    print("Fejlinput: " + reason + ". Genstarter proces")

    #genstart, med tilstrækkeligt delay til at man kan læse error-beskeden.
    time.sleep(2)
    print("")
    oprtn()


#Grundlæggende matematik.
def basic():
    #Her modtages værdierne
    print("Det her virker kun med helt simple stykker (så ikke mere end 2 forskellige tal)")
    #Note to self: måske kunne man bruge endnu en liste, til at finde operatorenes positioner, og derfra lave længere
    #udregniner mulige. Værd at undersøge.
    regnestykke = input("Skriv regnestykket (med mellemrum mellem symbolerne): ")

    # Her kører en failsafe, hvis man bruger kommaer.
    if "," in regnestykke:
        failsafe("Brug punktum i stedet for komma")

    indhold = regnestykke.split(" ")

    #baseret på brugte værdier, udregnes matematikken her.
    if "+" in indhold: #Addition
        indhold.remove("+")
        print(indhold[0], " + ", indhold[1], " = ", float(indhold[0])+float(indhold[1]))
    elif "*" in indhold:  #multiplikation
        indhold.remove("*")
        print(indhold[0], " * ", indhold[1], " = ", float(indhold[0]) * float(indhold[1]))
    elif "-" in indhold:   #subtraktion
        indhold.remove("-")
        print(indhold[0], " - ", indhold[1], " = ", float(indhold[0]) - float(indhold[1]))
    elif "/" in indhold:   #Division
        indhold.remove("/")
        print(indhold[0], " / ", indhold[1], " = ", float(indhold[0]) / float(indhold[1]))
    else:
        failsafe("Ugyldig operation, tjek input")

    #Her genstartes programmet.
    time.sleep(1)
    print("")
    oprtn()

def ekspn():
    print("Input værdier. '+' tages som eksponenter, '-' bruges til rødder, og kan indtil videre kun bruges til kvadratrødder ved enkelte tal. Husk mellemrum mellem symboler")
    #Her splittes inputtet i en liste
    regnestykke = input("værdier: ")

    #Her kører en failsafe, hvis man bruger kommaer.
    if "," in regnestykke:
        failsafe("Brug punktum i stedet for komma")

    indhold = regnestykke.split(" ")

    #Her sorteres listen efter brugbare værdier, for at afgøre operationen.
    if "+" in indhold:
        indhold.remove("+")
        print(indhold[0], " ^ ", indhold[1], " = " ,float(indhold[0]) ** float(indhold[1]))
    if "-" in indhold:
        indhold.remove("-")
        print("kvadratroden af ", indhold[0], "er " , math.sqrt(float(indhold[0])))
    else:
        failsafe("Ugyldig operation, tjek valget af tegn")

    #Her genstartes programmet (uanset hvilken funktion er blevet kørt).
    time.sleep(1)
    print("")
    oprtn()


#Etablering af mulige operationer.
def oprtn():
    print("mulige operationer: 'basic math' (plus, minus, gange og division) & 'eksponentielt'")
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
        failsafe("Ugyldig/ukendt operationsnavn")

#Kør
oprtn()
