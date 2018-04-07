print ("<-Calculadora->")
N1 =int(input("Introduce el 1 Valor "))
N2 =int(input("Introduce el 2 Valor "))

print ("Que operacion desea realizar?")
print ("a) Suma")
print ("b) Resta")
print ("c) Multiplicacion")
print ("d) Divicion")

opcion = input ("Elija una opcion")

if opcion =="a":
    suma =N1+N2
    print ("calculando...")
    print ("El resultado es ",suma)
if opcion =="b":
    resta =N1-N2
    print ("calculando...")
    print ("El resultado es ",resta)
if opcion =="c":
    multiplicacion =N1*N2
    print ("calculando...")
    print ("El resultado es ",multiplicacion)
if opcion =="d":
    divicion =N1/N2
    print ("calculando...")
    print ("El resultado es ",divicion)
