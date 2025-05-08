#Estrutura para saber qual número é maior

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num1 > num2:
    print('O primero valor é maior')
else:                                #Se caso o primeiro bloco não for True, o Else e executado
    print('O segundo valor é maior')


#Estrutura para saber se tem idade para votar
from datetime import date

ano = int(input('Digite o ano de nascimento'))
hoje = date.today().year
sub = hoje - ano           #Utilizando a biblioteca date, para saber o ano atual e subtrair com o ano de nascimento

if sub > 16:
  print('Ela tem idade para votar')
else:
  print('Ainda não possui a idade necessária')

#Estrutura das notas

nota = 75 
 
if nota >= 90: 
    print("Nota A") 
elif nota >= 80: 
    print("Nota B") 
elif nota >= 70:        #Como a nota é 70, ele executara esse bloco da estrutura
    print("Nota C") 
else: 
    print("Nota D")

#Estrutura se a pesso tem CNH

idade = int(input('Digite sua idade: '))
cnh = True

if idade >= 18:
    if cnh:
        print('Tem idade e possui CNH')
    else:
        print('Não dirigi sem a carteira')
else:
    print('Não tem carteira por ser menor de idade')
    




















