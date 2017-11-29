from alunos import Aluno

nome = input('digite o nome do aluno \n')
celular = 0000000
email = 'email@email.com'
ra = input('digite o R.A do aluno \n')
aluno = Aluno(nome,celular,email,ra)
maximo_bd = 2
maximo_si = 2
numero_bd = 0
numero_si = 0
x = ''
lista = []
while x == '':
    t = 0
    print('logado como: {} \nR.A: {}'.format(nome,ra))
    print('===Disciplinas para matricula===')
    print('===BD : Banco de dados===')
    print('===SI : Sistema da informação===')
    print('===Escolha a sua===')
    res = input('(A) - Banco de dados \n(B) - Sistema da informação \n')
    res.lower()
    if res == 'a':
        if ra in lista :
            print('você já está matriculado nessa disciplina !!')
        elif ra not in lista:
            aluno.aviso(numero_bd,maximo_bd)
            print('você escolheu a disciplina Banco de dados, boa escolha !!!')
            numero_bd += 1
            lista.append(ra)
            while t < 5900000:
                t += 1
    elif res == 'b':
        if ra in lista :
            print('você já está matriculado nessa disciplina !!')
        elif ra not in lista:
            aluno.aviso(numero_si,maximo_si)
            print('você escolheu a disciplina Sistema da informação, belissima escolha !!!')
            numero_si +=1
            while t < 5900000:
                t += 1
    else:
        print('opção invalida')
    x = input('aperte enter para fazer matricula denovo, ou confirme outra tecla para sair')