# Sistema de Login
usuario_correto = "admin"
senha_correta = "1234"

# Contador de tentativas
tentativas = 0

print("=== Sistema de Login ===")

# Estrutura de repetição com limite de tentativas
while tentativas < 3:
    # Coleta de dados (funções built-in)
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    tentativas += 1

    # Estrutura condicional para verificar acesso
    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.\n")

# Verifica se falhou após 3 tentativas
if tentativas == 3:
    print("Número máximo de tentativas atingido. Acesso bloqueado.")
