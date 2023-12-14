print("Estaciones. ")

estacion = input("ingrese la estación en la que se encuentra: ") #se solicita la estación

if estacion == "otoño":                                           #en caso de otoño
    mes = input( " abarca los meses marzo, abril y mayo. Ingrese en que mes se encuetra: ")
    if mes == "marzo": 
        print("usted se encuentra a principios de otoño.")
    elif mes == "abril":
        print("usted se encuentra a mediados de otoño.")
    elif mes == "mayo":
        print("usted se encuentra a finales de otoño.")
elif estacion == "invierno":                                      #en caso de invierno 
    mes = input( " abarca los meses junio y julio. Ingrese en que mes se encuetra: ")
    if mes == "junio": 
        print("usted se encuentra a principios de invierno.")
    elif mes == "julio":
        print("usted se encuentra a finales de invierno.")
elif estacion == "primavera":                                     #en caso de primavera 
    mes = input( " abarca los meses septiembre, octubre y noviembre. Ingrese en que mes se encuetra: ")
    if mes == "septiembre": 
        print("usted se encuentra a principios de primavera.")
    elif mes == "octubre":
        print("usted se encuentra a mediados de primavera.")
    elif mes == "noviembre":
        print("usted se encuentra a finales de primavera.")
elif estacion == "verano":                                       #en caso de verano 
    mes = input( " abarca los meses diciembre, enero y febrero. Ingrese en que mes se encuetra: ")
    if mes == "diciembre": 
        print("usted se encuentra a principios de verano.")
    elif mes == "enero":
        print("usted se encuentra a mediados de verano.")
    elif mes == "febrero":
        print("usted se encuentra a finales de verano.")
else:                                                         #en caso de un dato no registrado 
    print("error")
    
        
    