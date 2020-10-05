tyden = ["v nedeli","v pondeli","v úterý","ve stredu","ve ctvrtek","v patek","v sobotu"]
for x in range(7):
    print(tyden[x]+"..."+str(x))
odjezd = int(input("Kdy odjiždíš?:"))
delka = int(input("Kolik nocí tam budeš?:"))
den = ((odjezd + delka)% 7)
zprava = tyden[den]
print("Vracíš se "+zprava)
