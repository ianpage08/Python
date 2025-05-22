# Credenciais pré-definidas (em um cenário real, estas viriam de um banco de dados)
email = 'ianpage27@gmail.com'
senha = '123456789'

# Solicita ao utilizador que digite o e-mail e a senha
usuario = input('Digite seu Email: ')
senha_usuario = input('Digite sua Senha: ')

# Bloco de condições para verificar as credenciais
if (email == usuario and senha_usuario == senha):
    # Se e-mail e senha estiverem corretos
    print('Usuario logado com sucesso')
elif (email != usuario and senha_usuario != senha):
    # Se tanto o e-mail quanto a senha estiverem incorretos
    print('Usuario e senha incorretos')
elif (email != usuario and senha_usuario == senha):
    # Se o e-mail estiver incorreto, mas a senha estiver correta (improvável em um cenário real)
    print('Usuario incorreto')
elif (senha_usuario != senha and email == usuario):
    # Se a senha estiver incorreta, mas o e-mail estiver correto
    print('Senha incorreta')
else:
    # Caso alguma condição inesperada ocorra (geralmente não será atingido com estas condições)
    print('Erro inesperado. Tente novamente')