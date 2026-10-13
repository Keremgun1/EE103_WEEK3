num = int(input("Faktöriyelini bulmak istediğiniz sayı: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Sonuç:", fact)

num = int(input("Faktöriyelini bulmak istediğiniz sayı: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Sonuç:", fact)
