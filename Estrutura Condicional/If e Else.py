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
























