boucle = "o"
while (boucle == "o"):
    eleve=input("Saisir le nom de l'éleve présent: ")
    boucle=input("Voulez vous continuer o/n : ")

continuer = True
while continuer:
    saisi=input("Saisir le nom de l'éleve présent ou taper q pour quitter ")
    if (saisi == "q"):
        break
essai=4
for (essai=essai-1):