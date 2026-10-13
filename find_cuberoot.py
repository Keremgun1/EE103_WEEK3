given_number = int(input("Küp kökü bulunacak bir tam sayı girin: "))

# Sayının negatif olup olmadığını başta kaydedelim
is_negative = False
if given_number < 0:
    is_negative = True
    # İşlemleri kolaylaştırmak için sayıyı geçici olarak pozitife çevirelim
    working_number = -given_number
else:
    working_number = given_number

guess_number = 0

# Küpü, aradığımız sayıya ulaşana veya geçene kadar tahmin numarasını artır
while guess_number ** 3 < working_number:
    guess_number += 1

# Kontrol edelim
if guess_number ** 3 == working_number:
    # Eğer başta negatifse, sonucumuzu da eksi yapalım
    if is_negative:
        guess_number = -guess_number
    print(f"{given_number} sayısının küp kökü: {guess_number}")
else:
    print(f"{given_number} tam bir küp köke sahip değil!")