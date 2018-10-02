hand = []
print("Finns i sjön!")
fråga = 0
while fråga != 5:
    try:
        fråga = int(input("Vilket kort vill du fråga efter (1 -4) "))
    except:
        print("Skriv ett nummer, försök igen")
    import random
    aikort = random.randint(1,4)
    print(aikort)
    if fråga == aikort:   
        hand.append(aikort)
        print("i din hand har du", hand)
    else:
        print("finns i sjön")
else:
    print("Tack för spelet")