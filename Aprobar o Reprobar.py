from tokenize import Double


nota = input("Ingrese nota 1: ")
nota = float(nota)
corte1 = float(0.3)
cal = nota * corte1
cal = round (cal, 2)
cal = str(cal,)
print ("Su nota del primer corte es : " + cal)

nota2 = input ("Ingrese nota 2: ")
nota2 = float(nota2)
corte2 = float(0.3)
cal2 = nota * corte2
cal2 = round (cal2, 2)
cal2 = str(cal2,)
print ("Su nota del primer corte es : " + cal2)

nota3 = input ("Ingrese nota 3: ")
nota3 = float(nota3)
corte3 = float(0.4)
cal3 = nota * corte3
cal3 = round (cal3, 2)
cal3 = str(cal3,)
print ("Su nota del primer corte es : " + cal3)

notaFinal = float(cal) + float(cal2) + float(cal3)


if notaFinal >= 3:
    print ("Usted Aprobo")

else:
    print("Usted Reprobo")

