import random
import string

diccio = {}

def gerar_valor_aleatorio(tamanho):
    caracteres = string.ascii_letters + string.digits  # letras (maiúsculas e minúsculas) + dígitos
    valor_aleatorio = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return valor_aleatorio

def CP():
    # Exemplo de uso para gerar um valor aleatório com 8 caracteres
    ponto = gerar_valor_aleatorio(8)
    print(f"Ponto {ponto} criado")
    file = open(ponto, "a")
    file.write("0x000")
    file.close()
    diccio[ponto] = []
    diccio[ponto].append("0x001")
    diccio[ponto].append("0x002")
    diccio[ponto].append("0x003")

def LPs():
    for ponto, value in diccio.items():
        print(f"{ponto} : {value}")

def LP():
    ponto = str(input("Digite o nome do ponto: "))
    with open(ponto, 'r') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)

    print(diccio[ponto])

def menu():
    print("1 - Criar um ponto.")
    print("2 - Listar pontos.")
    print("3 - Ler um ponto.")
    opcao = int(input("Opcao: "))

    if opcao == 1:
        CP()
        menu()
    if opcao == 2:
        LPs()
        menu()
    else:
        LP()
        menu()
    
menu()
