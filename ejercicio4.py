# Encontrar números primos en un rango

primo = []
for num in range(2, 31):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primo.append(num)
print(f"los numeros del 2 al 30 son primos: {primo}")

    