class ReglaCifradoTraslacion(ReglaCifrado):
    def mensaje_valido(self, mensaje):
        super().mensaje_valido(mensaje)
        if any(c.isnumeric() for c in mensaje):
            raise ErrorNumeros(posicion=mensaje.index(c), caracter=c)
        if any(c not in '@_#$%' and not c.isalpha() for c in mensaje):
            raise ErrorContenido(posicion=mensaje.index(c), caracter=c)

    def cifrar(self, mensaje):
        super().cifrar(mensaje)
        mensaje = mensaje.lower()
        cifrado = ""
        for char in mensaje:
            if char.isalpha():
                cifrado += chr((ord(char) - ord('a') + self.token) % 26 + ord('a'))
            else:
                cifrado += char
        return cifrado

    def descifrar(self, mensaje):
        super().descifrar(mensaje)
        mensaje = mensaje.lower()
        descifrado = ""
        for char in mensaje:
            if char.isalpha():
                descifrado += chr((ord(char) - ord('a') - self.token) % 26 + ord('a'))
            else:
                descifrado += char
        return descifrado


class ReglaCifradoNumerico(ReglaCifrado):
    def mensaje_valido(self, mensaje):
        super().mensaje_valido(mensaje)
        if any(c.isnumeric() for c in mensaje):
            raise ErrorNumeros(posicion=mensaje.index(c), caracter=c)
        if ' ' in mensaje[1:-1] or mensaje.startswith(' ') or mensaje.endswith(' '):
            raise ErrorEspacios()

    def cifrar(self, mensaje):
        super().cifrar(mensaje)
        mensaje = mensaje.lower()
        cifrado = ""
        for char in mensaje:
            if char.isalpha():
                cifrado += str(ord(char) * self.token) + ' '
            else:
                cifrado += char
        return cifrado.strip()

    def descifrar(self, mensaje):
        super().descifrar(mensaje)
        mensaje = mensaje.lower()
        descifrado = ""
        numeros = mensaje.split()
        for num in numeros:
            descifrado += chr(int(num) // self.token)
        return descifrado


class Cifrador:
    def __init__(self, agente):
        self.agente = agente

    def encriptar(self, mensaje):
        self.agente.mensaje_valido(mensaje)
        mensaje = mensaje.lower()
        return self.agente.cifrar(mensaje)

    def desencriptar(self, mensaje):
        self.agente.mensaje_valido(mensaje)
        mensaje = mensaje.lower()
        return self.agente.descifrar(mensaje)