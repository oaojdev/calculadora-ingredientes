from metodos import * 

opcao = 1

while opcao != 5:
    print("\n---------- MENU DE OPÇÕES ----------\n"
          "1) Registrar ingredientes\n"
          "2) Listar ingredientes\n"
          "3) Buscar ingrediente por codigo\n"
          "4) calcular valor de venda\n"
          "5) Sair do Sistema\n"
          "------------------------------------")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        calcularPrecoUsado()
    elif opcao == 2:
        print("teste")
    elif opcao == 3:
        print("teste")
    elif opcao == 4:
        print("teste")
    elif opcao == 5:
        print("Atendimento encerrado")

print("\nObrigada por usar o sistema!")
