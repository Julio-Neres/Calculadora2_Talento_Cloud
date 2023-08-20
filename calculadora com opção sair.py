def calculadora():
    while True: 
        print("1:soma")
        print("2:subtração")
        print("3:multiplicação")
        print("4:divisao")
        print("0: Sair")
       
        escolha =int(input("Escolha uma operação:"))
        if escolha ==0:
            print("Saindo da calculadora")
            break
        elif escolha ==1:
            num1= float(input("Insira o primeiro número:"))
            num2=float(input("Insira o segundo número:"))
            resultado = num1+num2
            Print("Resultado da soma é:",resultado)
        elif escolha == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print("Resultado da subtração é: ", resultado)
        elif escolha == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print("Resultado da multiplicação é: ", resultado)
        elif escolha == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 == 0:
                print("Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                print("Resultado da divisão é: ", resultado)
        else:
            print("Opção inválida. Por favor escolha uma das opções entre 0 e 4")

calculadora()



        