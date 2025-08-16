import secrets
import string


class GerarChave():
    """Gerador de chaves aleatória"""
    
    def __init__(self):
        self.gerar_chave()

    def gerar_chave(self):
        self.letras = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(4))
        self.numeros = ''.join(secrets.choice(string.digits) for _ in range(3))
        
        return self.letras + self.numeros


print(GerarChave().gerar_chave())