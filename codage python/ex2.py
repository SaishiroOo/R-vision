date=input("Saisir une date sous le format JJ/MM/AAAA : ")
for i in range (len(date)):
    print(date[i],end=" ")
    if (date[i] =="/"):
        date = " "