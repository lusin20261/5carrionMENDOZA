from click import option


print("===========================================================")
print("=============mi calculadora de la marca verity=============")
print("===========================================================")

while True:
    print("")
    print("elije la operacion que quieras")
    print("1.sumar")
    print("2.restar")
    print("3.multiplicacion")
    print("4.divicion")
    print("------------------------------")

    option =input("elige una opsion")

    if (option =="1"):
        num1 = input("ingrese el primer numero: ")
        num1 = int(num1) 
        num2 = input("ingrese el segundo numero: ")
        num2 = int(num2)
        print("el resultado de la suma es:",num1+num2)

    elif (option =="2"):
        num1 = input("ingrese el primer numero: ")
        num1 = int(num1)
        num2 = input("ingrese el segundo numero: ")
        num2 = int(num2)
        print("el resultado de la diferencia es:",num1-num2)

    elif       