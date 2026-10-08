#Validador de dados em pyyhon
#O programa recebe qualquer tipo de dado e verificar o tipo dele e entrega para o úsuario

dado = input("Digite qualquer coisa para verificar o tipo de dado: ").strip()
if dado == "":
    print("Nenhum valor informado!")
elif dado == "True" or dado == "False":
        print("Seu tipo de dado é boleano!")
else:
    try: 
        dado = int(dado)
        print("Seu tipo de dado é um número inteiro!")
        
    except ValueError:
        try:
            dado = float(dado)
            print("Seu tipo de dado é um número decimal!")
            
        except ValueError:
                print("Seu tipo de dado é do tipo string!")
            
        
            
    
    






