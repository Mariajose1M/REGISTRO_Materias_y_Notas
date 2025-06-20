print("EJERCICIO 6")
print("***********************************************************************************************")

materias= []
materias.append(input("Ingrese la primer materia:"))
materias.append(input("Ingrese la segunda materia:"))
materias.append(input("Ingrese la tercera materia:"))
print(f"Las materias ingresadas son: {materias}")

notas= []
notas.append(float(input("Ingrese la primer nota:")))
notas.append(float(input("Ingrese la segunda nota:")))
notas.append(float(input("Ingrese la tercera nota:")))
print(f"Las notas ingresadas son: {notas}")

print("***********************************************************************************************")

print("Instruccion 1")


if "Biologia" in materias:
    materias.append("Fisica")
    print(f"Materias modificadas modificada:{materias}")
else:
    print("materia no encontrada")
    
print("***********************************************************************************************")
print("Instruccion 2")

if 2.8 in notas:
    notas.append(5.0)
    print(f"Notas modificadas:{notas}")
else:
    print("Nota no encontrada")
    
print("***********************************************************************************************")
print("Instruccion 3")

if "Lengua" in materias:
    materias.remove("Lengua")
    print(f"Materias eliminadas:{materias}")
else:
    print("Materia no encontrada")
    
print("***********************************************************************************************")
print("Instruccion 4")

cantidad= len(notas)
print(f"cantidad de notas:{cantidad}")

if cantidad >= 3:
    notas.pop(0)
    print(f"Nota eliminada:{notas}")
else:
    print("No se puede eliminar la nota")
    
print("***********************************************************************************************")
print("Instruccion 5")

if "Matematicas" in materias:
    materias.append("Algebra")
    print(f"Materias modificadas:{materias}")
else:
    print("Materia no encontrada")
    
print("***********************************************************************************************")
print("Instruccion 6")

favoritas= materias[:2]
print(f"Materias favoritas:{favoritas}")

print("***********************************************************************************************")
print("Instruccion 7")

notas_altas= notas[-2:]
print(f"Notas altas:{notas_altas}")

print("***********************************************************************************************")
print("Instruccion 8")

if "Fisica" in materias:
    asignatura_extra= ("Fisica", 5.0)
    print(f"Asignatura extra:{asignatura_extra}")
else:
    print("Asignatura extra no encontrada")
    
print("***********************************************************************************************")
print("Instruccion 9")

suma= sum(notas_altas)
print(f"La suma de las notas altas es: {suma}")

if suma>8:
    favoritas.append("Excelente")
    print(f"Lista actualizada: {favoritas}")
else:
    print("No se puede agregar Excelente a la lista")
    
print("***********************************************************************************************")
print("Instruccion 10")

if "Excelente" in favoritas:
    reporte={"mejores materias": favoritas,"promedio": sum(notas_altas)/len(notas_altas)}
    print(f"Reporte: {reporte}")
else:
    print("No se puede generar el reporte")
    
    print("***********************************************************************************************")
print("Instruccion 11")

if "reporte" in locals():
    reporte["estado"] = "Destacado"
    print(f"El diccionario modificado:{reporte}")

else:
    print("reporte no es un diccionario")
    
print("***********************************************************************************************")
print("Instruccion 12")

if "Geografía" not in materias:
    materias.append("Geografía")
    print(f"materia agregada:{materias}")

else:
    print("Geografia ya esta")
    
print("***********************************************************************************************")
print("Instruccion 13")

if "Álgebra" in materias and "Física" in materias:
    materias.remove("Física")
    print(f"materia eliminada:{materias}")

else:
    print("La materia no se puede eliminar")
    
print("***********************************************************************************************")
print("Instrucciones 14")

print("Resultados Finales:")
print(f"Materias:{materias}, notas:{notas},materias favoritas: {favoritas}, notas altas: {notas_altas}")

if asignatura_extra in locals():
    print(f"Asignatura extra:{asignatura_extra}")
else:
    print("No hay asignatura extra")

if "reporte" in locals():
    print(f"Reporte: {reporte}")
else:
    print("Reporte no fue creado")