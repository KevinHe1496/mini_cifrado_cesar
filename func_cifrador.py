alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

print(len(alphabet))

def crea_cifrador(d: int):
    def cifrar(mensaje: str):
        result = ''
        for letra in mensaje.upper():
            if letra in alphabet:
                index = alphabet.index(letra)
                new_index = (index + d) % 28
                result += alphabet[new_index]

        return result
    
    return cifrar




    
        