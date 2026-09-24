def sumar(a: int, b: int):
    return a + b

def saludar(nombre: str):
    saludo = f"Hola {nombre}"
    return saludo

def regsitro(nombre:str , password:str):
    registro_exitoso= f"Bienvenido {nombre} al sistema su contraseña es {password}"
    return registro_exitoso

#Primer funcion
num1 = 3
num2 = 4
print("La suma de 3 + 4 es: ",sumar(num1, num2))

#Segunda funcion
nombre = "Esau"
print(saludar(nombre))

#Tercera
password = 1234
print(regsitro(nombre, password))