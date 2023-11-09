import hashlib
import sys

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

try:
    #Lendo a senha do arquivo txt fornececido pelo o usuário
    with open('senha_correta.txt', 'r') as arquivo:
        senha = arquivo.read().strip()
except FileNotFoundError:
    sys.exit()

try:
    #Lendo a senha criptografada do arquivo txt da hash
    with open('hash_senha.txt', 'r') as arquivo:
        senha_criptografada = arquivo.read().strip()
except FileNotFoundError:
    sys.exit()

#Verificando se asenha coincide com a senha criptografada
def test_answer():
    assert criptografar_senha(senha) == senha_criptografada