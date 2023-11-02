print('Digite 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir ')
escolha = 0 
while escolha not in (1,2,3,4):
    escolha = int(input("Digite o numero da operação que voçe quer:") )
    if escolha not in (1, 2, 3, 4):
        print("Escolha inválida. Tente novamente.")
    elif escolha == 1:
        a =int(input("Digite o 1 numero:"))
        b =int(input("Digite o 2 numero:"))
        print(a+b)
        
    elif escolha == 2 :
        a =int(input("Digite o 1 numero:"))
        b =int(input("Digite o 2 numero:"))
        print(a-b)
        
    elif escolha == 3 :
        a =int(input("Digite o 1 numero:"))
        b =int(input("Digite o 2 numero:"))
        print(a*b)
       
    elif escolha == 4 :
        a =int(input("Digite o 1 numero:"))
        b =int(input("Digite o 2 numero:"))
        print(a/b)
        
print("voçê escolheu a opção :",escolha)   