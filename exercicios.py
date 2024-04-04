# 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# first_number = int(input("insira seu primeiro número :"))

# second_number = int(input("insira seu segundo número :"))

# total = first_number + second_number

# print("O total é "+ str(total))

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# first_number = int(input("insira seu primeiro número :"))

# resto= first_number%5

# print(resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# first_number = int(input("insira seu primeiro número :"))

# second_number = int(input("insira seu segundo número :"))

# total = first_number * second_number

# print("O total é "+ str(total))

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.



# second_number = int(input("insira seu segundo número :"))

# first_number = int(input("insira seu primeiro número :"))

# second_number = int(input("insira seu segundo número :"))

# total = first_number // second_number

# print("O total é "+ str(total))

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# first_number = int(input("insira seu primeiro número :"))

# total = first_number**2

# print("O total é "+ str(total))

#6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# first_number = float(input("insira o primeiro número: "))

# second_number = float(input("insira o srgundo número: "))

# total = first_number+second_number

# total_str = str(total)

# print("O total é "+total_str)


#7. 

# first_number = float(input("Insira seu primeiro número: "))

# second_number = float(input("Insira seu segundo número: "))

# media = str((first_number+second_number)/2)

# print("A sua média é: " + media)

#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = float(input('insira o seu número base: '))

# expoente= float(input("insira o seu expoente: "))

# potencia = base**expoente

# potencia = str(potencia)

# print("A potência é :" + potencia)

#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#(0 °C × 9/5) + 32 = 32 °F

# temperatura_celsius = float(input("Insira sua temperatura em celsius: "))

# def conversor(temp):
#     farenheit = (temp * 9/5) + 32

#     return farenheit


# print("A sua temperatura em farenheit será de " + str(conversor(temperatura_celsius)))

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Insira o raio do seu círculo: "))

# def calcula_area(r):
#     pi = 3.14
#     area= pi*(r**2)
#     area_formatada = "{0:.2f}".format(area)
#     return area_formatada


# area_txt = str(calcula_area(raio))
# texto = "A área do seu círculo é de " + area_txt + "m²"

# print(texto)

#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# input_txt = input("Digite seu nome que nós transofrmaremos em maiúscula: ")

# maiscl = input_txt.upper()

# print(maiscl)

#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# input_txt =  input("Digite seu nome completo men:")

# minsculo= input_txt.lower()

# print(minsculo)

#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# input_phrase = input("Insira uma frase com espaços em branco: ")

# stripping = input_phrase.strip()

# print(stripping)

#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# itens = input("insira sua data por favor em formato dd/mm/aaaa: ").split("/")

# print("Esse é o seu dia: "+itens[0])
# print("Esse é o seu mês: "+itens[1])
# print("Esse é o seu ano: "+ itens[2])


#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# primeira_string = input("insira sua primeira string: ")
# segunda_string = input("insira sua segunda string: ")

# concatenation= primeira_string+segunda_string

# print(concatenation)

#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# var_1 = False
# var_2 = False

# var_consolidada = var_1 and var_2

# print(var_consolidada)

#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# var_1 = True
# var_2 = False

# resultado = var_1 or var_2
# print("o resultado da sua variável é: "+str(resultado))

#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# var = False

# inverted = not var

# print("Sua variável invertida é: " + str(inverted))

#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# n_1 = input("Insira seu primeiro número: ")
# n_2 = input("Insira seu segundo número: ")

# if n_1==n_2:
#     print("Parabéns você colocou dois números enguais")
# else:
#     print("Os números estão diferentes :(")

#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# n_1= input("Insira um número pls: ")
# n_2= input("Insira seu segundo número pleaserrrr: ")

# if n_1==n_2:
#     print("seus números estão enguais :(")
# else:
#     print("seus números estão deferentcheeee :)")

#Exercício 21: Conversor de Temperatura

# try:
#     temp_cels = float(input("Insira a temperatura: "))
#     print("Boa, você inseriu no formato correto!")
#     def conversor(temp):
#         farenheit = (temp * 9/5) + 32

#         return farenheit


#     print("Legal, sua temperatura em farenheit é: "+ str(conversor(temp_cels)))
# except:
#     print("Você inseriu os números errados.")

# Exercício 22: Verificador de Palíndromo


# def verifica_inversao(txt, inv_txt):
#     if txt==inv_txt:
#         print("Parabéns você colocou os textos iguais.")
#     else:
#         print("Textos diferentes")


# try:
#     texto= input("Insira seu texto: ")
#     var = isinstance(texto, str)
#     invertido = texto[::-1]
#     print(var)
#     print(invertido)

#     verifica_inversao(texto,invertido )


# except:
#     print("você não inseriu textos no formato correto")

#Exercício 23: Calculadora Simples



#definindo variáveis para o programa

# lst=['*','+','/',"-"]


# #teste de primeiro número
# #teste de operador
# #teste de segundo número

# #teste de operador

# print("Bem vindo a calculadora básica :)")

# #testando primeiro número
# try:
#     num_1=float(input("Insira seu primeiro número: "))
# except:
#     print("Xi, deu erro nno segundo número")


# operador = input("Insira seu operador '*','+','/','-': ")

# #testando operador
# def stringInList(operador, lst):
#     for i in lst:
#         if operador in i:
            
#             return print("Você Inseriu um operador válido")

            
#     return Exception("Você inseriu o operador incorreto")

# stringInList(operador,lst)

# #testando segundo número
# try:
#     num_2=float(input("Insira seu segundo número: "))
# except:
#     print("Xi, deu erro nno segundo número")


# #calculando
# def calculadora(operador,num_1,num_2):
#     if operador == "*":
#         resultado=num_1*num_2
#     elif operador == "+":
#         resultado=num_1+num_2
#     elif operador == "-":
#         resultado=num_1-num_2
#     elif operador == "/":
#         resultado=num_1/num_2
#     return resultado


# #chamando função
# print("Seu resultado é "+str(calculadora(operador,num_1,num_2)))



#Exercício 24: Classificador de Números


#Função para saber sinal do número
# def n_cond(number):
#     if number==0:
#         clas="zero"
#     elif number>0:
#         clas="positivo"
#     else:
#         clas="negativo"

#     return clas

# #Função para saber se o número é par ou impar
# def is_even(number):
#     if number%2==0:
#         result="par"
#     else:
#         result="impar"
#     return result

# n=-12

# try:
#     n= int(input("Insira seu número: "))
#     clas=n_cond(n)
#     result=is_even(n)
#     print(f"O número {str(n)} é {clas} e {result}!")


# except ValueError:
#     print("Erro! Digite um valor válido do número")


#Exercício 25: Conversão de Tipo com Validação



# """
# 1 - insere a lista
# o certo seria, 
# se contiver qualquer caractére diferente de vírgula ou número dá erro

# primeiro eu vou separar os caractéres com split
# depois eu vou fazer um for que para cada item da lista ele converte
# no entanto esse for precisára ter try except
# """

# lista_string= "1,2,3,4,5,6"

# lista_ls = lista_string.split(",")
# lista_numerica=[]

# try:
#     for n in lista_ls:
#         n_conv=int(n)
#         lista_numerica.append(n_conv)
#     print(lista_numerica)
# except:
#     print("Deu erro em algum número inserido")