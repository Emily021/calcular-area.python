import math

# Paso 1 : Solicitar al usuario que ingrese el radio del circulo.
 #   Mostrar mensaje: "Ingrese el radio del circulo" 
 #   Leer el dato ingresado y asignarlo a variable radio


radio = float(input("Ingrese el radio del circulo"))
    #Paso 2 : Calcular el area del circulo utilizando la formula area = 3.14 * radio^2
  #  Definir y asignar a la variable area el resultado de 3.14 * radio^2

area = math.pi * (radio**2)
    #Paso 3 : Mostrar al usuario el area calculada
  #  Mostrar mensaje: "El area del circulo con radio", radio, "es:" area
  
print("El area del circulo con radio", radio, "es:", area)