import operaciones as op

operacion = input("Ingrese la operacion a realizar(sumar, restar, dividir, multiplicar): ")
primernumero = float(input("Ingrese su primer numero: "))
segundonumero = float(input("Ingrese su segundo numero: "))

if operacion == "sumar":
    print(op.sumar(primernumero, segundonumero))
    
elif operacion == "restar":
    print(op.restar(primernumero, segundonumero))
    
elif operacion == "multiplicar":
    print(op.multiplicar(primernumero, segundonumero))
    
elif operacion == "dividir":
    print(op.dividir(primernumero, segundonumero))