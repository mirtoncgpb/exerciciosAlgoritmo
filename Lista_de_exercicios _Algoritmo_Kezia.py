#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ListExerc01
num = int (input("Informe um número interio: "))
print ("O número informado foi:",num)


# In[14]:


#ListExerc02
print ("Informe dois números inteiros.")
print("--------------------------------")
num1 = int (input("Número 1: "))
num2 = int (input("Número 2: "))
soma = num1+num2
print ("Soma dos números:",(soma))


# In[ ]:


#ListExerc03
print ("Informe as notas quatro bimestrais:")
print("-------------------------------------")
nota1 = float (input("Informe a 1º nota: "))
nota2 = float (input("Informe a 2º nota: "))
nota3 = float (input("Informe a 3º nota: "))
nota4 = float (input("Informe a 4º nota: "))
media = ((nota1+nota2+nota3+nota4)/4)
print ("A média da notas =", media)


# In[23]:


#ListExerc04
print ("Conversão de M para cm")
print("------------------------")
valorMetro = float (input("Informe o valor em metros: "))
valorCentimetro = valorMetro*100
print("O medida de {:.2f} m é equivalentea {:.0f} cm.".format(valorMetro,valorCentimetro))


# In[26]:


#ListExerc05
import math
print ("Calcular o área de um circulo")
print ("-----------------------------")
raioCirculo = float (input("Informe raio de um círculo: "))
areaCirculo = float (math.pi * (raioCirculo**2)) #math.pow(raioCirculo,2)
print ("Área do circulo {:.3f}:".format(areaCirculo))


# In[29]:


#ListExerc06
print ("Calcular o área de um quadrado")
print ("-----------------------------")
medidaLado = float (input("Informe a medida de um dos lados do quadrado: "))
areaQuadrado = float (medidaLado**2)
print ("\nÁrea do quadrado é {:.2f}cm.\nO dobro da área do quadrado é {:.2f}cm.".format(areaQuadrado,(areaQuadrado*2)))


# In[ ]:


#ListExerc07
print ("Calcular total de salário/mês")
print ("-----------------------------")
valorHora = float (input ("Informe o valor da sua hora trabalhada: "))
print ("Informe a quantidade de horas/minutos trabalhadas no mês:")
quant_horas = int (input ("Informe a quantidade de horas:"))
quant_minutos = int (input ("Informe a quantidade de minutos:"))
total_horas_trabalhadas = float ((((quant_horas*60)+ quant_minutos)/60))
valor_salario = float (valorHora*total_horas_trabalhadas)
print ("Total a ser pago referente ao mês com",quant_horas,"horas:",quant_minutos,"R$",valor_salario)


# In[10]:


#ListExerc08
print ("Transformar Farenheit em Celsius")
print ("--------------------------------")
temp_Farenheit = float (input ("Informe a temperatura em Farenheit: "))
temp_Celsius = float (5*(temp_Farenheit-32)/9)
print ("A temperatura de {:.1f}°F corresponde a {:.1f}°C.".format(temp_Farenheit,temp_Celsius))


# In[9]:


#ListExerc09
print ("Transformar Celsius em Farenheit")
print ("--------------------------------")
temp_Celsius = float (input ("Informe a temperatura em Celsius: "))
temp_Farenheit = float ((temp_Celsius*1.8)+32)
print("A temperatura de {:.1f}°C corresponde a {:.1f}°F.".format(temp_Celsius,temp_Farenheit))


# In[ ]:


#ListExerc10
print ("Conversão de Dólar para Real")
print ("--------------------------------")
valor_Dolar = float (input("Informe o valor em dólar: "))
cotacao_Dolar = float (input("Informe a cotação do dólar: "))
valor_Real = float (valor_Dolar*cotacao_Dolar)
print("Valor em Dólar:",valor_Dolar,"-->","Valor em Real: R$",valor_Real)


# In[8]:


