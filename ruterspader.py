run = 0
gissningar = 0
while run == 0:
    try: 
        gissa = int(input("Gissa ett nummer mellan 1 - 4 "))
    except:
        print("Du måste välja en siffra")
    import random
    a = random.randint(1,4)
    if gissa == a:
        gissningar = gissningar + 1
        print("rätt")
        run = 1
        print("antal gissningar", gissningar)
    else:
        print(a)
        print("fel")
        gissningar = gissningar + 1
        print ("antal gissningar", gissningar)
else:
    print("Tack för spelet")