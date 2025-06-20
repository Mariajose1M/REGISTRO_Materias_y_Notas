print("Clasificacion de edad por grupo")
edad= int(input("Ingrese su edad para clasificarlo en un grupo:"))
if edad>=0 and edad<=12:
    print("Usted se encuentra en el grupo: Niño")
elif edad>=13 and edad<=17:
    print("Usted se encuentra en el grupo: Adolescente")
elif edad>=18 and edad<=64:
    print("Usted se encuentra en el grupo: Adulto")
else:
    print("Usted se encuentra en el grupo: Adulto mayor")
    
    