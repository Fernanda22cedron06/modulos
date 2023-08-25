"""Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro."""
fin=int(input("Ingrese el limite "))
n=1
primos=[]
def nprimos():
    while n<fin:
         resto=0
    for i in range(1,fin):
        #pregunto si el resto es igual a 0    
        if n%i==0:
            resto+=1
        if resto<3:
            print(n)
    primos.append(n)
n+=1
print("Numeros primos "+primos)

""" Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
que el usuario ingrese ‘salir’"""
salida=""
lista=[]
while(salida!="salir"):
    salida=input("Ingrese condimento (salir p/salir): ")
    if salida!="salir":
        if salida in lista:
            print("ya agrego esto")
        else:
            print(salida)
            lista.append(salida)
print(lista)

salida=""
lista=[]
while True:
    salida=input("Ingrese condimento (salir p/salir): ")
    if salida!="salir":
        if salida in lista:
            print("ya esta")
        else:
            lista.append(salida)
    else:
        break
print(lista)

"""Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. """

def hacer_remera(tamanio="l",mensaje="me gusta python"):
    print("Su remera es talle ",tamanio," y se imprimira ",mensaje)

hacer_remera()
hacer_remera("m",mensaje="genial")

"""Serie de Fibonacci"""
def fibonacci(n):
    lista=[0]
    a=1
    b=1
    lista.append(a)
    lista.append(b)
    for i in range(3,n):
        c=a+b
        a=b
        b=c
        lista.append(c)
    return lista
fin=int(input("ingrese tope: "))
print(fibonacci(fin))

"""Conversión imperial"""

# 1 Gramo = 0.0022 Libra
# 1 Cm = 0.393701 Pulgada
# 1 Km = 0.621371 Millas
LPM=[0.0022,0.393701,0.621371]

while True:
    v1=float(input("Valor 1 "))
    opcion=int(input("1 gr a lib - 2 cm a pu - 3 km a mi / 4 lib a gr - 5 pu a cm - 6 mi a km (0 p/salir) "))
    if opcion==0:
        print("Muchas gracias")
        break
    elif opcion==1:
        print(str(v1) + " gr = "+ str(v1*LPM[0])+" lib")
    elif opcion==2:
        print(str(v1) + " cm = "+str(v1*LPM[1])+" pul")
    elif opcion==3:
        print(str(v1) + " km = "+str(v1*LPM[2])+" mil")
    elif opcion==4:
        print(str(v1) + " lib = "+str(v1/LPM[0])+" gr")
    elif opcion==5:
        print(str(v1) + " pul = "+str(v1/LPM[1])+" cm")
    elif opcion==6:
        print(str(v1) + " mil = "+str(v1/LPM[2])+" km")
    else:
        print("invalido")

""" un año es bisiesto """

#a

def bisiesto(a):
    b=True
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                b=True
            else:
                b=False
        else:
            b=False
    else:
        b=False
    return b

#b

anio=int(input("Escriba el año para saber si es bisiesto: "))
if(bisiesto(anio)):
    print("Es bisiesto")
else:
    print("no es bisiesto")
           
def bisiesto(a):
    b=True
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                b=True
            else:
                b=False
        else:
            b=False
    else:
        b=False
    return b

anio=int(input("Escriba el año donde quiera detener la prueba: "))
bisiestos=[]
for i in range(2000,anio):
    if(bisiesto(i)):
        print(str(i))
        bisiestos.append(i)

print(bisiestos)

"""los números naturales"""
num=[]
suma=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        suma+=i
        num.append(i)
print(num)
print(suma)
