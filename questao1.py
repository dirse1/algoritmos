# Crie um algoritmo que simule o acesso de um usuário
# a uma área restrita. O programa deve pedir
# nome de usuario, senha, e se possui autorizacao especial

print('=== SISTEMA DE ACESSO ===')

tentativas = 0

for tentativas in range(1, 4):
    user = (input('Digite o seu usuário: '))
    senha = (input('Digite a sua senha: '))
    acesso = (input('Possui autorização especial?(S/N): '))
    if (user == 'admin' and senha == 'monster123' or acesso == 'S' or acesso == 's'):
        print('Acesso liberado')
        print('Bem-vindo ao sistema!')
        break
        
    else:
        print('Acesso negado')
