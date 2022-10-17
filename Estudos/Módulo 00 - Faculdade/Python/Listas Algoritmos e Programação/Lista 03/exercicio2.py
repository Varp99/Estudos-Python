# Faça um programa que leia um código(número) de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

codigo = int(input("Digite um código: "))
senha = int(input("Digite uma senha: "))

while codigo == senha:
    print("Erro, o código está igual a senha")
    codigo = int(input("Digite um código: "))
    senha = int(input("Digite uma senha: "))

print("Código e Senha diferentes, portanto, válido")
print("Código: ", codigo)
print("Senha: ", senha)