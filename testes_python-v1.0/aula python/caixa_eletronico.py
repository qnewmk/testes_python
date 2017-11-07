from Contas import Conta
from Cliente import Cliente
from Bancos import Banco
import os
contador=0
m = 0
g = ('haha')
while (m==0):
    if(g !="pos"):
        m = input('possui conta ?(S/N)')
    else:
        if(m == 's'):
            numero = int(input('digite sua conta:'))
            res = ("s")
            while (res == 's'):
                os.system('cls')
                print('oque deseja fazer?\n')
                print('d : deposito')
                print('s : saque')
                print('f : sair')
                i = input('e : extrato\n')
            
                if(i == 'd'):
                    os.system('cls')
                    x = int(input('Qual o valor do deposito ?\n'))
                    teste.deposito(x)
                    print('operação realizada com sucesso!!!')
                elif(i == 's'):
                    os.system('cls')
                    x = int(input('qual o valor do saque ?\n'))
                    teste.saque (x)
                    o = 20000000
                    while (o > 0 ):
                        o -= 1
                elif(i == 'e'):
                    os.system('cls')
                    teste.extrato()   
                    print('seu saldo é de : ',teste.saldo)
                elif(i == 'f'):
                    k += 6  
                else:
                    os.system('cls')
                    print('comando desconhcido...')
                    res = input('deseja tentar denovo? (S/N)\n')
                    if(res =='n'):
                        break
    elif(m == 'n'):
        os.system('cls')
        nome = input('digite seu nome : ')
        telefone = int (input('digite seu telefone :'))
        contador += 2
        user = Cliente(nome, telefone)
        acc = Conta(0, nome, contador)
        Bank = Banco('Ermanoteu')
        print('o seu numero de conta é: {}'.format(contador))
        o = 20000000
        while (o > 0 ):
            o -= 1
        m = 0
        g = ('pos')