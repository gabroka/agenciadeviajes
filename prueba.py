import datetime

#print(help(datetime))
fecha_actual=datetime.datetime.today().strftime('%d%m%y')
print(fecha_actual,'-',type(fecha_actual))