#ListExerc11
import math 

print ("Calculo de rendimento 0,70% a. m")
print ("--------------------------------")
deposito = float (input("Por favor informe o valor a ser depositado: "))
rendimento = float (deposito * 0.007)
print("Valor depositado:",deposito,"Redimento a.m.:",'{:.2f}'.format(rendimento),"Total na conta:",'{:.2f}'.format(deposito + rendimento))


# In[13]:


#ListExerc12
import math 

print ("Venda em 5 prestações sem juros")
print ("-------------------------------")
valor_compra = float (input("Informe o valor total das compras: "))
parcela = float (valor_compra / 5)
print ("O valor total:",'{:.2f}'.format(valor_compra),"<==> Valor das prestações em 5x:",'{:.2f}'.format(parcela))


# In[17]:


#ListExerc13
import math 

print ("Venda em 5 prestações sem juros")
print ("-------------------------------")
valor = float (input("Informe o valor inicial do produto: "))
perc_acrescimento = float (input("Informe o valor de acrescimo: "))
valor_de_venda = (valor+ (valor * (perc_acrescimento/100)))
print ("Preço de venda:",'{:.2f}'.format(valor_de_venda))


# In[19]:


#ListExerc14
import math 

print ("Consumo médio de combustível")
print ("-------------------------------")
distancia_pecorrida = float (input("Informe a distancia pecorrida no trajeto em Km: "))
consumo_combustivel = float (input("Informe a quantidade a combustível consumido L: "))
consumo_medio = distancia_pecorrida / consumo_combustivel
print ("Consumo médio de combustível Km/l:",'{:.2f}'.format(consumo_medio))


# In[24]:


#ListExerc15
import math 

print ("Calculo da expressão D=(R+S)/2 ")
print ("-------------------------------")
print ("informe as os valores para A, B e C:")
a = float (input("A: "))
b = float (input("B: "))
c = float (input("C: "))
r = (a+b)**2
s = (b+c)**2
d = (r+s)/2
print ("A solução da da expressão D=(R+S)/2:",'{:.2f}'.format(d))


# In[27]:


#ListExerc16
import math 

print ("Calculo do salário + comissão")
print ("------------------------------")
nome_vendedor = input("Informe o nome do vendedor: ")
salario_fixo = float (input("Informe o salário fixo, R$: "))
total_vendas = float (input("Informe o total de vendas, R$: "))
perc_comissao = total_vendas * 0.15
salario_final = salario_fixo + perc_comissao
print ("Nome do vendedor",nome_vendedor)
print ("Salário fixo:",'{:.2f}'.format(salario_fixo))
print ("Sálario com comissão:",'{:.2f}'.format(salario_final))


# In[14]:


#ListExerc17
import math 

print ("Calculos com dois números Inteiros")
print ("------------------------------")

print("Por favor informe dois números inteirose um Real:")
numInteiro1 = int (input("Número Inteiro-1: "))
numInteiro2 = int (input("Número Inteiro-2: "))
numReal = float (input("Número Real: "))

# produto do dobro do primeiro com metade do segundo.
calculo_do_dobro = float ((2 * numInteiro1) * (numInteiro2 / 2))
# soma do triplo do primeiro com o terceiro.
soma = float ((numInteiro1*3) + numReal)
# terceiro elevado ao cubo
cubo_Numero = float (numReal**3)

print("Produto do dobro do 1º Número com metade do 2º Número:",'{:.2f}'.format(calculo_do_dobro))
print ("-------------------------------------------------------------------------")
print("Soma do triplo do 1º Número com o Número Real:",'{:.2f}'.format(soma))
print ("-------------------------------------------------------------------------")
print("Número Real elevado ao cubo:",'{:.2f}'.format(cubo_Numero))


# In[13]:


#ListExerc18
import math 

print ("Calculo do peso ideal")#lembrando que o valor de peso do individuo já está informado na questão.
print ("------------------------------")

