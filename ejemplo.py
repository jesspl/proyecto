# def i(x):
#     if i >= 0:
#         print(x)
#         i(x-1)


# i(10)

# def cuentaRegresiva(num):
#     if num >= 0:
#         print(num)
#         cuentaRegresiva(num-1)

# cuentaRegresiva(10)

#RETO GRUPAL: Función factorial recursiva.
#factorial(4) -> 4 * 3 * 2 * 1
#RETO GRUPAL: Función factorial recursiva. Crear una función que reciba un número y regrese el número factorial
#factorial(4) -> 4 * 3 * 2 * 1

def sigma(num):
    if num==1:
        return 1
    else: 
        return num * sigma(num-1)

print (sigma(3))

def fibo(num):
    if num==1:
        return 0
    elif num== 2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
    