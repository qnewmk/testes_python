from datetime import datetime
hoje = datetime.today()
data_entrega= datetime.now()
dia = int(input('digite o dia de entrega'))
mes = int(input('digite o mes de entrega'))
ano = int(input('digite o ano de entrega'))
data_entrega.day = dia
data_entrega.month = mes
data_entrega.year - ano
data_entrega = datetime.hour = 0
data_entrega = datetime.minutes = 0
data_entrega = datetime.seconds = 0
if hoje < data_entrega :
    print('pode enviar tarefa')
elif hoje > data_entrega :
    print('prazo expirado')