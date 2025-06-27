from operacoesbd import *

def registrarProdutos(conexao):
    nome = input("Digite o nome do ingrediente: ")
    quantidadeProduto = float(input("Digite a quantidade desse produto: "))
    preco = float(input("Digite o valor do ingrediente: "))

    print(f"Ingrediente registrado, Nome: {nome}, Quantidade: {quantidadeProduto} e o preço é {preco:.2f}")

def listarProdutos(conexao):

    consulta = 'select * from manifesto'
    manifestos = listarBancoDados(conexao, consulta)

    if len(manifestos) == 0:
        print("Não existem Produtos registrados a serem exibidos")
    else:
        print("Lista de Manifestaçoes")
        for item  in manifestos:
            print('Codigo do manifesto: ',item[0], '\nManifesto:', item[2], '\nAutor:', item[1])

def calcularPrecoUsado(conexao):
    preco = float(input("Adicione o valor do produto: "))
    quantidadeTotal = float(input("Adicione qual a quantidade total do produto: "))
    quantidadeUsada = float(input("Adicione a quantidade usada: "))

    #  Preco / quantidadeTotal
    calculoUnidade = preco / quantidadeTotal
    #  custoPorUnidade * quantidadeUsada = custoUsado
    calcularPrecoUsado = calculoUnidade * quantidadeUsada

    print(f"O valor para da quantidade usada é: R${calcularPrecoUsado:.2f}")

