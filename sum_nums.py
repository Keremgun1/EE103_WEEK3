n = int(input("Bir sayı girin: "))

# Döngü ile toplam
toplam = 0
for i in range(1, n + 1):
    toplam += i

# Gauss formülü ile toplam
sum_gauss = n * (n + 1) / 2

# Karşılaştırma
if toplam == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")