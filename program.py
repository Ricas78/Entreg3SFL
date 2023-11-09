import hashlib
import sys

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha, senha_criptografada):
    return criptografar_senha(senha) == senha_criptografada

try:
    #Lendo a senha do arquivo txt fornececido pelo o usuário
    with open('senha_correta.txt', 'r') as arquivo:
        senha = arquivo.read().strip()
except FileNotFoundError:
    print('O arquivo da senha digitada não foi encontrado.')
    sys.exit()

#linhas de código utilizadas pr verificar a hash da senha correta e colar no arquivo txt da hash
#hash_senha = criptografar_senha(senha)
#print('hash = ', hash_senha)

try:
    #Lendo a senha criptografada do arquivo txt da hash
    with open('hash_senha.txt', 'r') as arquivo:
        senha_criptografada = arquivo.read().strip()
except FileNotFoundError:
    print('O arquivo com a hash da senha correta não foi encontrado.')
    sys.exit()

#Verificando se asenha coincide com a senha criptografada
if verificar_senha(senha,senha_criptografada):
    print('A senha é correta.')
else:
    print('A senha é incorreta.')