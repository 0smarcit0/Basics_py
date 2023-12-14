print("colores. \n")

color_b = input("seleccione el color base. Rojo (r) o verde (v): ")

if color_b == "r": 
    color_s = input("seleccione el color secundario. Amarillo (am) o Azul (a): ")
    if color_s == "am":
        print("el color resultante es anaranjado ")
    else:
        print("el color resultante es purpura")
elif color_b == "v":
    color_s= input("seleccione el color secundario. Amarillo (am) o Azul (a): ")
    if color_s == "am":
        print("el color resultante es amarillo verdoso ")
    else:
        print("el color resultante es azul verdoso")
else:
    print("dato incorrecto")               
        
   