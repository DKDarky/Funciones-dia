#Ejemplo para calcular el area del triangulo

#Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#invocamos la funcion
resultado = calcularAreaTriangulo(base,altura)
#salida
print(f"El area del trianguolo es {base} y la altura {altura} es: ", resultado)

#Funcion con argumento predeterminados
def my_function(country = "Colombia"):
    print("I am from " + country)

#invocar la funcion
my_function()
my_function("Sweeden ")
my_function("India")
my_function("Brazil")

#Argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: " + args[2])


#Invocamos la funcion
mostrarEstudiantes("Emil","Tobias","Linus")

#Argumentos de palabra clave

def mostrarCarros(Carro1,Carro2,Carro3):
    print("El carro es: " + Carro2)

#Invocamos la funcion
mostrarCarros(Carro1 = "AMW", Carro3 = "Ferrari", Carro2 = "Ford")

#Argumento Arbitrario *+kwargs
def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["Apellido"])

mostrarCliente(nombre = "Tobias", Apellido = "Rafsnes")

#Declaracion de paso

def miFuncion():
    pass


#Funcion integradas
x = main(5, 10, 25)
y = main(5, 10, 25)

print(x)
print(y)

#funciones pow
num1 = pow(7, 4)

print(num1)

#modulo de matematicas
import math

num2 = math.sqrt(34)

print(num2)

#Modulo matematicas

import math

num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) #returns 8
print(num4) #returns 7