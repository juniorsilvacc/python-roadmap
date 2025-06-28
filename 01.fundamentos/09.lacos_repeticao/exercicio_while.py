usuario_correto = "admin"
senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("✅ Login bem-sucedido!")
        break
    else:
        print("❌ Usuário ou senha incorretos.")
        tentativas += 1 # soma 1 a cada erro (tentativas = 0 + 1 = 1, tentativas = 1 + 1 = 2...)
if tentativas == 3:
    print("🔒 Conta bloqueada após 3 tentativas.")