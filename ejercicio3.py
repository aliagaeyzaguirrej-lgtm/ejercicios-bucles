#Contar cuántas letras 'a' tiene una frase
frase = input("ingrese una frase que le guste ").lower()
contador = 0
for i in frase:
    if i == "a":
        contador += 1
print("---CONTADOR DE A EN UNA FRASE---")
print(f"en la frase: {frase} hay {contador} de a")