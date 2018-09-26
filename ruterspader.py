run = 0
while run == 0:
    gissa = int(input("Gissa ett nummer mellan 1 - 4 "))
    import random
    a = random.randint(1,4)
    if gissa == a:
        print("rätt")
        run = 1
    else:
        print("fel")
else:
    print("Tack för spelet")