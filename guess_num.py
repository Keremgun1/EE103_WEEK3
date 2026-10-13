from secret_number import secretNum

deneme = 0
while True:
    if deneme >= 5:
        while True:
            print("Oh! Noooooo...")

    guess = int(input("Bir sayı tahmin edin (5 hakkın var): "))
    deneme += 1

    if guess < secretNum:
        print("too low")
    elif guess > secretNum:
        print("too high")
    else:
        print("Tebrikler, doğru!")
        break