altura = float(input("Informe a altura em metros:"))
#equação informada na questão: (72.7*altura) – 58
calculoPesoIdeal = float (72.7 * altura)-58
print ("Seu peso ideal seria: {:.2f}Kg".format(calculoPesoIdeal))


# In[67]:


#ListExerc19
#import math 

print ("Calculo de vecolidade de Download")#Informar o tempo aproximado de um download em minutos. 
print ("------------------------------")

tamanhoArquivoDownload_MB = float (input("Informe o tamanho do arquivo para download em MB: "))
velocidadeInternet = float (input("Informe a velocidade do link da internet em MBps: "))
calculo_MBps_para_MB = float (velocidadeInternet/8) #para achar o valor em MB por segundo
calculo_Tempo_Down = float (tamanhoArquivoDownload_MB/calculo_MBps_para_MB)/60 # para achar o tempo aproximado em minutos
print ("Tempo aproximado de download do arquivo:",'{:.1f}'.format(calculo_Tempo_Down),"min.")


# In[71]:


#ListExerc20
#import math 

print ("Troca de valores nas variaveis")
print ("------------------------------")

a = int (input("Informe uma valor inteiro para A: "))
b = int (input("Informe uma valor inteiro para B: "))

aux = a
a = b
b = aux
print ("A:",a,"-","B:",b)


# In[78]:


#ListExerc21
#import math 

print ("Calcular Salário liquido e descontos")
print ("------------------------------")

#calculo salario bruto:
valorHora = float (input ("Informe o valor da sua hora trabalhada: "))
print ("Informe a quantidade de horas/minutos trabalhadas no mês.")
quant_horas = int (input ("Informe a quantidade de horas:"))
quant_minutos = int (input ("Informe a quantidade de minutos:"))
total_horas_trabalhadas = float ((((quant_horas*60)+ quant_minutos)/60))

salarioBruto = float (valorHora*total_horas_trabalhadas)

#Descontos:
desconto_IR = salarioBruto * 0.11
desconto_INSS = salarioBruto * 0.08
desconto_Sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto-(desconto_IR+desconto_INSS+desconto_Sindicato)

#saídas
print("\n  Salário Bruto:","R$",'{:.2f}'.format(salarioBruto))
print("       IR (11%):","R$",'{:.2f}'.format(desconto_IR))
print("      INSS (8%):","R$",'{:.2f}'.format(desconto_INSS))
print("  Sindicato(5%):","R$",'{:.2f}'.format(desconto_Sindicato))
print("Salário Liquido:","R$",'{:.2f}'.format(salarioLiquido))


# In[101]:


#ListExerc22

print ("Verificar maior número") 
print ("------------------------------")

print ("Informe dois números:")
num1 = float(input("1º Número: "))
num2 = float(input("2º Número: "))

if num1 > num2:
    print("\nO primeiro número é maior que o segundo:",num1)
else:
    print("\nO segundo número é maior que o primeiro:",num2)


# In[103]:


#ListExerc23

print ("Verificar se o número é positivo ou negativo.")
print ("------------------------------")
valor = float(input("Informe um número: "))

if valor > 0:
    print("\nPositivo")
else:
    print("\nNegativo")


# In[166]:


#ListExerc24

print ("Validação F ou M.")
print ("------------------------------")

sexo = input("Informe seu sexo, F ou M: ")
  
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo  == "M" or sexo == "m":
    print ("Masculino")
    
else:
    print("Sexo Inválido!")


# In[18]:


#ListExerc25

print ("Calcular a média do aluno e informar situação.")
print ("------------------------------")

