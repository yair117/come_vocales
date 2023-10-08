# Indicar al usuario que ingrese una pal
palabra=input("Ingresa una palabra\n")
# y asignarlo a la variable user_word.
palabra= user_word.upper()

Palabras_no_consumidas=""

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in "A, E, I, O, U":
        continue
    else:
        Palabras_no_consumidas += letter
    
for letra in Palabras_no_consumidas:
    print(letra)