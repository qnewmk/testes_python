from datetime import datetime
now = datetime.now()
#print('{}/{}/{}\n{}:{}:{}'.format(now.year,now.month,now.day,now.hour,now.minute,now.second))
dia = input('digite dia de entrega\n')
mes = input('digite mes de entrega\n')
ano = input('digite ano de entrega\n')
data = (dia+'/'+mes+'/'+ano)
data_atual = (now.day+'/'+now.month+'/'+now.year)
if data < data_atual:
    print('data de entrega ')