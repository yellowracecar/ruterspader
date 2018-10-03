hand = [1]
print("Finns i sjön!")
fråga = 0
aifråga = 0
while fråga != 5:
    try:
        fråga = int(input("Vilket kort vill du fråga efter (1-4)? "))
    except:
        print("Skriv ett nummer, försök igen")
    import random
    aikort = random.randint(1,4)
    print("rätt kort var ", aikort)
    if fråga == aikort:   
        hand.append(aikort)
        print("kort i din hand =", hand.count(1))
    elif fråga != aikort:
        print("finns i sjön!")
        input("tryck enter för att forstätta")
        hand.append(1)
        import random
        aifråga = random.randint(1,4)
        print("Ge mig dina", aifråga)
        if aifråga == hand:
            hand.remove(1)
            print("kort i din hand", hand)
        else:
            print("finns i sjön")
            print("Din tur vvv")
else:
    print("Tack för spelet")