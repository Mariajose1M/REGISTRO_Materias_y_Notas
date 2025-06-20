print("Promedio de notas")
no1= float(input("Ingrese la primer nota:"))
no2= float(input("Ingrese la segunda nota:"))
no3= float(input("Ingrese la tercera nota:"))
prom=(no1+no2+no3)/3
if prom>= 3.0:
    print("Aprueba")
elif prom>=2.0 and prom<=2.9:
    print("Habilita")
else:
    print("Pierde")
    