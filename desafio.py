
salario="7900"

nome= "theo souza"

porc="150"

if len(nome)>0:

    if len(nome.split(' '))>1:
        print('Nome Válido')
    
    else:
        raise Exception("Digite seu nome completo, não o inicial!")
    
        
else:
    raise Exception("Não deixe o seu nome zerado!!")
    #nome = input("Digite o seu nome completo: ")
    

try:
    #salario = float(input("Digite a sua remuneração: "))
    salario_ajustado = float(salario)
    if salario_ajustado>0:
        print("Salário maior que zero, não tão pobre assim...")
    else:
        raise Exception("Você inseriu um salário negativo ou zerado que isso kkk")
except:
    raise Exception("Você inseriu um valor não numérico no salário")

try:
    #salario = float(input("Digite a sua remuneração: "))
    porc_ajustado = float(porc)
    if porc_ajustado>0:
        print("Salário maior que zero, não tão pobre assim...")
    else:
        raise Exception("Você inseriu um salário negativo ou zerado que isso kkk")
except:
    raise Exception("Você inseriu um valor não numérico no salário")


def calcula_bonus(remun, porc_ajustado):
    bonus= 1000+(remun*porc_ajustado/100)
    
    return bonus

print("Saudações meu querido "+nome+ ", o seu bônus foi de "+str(calcula_bonus(salario_ajustado, porc_ajustado)))