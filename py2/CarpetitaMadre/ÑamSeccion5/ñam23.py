# Crear una función llamada es_palindromo que reciba un texto como parámetro y retorne True si es un palíndromo (se lee igual al derecho y al revés) o False en caso contrario. La función debe ignorar espacios, mayúsculas/minúsculas y signos de puntuación.

def es_palindromo(texto):

    texto_limpio = ''.join(caracter for caracter in texto if caracter.isalnum()).lower()
    
    return texto_limpio == texto_limpio[::-1]

print(es_palindromo("Anita lava la tina")) 
print(es_palindromo("Hola mundo"))
