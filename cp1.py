5#Augusto Fisco Milreu RMº98245
import time

print("Bem-vindo a Vinheria Agnello, para iniciarmos o processo de compra preencha as seguintes informações: ")
time.sleep(3)
nome = str(input("Digite seu nome completo: "))
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("A Vinheria Agnello não tolera a venda de bebidas alcoólicas para menores de 18 anos, sua compra será finalizada!")
    time.sleep(1.5)
    print("Finalizando compra.")
else:
    enderecoC = input("Digite o endereço de cobrança: ")
    enderecoE = input("Digite o endereço de entrega: ")
    valor = 0
    q = 0

    print("Suas informações foram analisadas e aprovadas")
    print("Nosso catálogo será apresentado!")
    time.sleep(1.7)

    while True:

                print("Catálogo Vinheria Agnello:\n"
                "OBS: Preço mínimo de compra (R$ 100,00)\n"
                "Para compras com valor ACIMA de R$ 200,00 terão frete GRATUITO!\n"
                "Digite o número de antes do nome do vinho para seleciona-ló:\n"
                  "(0) Vinho Tinto - Porto Pierro R$69,90\n"
                  "(1) Vinho Branco - De Martino R$70,90\n"
                  "(2) Vinho Rosé - Chileno R$50,99\n"
                  "(3) Espumante - Chandon R$83,90\n"
                  "(4) Vinho Licoroso - Sauvignon R$69,99\n"
                  "(5) Finalizar Compra\n")
                print("O valor do seu carrinho de compras está atualmente em R$%.2f" % valor)
                e = int(input("Sua escolha.: "))

                if e == 0:
                    q += 1
                    valor += 69.90
                elif e == 1:
                    q += 1
                    valor += 70.90
                elif e == 2:
                    q += 1
                    valor += 50.99
                elif e == 3:
                    q += 1
                    valor += 83.90
                elif e == 4:
                    q += 1
                    valor += 69.99
                elif e == 5:
                    break
                else:
                    print("Digite o número correto!")
                    break
    if valor < 100:
        print("O valor da compra deve ser superior a R$100,00")
        print("O valor do seu carrinho de compras deu um total de R$%.2f" % valor)
    elif valor <= 200:
        print("Muito obrigado pela preferência ao escolher seus vinhos em sua Vinheria Agnello!")
        time.sleep(0.7)
        frete = 30
        valor3 = valor + frete
        print("Seu carrinho ficou no total de R$%.2f. Com nossa entrega, seu vinho será devidamente cuidado e entregue no seu lar em poucos dias, totalizando em um valor de R$%.2f" % (valor, valor3))
        print("A quantidade de vinhos escolhidos adicionados no seu carrinho, tem um total de %d item(s)" % q)
        print("A sua entrega será enviada para esse endereço: %s" % enderecoE)
        resp = input("Deseja continuar?\n"
                     "(S para SIM)\n"
                     "(N para NÃO): ")
        if resp == "S":
            print("Muito obrigado pela compra, a Vinheria Agnello agradece e estará sempre a disposição! A entrega será feita em %s" % enderecoE)
        elif resp == "N":
            enderecCORRETO = input("Digite o novo endereço de entrega: ")
            time.sleep(0.5)
            print("Muito obrigado pela compra, a Vinheria Agnello agradece e estará sempre a disposição! A entrega será feita em %s" % enderecCORRETO)
        else:
            print("Digite uma opção válida!")
    elif valor > 200:
        print("Muito obrigado pela preferência ao escolher seus vinhos em sua Vinheria Agnello!")
        time.sleep(0.7)
        print("Seu carrinho ficou com um total de R$%.2f. Como sua compra foi acima de R$200,00 terá o frete gratuito, com a garantia do cuidado e o lazer de receber seu vinho em seu lar em poucos dias." % valor)
        print("A quantidade de vinhos escolhidos adicionados no seu carrinho, tem um total de %d item(s)" % q)
        print("A sua entrega será enviada para esse endereço: %s" % enderecoE)
        resp = input("Deseja alterar o destino ou continuar?\n"
                     "(S para SIM)\n"
                     "(N para NÃO): ")
        if resp == "S":
            print("Muito obrigado pela compra, a Vinheria Agnello agradece e estará sempre a disposição! A entrega será feita em %s" % enderecoE)
        elif resp == "N":
            enderecCORRETO = input("Digite o novo endereço de entrega: ")
            time.sleep(0.5)
            print("Muito obrigado pela compra, a Vinheria Agnello agradece e estará sempre a disposição! A entrega será feita em %s" % enderecCORRETO)
        else:
            print("Digite uma opção válida!")

