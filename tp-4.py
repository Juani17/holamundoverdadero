import random

random = random.randint(0, 100)
jump = random.randint(0, 10)

print(random, jump)

numbers_list = [i for i in range(0, random, jump)]
search_number = int(input("Ingrese numero a buscar: "))
val = False

for i in range(len(numbers_list)):
    if numbers_list[i] == search_number:
        val = True
        break

if val: print(f"Numero encontrado: {search_number}")
else: print(f"El numero a buscar no se encuentra")