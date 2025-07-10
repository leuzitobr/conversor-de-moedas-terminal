import requests
import os
#Titulo do projeto
print("-------------------\nCONVERSOR DE MOEDAS!\n-------------------\n")

#Variavel para controlar o while
resp = int(1)
while resp == 1:
    #Abaixo o usuario irá informar a moeda na qual deseja receber a conversão 
    coinDestiny = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
    while coinDestiny < 1 or coinDestiny > 9:
        print("A opção selecionada não é valida!")
        coinDestiny = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
    #Estrutura de repetição para não haver resultados invalidaos no codigo 


    #Abaixo o usuario irá informar a moeda na qual deseja realizar a conversão
    coinOrigin = int(input("Digite qual será a moeda de origem utilizada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
    while coinOrigin < 1 or coinOrigin > 9:
        print("A opção selecionada não é valida!")
        coinOrigin = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
    #Estrutura de repetição para não haver resultados invalidaos no codigo 

    # Enquanto as moedas forem iguais o comando resetara do começo 
    while coinDestiny == coinOrigin:
        print("A moeda de conversão e a moeda de origem não podem ser iguais ")
        #Abaixo o usuario irá informar a moeda na qual deseja receber a conversão 
        coinDestiny = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
        while coinDestiny < 1 or coinDestiny > 9:
            print("A opção selecionada não é valida!")
            coinDestiny = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
        #Estrutura de repetição para não haver resultados invalidaos no codigo 

        #Abaixo o usuario irá informar a moeda na qual deseja realizar a conversão
        coinOrigin = int(input("Digite qual será a moeda de origem utilizada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
        while coinOrigin < 1 or coinOrigin > 9:
            print("A opção selecionada não é valida!")
            coinOrigin = int(input("Digite qual será a moeda destinada para conversão:\n1-USD\n2-EUR\n3-GBP\n4-JPY\n5-CNY\n6-ARS\n7-CHF\n8-CAD\n9-BRL\n"))
        #Estrutura de repetição para não haver resultados invalidaos no codigo 

    #Moeda de destino 
    destinyCoin = ""
    originCoin = ""
    #validando moeda de destino
    if coinDestiny == 1:
        coinDestiny = "USD"
        destinyCoin = "Dolares"
    elif coinDestiny == 2:
        coinDestiny = "EUR"
        destinyCoin = "Euros"
    elif coinDestiny == 3:
        coinDestiny = "GBP"
        destinyCoin = "Libras Esterlinas"
    elif coinDestiny == 4:
        coinDestiny = "JPY"
        destinyCoin = "ienes"
    elif coinDestiny == 5:
        coinDestiny = "CNY"
        destinyCoin = "Yuans"
    elif coinDestiny == 6:
        coinDestiny = "ARS"
        destinyCoin = "Pesos Argentinos"
    elif coinDestiny == 7:
        coinDestiny = "CHF"
        destinyCoin = "Francos Suiços"
    elif coinDestiny == 8:
        coinDestiny = "CAD"
        destinyCoin = "Dolares Canadenses"
    else:
        coinDestiny = "BRL"
        destinyCoin = "Reais"

    #validando moeda de origem
    if coinOrigin == 1:
        coinOrigin = "USD"
        originCoin = "Dolares"
    elif coinOrigin == 2:
        coinOrigin = "EUR"
        originCoin = "Euros"
    elif coinOrigin == 3:
        coinOrigin = "GBP"
        originCoin = "Libras Esterlinas"
    elif coinOrigin == 4:
        coinOrigin = "JPY"
        originCoin = "Ienes"
    elif coinOrigin == 5:
        coinOrigin = "CNY"
        originCoin = "Yans"
    elif coinOrigin == 6:
        coinOrigin = "ARS"
        originCoin = "Pesos Argentinos"
    elif coinOrigin == 7:
        coinOrigin = "CHF"
        originCoin = "Franco Suiços"
    elif coinOrigin == 8:
        coinOrigin = "CAD"
        originCoin = "Dolares Canandenses"
    else:
        coinOrigin = "BRL"
        originCoin = "Reais"

    # O usuario informa o valor que ele deseja converter, e só parara o lopping quando o valor for um valor numerico
    while True:
        try:
            value = float(input("Digite o valor que será realizado a conversão:"))
            break
        except ValueError:
            print("O valor de numero está inválido!")

    #Faz a requisição da API
    url = f"https://v6.exchangerate-api.com/v6/1aeb9073b4b9fc23b16c6b34/latest/{coinOrigin}"

    #Realizar as requisições
    requisition = requests.get(url)
    dados = requisition.json()

    #Caso a api falhar essa tela ira mostrar
    if requisition.status_code != 200:
        print('Erro ao consultar a API')

    # Pegar a taxa de conversão 
    taxa = dados['conversion_rates'][coinDestiny]

    #Realizar a conversão
    convertedValue = value * taxa


    #Print para saber se estar tudo bem
    print(f"Voce quer converter {value:.2f} {originCoin}({coinOrigin}) para {destinyCoin}({coinDestiny}) \n Cotação: 1 {originCoin}({coinOrigin}) = {taxa:.2f} {destinyCoin}({coinDestiny})\n Resultado {value:.2f} {originCoin}({coinOrigin}) = {convertedValue:.2f} {destinyCoin} ({coinDestiny})")

    #Print para mostrar os dados da contação    
    print(f"Data da ultima contaçaõ: {dados['time_last_update_utc']}")

    #Pergunta para continuar o looping 
    resp = int(input("\nDeseja continuar a utilizar o conversor?\n [1]- SIM \n [2]- NÃO\n"))
    if resp == 1:
        print("Resposta enviada...")
        os.system('cls') 

    elif resp == 2:
        print("Resposta enviada...")
        print("Programa encerrado!") 
    else:
        print("Resposta invalida!\nOpção inexistente!\nPrograma encerrando por segurança.")
    
