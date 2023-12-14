import math  #llamamos a la libreria math para usar la funcion math.pi para la operacion 

print("VOLUMEN DE CILINDRO. \n ")

r_cilindro = float(input("Ingrese el radio del cilindro (en cm): "))   #pedimos y almacenamos datos 
                                                                                   
h_cilindro = float(input("Ingrese la altura del cilindro (en cm): "))              

volumen = math.pi * pow(r_cilindro, 2) * h_cilindro          #hacemos la operacion con math.pi que nos provee el valor de PI

p_capacidad =  volumen>= 0 and volumen <= 100                #en esta parte definimos las variables que nos ayudaran a determinar la capacidad del cilindro

m_capacidad = volumen >= 110 and volumen <=200 

a_capacidad = not volumen <210

print("\n")

if p_capacidad == True:                                                         #nos apoyamos en condicionales simples para ver determinar si el valor del volumen encaja en algunos de los rangos, si es asi, imprimimos el valor y el tipo de cilindro 
    
    print("el cilindro es de poca capacidad. ")
    print("el volumen del cilindro es: %.2f" %volumen, "centimetros cubicos")


if m_capacidad == True: 
    print("el cilindro es de media capacidad. ")
    print("el volumen del cilindro es: %.2f" %volumen, "centimetros cubicos")
    
if a_capacidad == True:
    print("el cilindro es de alta capacidad. ")
    print("el volumen del cilindro es: %.2f" %volumen, "centimetros cubicos")
    










