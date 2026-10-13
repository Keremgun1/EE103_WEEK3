given_number = int(input("Karekökü bulunacak tam kare bir sayı girin: "))

guess_number = 1

# Tahminin karesi verilen sayıdan küçük olduğu sürece tahmini 1 artır
while guess_number * guess_number < given_number:
    guess_number += 1

# Döngü bittiğinde kontrol edelim
if guess_number * guess_number == given_number:
    print(f"{given_number} sayısının karekökü: {guess_number}")
else:
    print("Tam kare değil!")