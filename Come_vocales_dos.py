word_without_vowels=""

user_word=input("INGRESA LA PALABRA")
user_word=user_word.upper()
# Bucle for para recorrer cada letra en la palabra
for letra in user_word:
    # Usar la ejecución condicional para devorar las vocales
    if letra in "AEIOU":
        # Si es una vocal, omitir el resto del código en este bucle y continuar con la próxima iteración
        continue
    else:
        # Si no es una vocal, agregar la letra a la cadena de letras no consumidas
        word_without_vowels += letra

# Imprimir las letras no consumidas
print("Palabra sin vocales:",word_without_vowels)