print("Informe notas do Aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1+nota2)/2

if media < 7:
    print("Aluno Reprovado!","\nMédia:",'{:.1f}'.format(media))
elif media >= 7 and media <= 9.99:
    print("Aluno Aprovado!","\nMédia:",'{:.1f}'.format(media))
elif media == 10:
    print("Aprovado com Distinção!","\nMédia:",'{:.1f}'.format(media))


# In[141]:


#ListExerc26
print ("Ler 3 números e verificar qual o maior.")
print ("------------------------------")

print ("Informe três números:")
num1 = float(input("1º Número: "))
num2 = float(input("2º Número: "))
num3 = float(input("3º Número: "))

soma = num1+num2
soma2 = num1+num3

if soma < num3:
    print("O 3º número é o maior:",num3)
elif soma2 < num2:
    print("O 2º número é o maior:",num2)
else: 
    print("O 1º número é o maior:",num1)


# In[149]:


#ListExerc27
print ("Perguntar tres valores e comprar o mais barato.")
print ("------------------------------")

print ("Informe os preços do três produtos:")
produto1 = float(input("Produto 1: "))
produto2 = float(input("Produto 2: "))
produto3 = float(input("Produto 3: "))

#calculo1 = produto2-produto1
#calculo2 = produto3-produto1

if produto3 < produto1 and produto3 < produto2:
    print("O produto 3 é o mais barato:",produto3)
elif produto2 < produto1 and produto2 < produto1:
    print("O produto 2 é o mais barato:",produto2)
else: 
    print("O produto 1 é o mais barato:",produto1)


# In[173]:


#ListExerc28
print ("Verificar turno que estuda.")
print ("------------------------------")

turno = input("Informe seu turno, M-matutino ou V-Vespertino ou N- Noturno: ")

if turno == "M" or turno == "m":
        print("Bom dia!")
elif turno  == "V" or turno == "v":
        print ("Boa tarde!")
elif  turno  == "N" or turno == "n":
        print("Boa noite!")
else:
    print("Valor Inválido!")


# In[17]:


#ListExerc29
print ("Calcular Ajuste salarial.")
print ("------------------------------")

salarioAtual = float(input("Informe o salário atual: "))

#% de Ajustes
ajuste01 = 1.2
ajuste02 = 1.15
ajuste03 = 1.1
ajuste04 = 1.05

"""critérios de ajustes.
salários até R$ 280,00 (incluindo): aumento de 20%
salários entre R$ 280,00 e R$ 700,00: aumento de 15%
salários entre R$ 700,00 e R$ 1500,00: aumento de 10% 
salários de R$ 1500,00 em diante: aumento de 5%"""

if salarioAtual <= 280:
    salarioNovo = float (salarioAtual*ajuste01)
    print("\n----------------------------------------------")
    print("                 Salário atual:","R$",'{:.2f}'.format(salarioAtual))
    print("Percentual de aumento aplicado:",'{:.2f}'.format((ajuste01-1)*100),"%")
    print("              Valor do aumento:","R$",'{:.2f}'.format(salarioNovo-salarioAtual))
    print("                  Novo salário:","R$",'{:.2f}'.format(salarioNovo))
    
elif salarioAtual >= 280.01 and salarioAtual < 700:
    salarioNovo = float (salarioAtual*ajuste02)
    print("\n----------------------------------------------")
    print("                 Salário atual:","R$",'{:.2f}'.format(salarioAtual))
    print("Percentual de aumento aplicado:",'{:.2f}'.format((ajuste02-1)*100),"%")
    print("              Valor do aumento:","R$",'{:.2f}'.format(salarioNovo-salarioAtual))
    print("                  Novo salário:","R$",'{:.2f}'.format(salarioNovo))
    
elif salarioAtual >= 700 and salarioAtual <= 1499.99:
    salarioNovo = float (salarioAtual*ajuste03)
    print("\n----------------------------------------------")
    print("                 Salário atual:","R$",'{:.2f}'.format(salarioAtual))
    print("Percentual de aumento aplicado:",'{:.2f}'.format((ajuste03-1)*100),"%")
    print("              Valor do aumento:","R$",'{:.2f}'.format(salarioNovo-salarioAtual))
    print("                  Novo salário:","R$",'{:.2f}'.format(salarioNovo))
    
elif salarioAtual >= 1500:
    salarioNovo = float (salarioAtual*ajuste04)
    print("\n----------------------------------------------")
    print("                 Salário atual:","R$",'{:.2f}'.format(salarioAtual))
    print("Percentual de aumento aplicado:",'{:.2f}'.format((ajuste04-1)*100),"%")
    print("              Valor do aumento:","R$",'{:.2f}'.format(salarioNovo-salarioAtual))
    print("                  Novo salário:","R$",'{:.2f}'.format(salarioNovo))


# In[27]:


#ListExerc30
print ("Calcular folha de pagamento.")
print ("----------------------------------------------------")

#calculo salario bruto:
valorHora = float (input ("Informe o valor da sua hora trabalhada: "))
print ("Informe a quantidade de horas/minutos trabalhadas no mês.")
quant_horas = int (input ("Informe a quantidade de horas:"))
quant_minutos = int (input ("Informe a quantidade de minutos:"))
total_horas_trabalhadas = float ((((quant_horas*60)+ quant_minutos)/60))

salarioBruto = float (valorHora*total_horas_trabalhadas)

#Descontos:
desconto_IR_01 = 0.05
desconto_IR_02 = 0.1
desconto_IR_03 = 0.2
desconto_INSS =  0.1
desconto_Sindicato = 0.03
desconto_FGTS = 0.11

#Calculos dos descontos
calculoDesc_IR_01 = salarioBruto*desconto_IR_01
calculoDesc_IR_02 = salarioBruto*desconto_IR_02
calculoDesc_IR_03 = salarioBruto*desconto_IR_03
calculoDesc_INSS = salarioBruto*desconto_INSS
calculoDesc_Sindicato = salarioBruto*desconto_Sindicato
calculo_FGTS = salarioBruto*desconto_FGTS

""" Critérios do Desconto do IR: 
Salário Bruto até 900 (inclusive) - isento 
Salário Bruto até 1500 (inclusive) - desconto de 5% 
Salário Bruto até 2500 (inclusive) - desconto de 10% """

if salarioBruto <= 900:
    salarioLiquido = salarioBruto-(calculoDesc_INSS+calculoDesc_Sindicato)
    
    print ("----------------------------------------------------")
    print("\n  i.       Salário Bruto:","R$",'{:.2f}'.format(salarioBruto))
    print("iii.          INSS (10%):","R$",'{:.2f}'.format(calculoDesc_INSS))
    print(" iv.           FGTS(11%):","R$",'{:.2f}'.format(calculo_FGTS))
    print("  v.  Total de descontos:","R$",'{:.2f}'.format(calculoDesc_INSS+calculoDesc_Sindicato))
    print(" vi.     Salário Liquido:","R$",'{:.2f}'.format(salarioLiquido))
    
elif salarioBruto > 900 and salarioBruto <= 1500:
    salarioLiquido = salarioBruto-(calculoDesc_IR_01+calculoDesc_INSS+calculoDesc_Sindicato)
    
    print ("----------------------------------------------------")
    print("\n  i.       Salário Bruto:","R$",'{:.2f}'.format(salarioBruto))
    print(" ii.             IR (5%):","R$",'{:.2f}'.format(calculoDesc_IR_01))
    print("iii.          INSS (10%):","R$",'{:.2f}'.format(calculoDesc_INSS))
    print(" iv.           FGTS(11%):","R$",'{:.2f}'.format(calculo_FGTS))
    print("  v.  Total de descontos:","R$",'{:.2f}'.format(calculoDesc_IR_01+calculoDesc_Sindicato))
    print(" vi.     Salário Liquido:","R$",'{:.2f}'.format(salarioLiquido))

elif salarioBruto >= 1500.01 and salarioBruto <= 2500:
    salarioLiquido = salarioBruto-(calculoDesc_IR_02+calculoDesc_INSS+calculoDesc_INSS+calculoDesc_Sindicato)
    
    print ("----------------------------------------------------")
    print("\n  i.       Salário Bruto:","R$",'{:.2f}'.format(salarioBruto))
    print(" ii.            IR (10%):","R$",'{:.2f}'.format(calculoDesc_IR_02))
    print("iii.          INSS (10%):","R$",'{:.2f}'.format(calculoDesc_INSS))
    print(" iv.           FGTS(11%):","R$",'{:.2f}'.format(calculo_FGTS))
    print("  v.  Total de descontos:","R$",'{:.2f}'.format(calculoDesc_IR_02+calculoDesc_INSS+calculoDesc_Sindicato))
    print(" vi.     Salário Liquido:","R$",'{:.2f}'.format(salarioLiquido))    

elif salarioBruto > 2500:
    salarioLiquido = salarioBruto-(calculoDesc_IR_03+calculoDesc_INSS+calculoDesc_Sindicato)
    
    print ("----------------------------------------------------")
    print("\n  i.       Salário Bruto:","R$",'{:.2f}'.format(salarioBruto))
    print(" ii.            IR (20%):","R$",'{:.2f}'.format(calculoDesc_IR_03))
    print("iii.          INSS (10%):","R$",'{:.2f}'.format(calculoDesc_INSS))
    print(" iv.           FGTS(11%):","R$",'{:.2f}'.format(calculo_FGTS))
    print("  v.  Total de descontos:","R$",'{:.2f}'.format(calculoDesc_IR_03+calculoDesc_INSS+calculoDesc_Sindicato))
    print(" vi.     Salário Liquido:","R$",'{:.2f}'.format(salarioLiquido))
    


# In[9]:


#ListExerc31
print ("Mostrar dia da semana.")
print ("----------------------------------------------------")

valor = int (input("Informe um número de 1 a 7: "))

if valor == 1:
    print("Domingo")
elif valor == 2:
    print("Segunda-feira")
elif valor == 3:
    print("Terça-feira")
elif valor == 4:
    print("Quarta-feira")
elif valor == 5:
    print("Quinta-feira")
elif valor == 6:
    print("Sexta-feira")
elif valor == 7:
    print("Sábado")
else:
    print("Valor inválido! Informe um número de 1 a 7.")


# In[14]:


#ListExerc32
print ("Avaliação da média do aluno.")
print ("----------------------------------------------------")

#coletando dados do aluno e das notas do aluno
nome = input("Informe o nome do aluno: ")
print ("----------------------------------------------------")
print("Informe as notas do aluno:")
nota1 = float(input("Nota - 1: "))
nota2 = float(input("Nota - 2: "))

#calculando a média aritmética das notas
mediaDasNotas = (nota1+nota2)/2

"""
A atribuição de conceitos obedece à tabela abaixo: 
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0       A
Entre 7.5 e 9.0        B
Entre 6.0 e 7.5        C
Entre 4.0 e 6.0        D
Entre 4.0 e zero       E
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 
"""

#Fazendo o tratamento das condicionais
if mediaDasNotas > 9:
    conceito = "A"
    situacao = "Aprovado"
    
elif mediaDasNotas >= 7.5 and mediaDasNotas <=8.99:
    conceito = "B"
    situacao = "Aprovado"
    
elif mediaDasNotas >= 6 and mediaDasNotas <=7.49:
    conceito = "C"
    situacao = "Aprovado"

elif mediaDasNotas >= 4 and mediaDasNotas <=5.99:
    conceito = "D"
    situacao = "Reprovado"
    
elif mediaDasNotas < 4:
    conceito = "E"
    situacao = "Reprovado"

#Fazendo a saída
print ("\n----------------------------------------------------")
print("Aluno:",nome)
print("Notas do aluno:",'{:.2f}'.format(nota1),"/",'{:.2f}'.format(nota2),"- Média:",'{:.2f}'.format(mediaDasNotas))
print("Conceito obtido:",conceito)
print("Situação:",situacao)
    


# In[41]:


#ListExerc33
print ("Verificar qual o tipo do triângulo.")
print ("----------------------------------------------------")

#Coletando os dados dos lados do triângulo
print("Informe três valores positivos para os lados do triângulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))


"""
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro
Triângulo Equilátero: três lados iguais;
Triângulo isósceles: quaisquer dois lados iguais; 
Triângulo Escaleno: três lados diferentes; 
"""

if lado1+lado2 > lado3 or lado2+lado3 > lado1 or lado1 + lado3 > lado2:
    print("Os valores formam um triângulo.")
    if lado1 == lado2 and lado2 == lado3:
        print("Os valores", lado1,"/",lado2,"/",lado3,"foram um triângulo Equilátero.")
    elif lado1==lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores", lado1,"/",lado2,"/",lado3,"foram um triângulo Isósceles.")
    elif lado1!=lado2 and lado1 != lado3 and lado2 != lado3:
        print("Os valores", lado1,"/",lado2,"/",lado3,"foram um triângulo Escaleno.")
else:
        print("Não é um triângulo!")


# In[54]:


#ListExerc34
print ("Equação do segundo grau.")
print ("----------------------------------------------------")

#Coletando os dados de A, B e C para ax2 + bx + c

print("Informe os valores para A, B e C: ")
print ("----------------------------------------------------")
a = float (input ("valor de A: "))
if a == 0:
    print("Não é equação de 2º grau")
    
else:
    b = float (input ("valor de B: "))
    c = float (input ("valor de C: "))

#calculo do Delta: Δ = b2 – 4ac
delta = float(b**2)-(4*a*c)

if delta < 0:
    print ("A equação não terá raízes reais, pois não existe raiz quadrada de número negativo.")
        
elif delta == 0:
    x = (-b)/2*a
    print ("Delta possui uma raiz:",x)
        #– b/2a
else:
#calculando X1 e X2
    x1 =  (-b + delta**0.5)/(2*a)
    x2 =  (-b - delta**0.5)/(2*a)
    print("Delta possui duas raizes:",x1,"|",x2)


# In[71]:


#ListExerc35/36 porque a questão 35 não existe
print ("Verificar se o ano é bissexto.")
print ("-------------------------------------------------")

ano = int(input("\nInforme um ano com 4 digitos (Ex.:1999): "))

#Fazendo o tratamento das condicionais
if ano % 4 == 0:
    print("O ano",ano, "é Bissexto.")
else:
    print("O ano",ano,"não é Bissexto.")


# In[76]:


#ListExerc37
print ("Calcular a média alcançada ")
print ("-------------------------------------------------")

#coletando dados do aluno e das notas do aluno
print("Informe notas do Aluno: ")
nota1 = float(input("1ª Nota: "))
nota2 = float(input("2ª Nota: "))
nota3 = float(input("3ª Nota: "))

#calculando a média aritmética das notas
media = (nota1+nota2+nota3)/3

#Fazendo o tratamento das condicionais
if media == 10:
    print("Aprovado com Distinção!","\nMédia:",'{:.1f}'.format(media))

elif media >= 7 and media <= 9.99:
    print("Aluno Aprovado!","\nMédia:",'{:.1f}'.format(media))

else:
    print("Aluno Reprovado!","\nMédia:",'{:.1f}'.format(media))



# In[32]:


#ListExerc38
print ("Caixa eletrônico.")
print ("=================================")

#coletando dados
print("Informe o valor do saque.\nValor minimo: R$10.0 | Valor maximo: R$600.0")
valor_saque = int(input("Valor: "))
while (valor_saque < 10 or valor_saque > 600):
    print("Valor inválido! Informe novamente!")
    valor_saque = int(input("Valor: "))
    
#calculo do saque conforme notas disponíveis ( 1, 5, 10, 50 e 100 reais)
nota_de_100 = valor_saque // 100
nota_de_50 = (valor_saque % 100) // 50
nota_de_10 = ((valor_saque % 100) % 50) // 10
nota_de_05 = (((valor_saque % 100) % 50) % 10) // 5
nota_de_01 = ((((valor_saque % 100) % 50) % 10) %5 ) // 1

print("Valor do saque: RS{:.1f} >>> Notas de R$100: {} | Notas de R$50: {} | Notas de R$10: {} | Notas de R$5: {} | Notas de R$1: {}".format(valor_saque,nota_de_100,nota_de_50,nota_de_10,nota_de_05,nota_de_01))


# In[70]:


#ListExerc39
print ("Verificar se o número é par ou impar.")
print ("--------------------------------------")

numero = int(input("Informe um número inteiro: "))

if numero % 2 == 0:
    print ("O número",numero,"é par.")
else:
    print ("O número",numero,"é impar.")


# In[76]:


#ListExerc39
#print ("O usuario escolhe a operação que se deseja realizar(soma, subtração, divisão ou multiplicação).")
#print ("--------------------------------------")

#coletando as entradas.
print("\n========================================================================")
print("\nInforme qual operação deseja realizar:\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
print("\n========================================================================")

operacao = input("Opção: ")

while(operacao != "1" and operacao != "2" and operacao != "3" and operacao != "4"): #tratamento da entrada de dados.
    print("\nOpção inválida! Digite novamene!")
    print("Escolha a operação: ")
    operacao = input("Opção: ")
    
operando1 = float(input("Digite o operando 1: "))
operando2 = float(input("Digite o operando 2: "))

while (operacao == "4" and operando2 == 0): #tratamento da tentativa de divisão por zero.
    print("Tentativa de divisão por zero")
    operando2 = float(input("Digite o operando 2: "))
    
#Realizando os caluclos das operações.
resultado = 0.0
if operacao == "1":
    resultado = operando1 + operando2
elif operacao == "2":
    resultado = operando1 - operando2
elif operacao == "3":
    resultado = operando1 * operando2
elif operacao == "4":
    resultado = operando1 / operando2

#Realizando o tratanmento das saídas.
'''
O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
par ou ímpar; 
positivo ou negativo; 
inteiro ou decimal. 
'''
'''
Teste para resolver o problema com a condição envolvendo decimal.

numero = float(input())

if(numero // 1 == numero): 
    print('\nNúmero inteiro!') 
else: 
    print('\nNúmero Decimal!')
    
'''
if (resultado % 2) == 0 and resultado > 0 and (resultado // 1) == resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Par|Positivo|Inteiro".format(resultado))    
elif (resultado % 2) == 0 and resultado < 0 and (resultado // 1) == resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Par|Negativo|Inteiro".format(resultado))
elif (resultado % 2) == 0 and resultado > 0 and (resultado // 1) != resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Par|Positivo|Decimal".format(resultado))
elif (resultado % 2) == 0 and resultado < 0 and (resultado // 1) != resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Par|Negativo|Decimal".format(resultado))
elif (resultado / 2) != 0 and resultado > 0 and (resultado // 1) == resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Impar|Positivo|Inteiro".format(resultado))
elif (resultado // 2) != 0 and resultado < 0 and (resultado // 1) == resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Impar|Negativo|Inteiro".format(resultado))
elif (resultado / 2) != 0 and resultado > 0 and (resultado // 1) != resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Impar|Positivo|Decimal".format(resultado))
elif (resultado // 2) != 0 and resultado < 0 and (resultado // 1) != resultado:
    print("\n========================================================================")
    print("O resultado da operação é {:.2f}, o valor é Impar|Negativo|Decimal".format(resultado))

