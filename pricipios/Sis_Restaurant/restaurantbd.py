import mysql.connector 
from tkinter import messagebox as mb

class Restaurant:
    #abrimos la conexion:
 def crear(self):
       miconexion = mysql.connector.connect(host="localhost", user="root",password="1234",db="restaurantebd")
       
       return miconexion
   

    #funcion de insertar y consultar pedido
 def cargar(self,cargar_datos,numero_mesa):
     #separar en 2 listas independientes el id y cantidad
     idplato = list(map(int, cargar_datos[0]))
     cantidad =  list(map(int, cargar_datos[1]))
     
     #recorrer las 2 listas simultaneamente y ejecutar insert para cada par de datos
    
     for cant,idp in zip(cantidad, idplato):
         cone = self.crear()
         cursor = cone.cursor()
         cursor.execute("INSERT INTO mesa(Num_Mesa, Cantidad, Condicion, idPlato) VALUES(%s,'%s','no facturado','%s')"%(numero_mesa,cant,idp))
        
     mb.showinfo("informacion","los datos fueron cargados")
     #consultar mesa para retornar y mostrar el pedido en el treeview self.pedido_carga
     cone =self.crear()
     cursor = cone.cursor()
     cursor.execute("SELECT M.cantidad as 'Cant.',P.Nombre_Plato as 'Descrip.',P.Precio as 'Pre.Uni.',TRUNCATE (Cantidad*P.Precio,1)as 'Pre.Total' FROM mesa M, plato P WHERE M.Condicion like 'No Facturado' and M.idPlato = P.idPlato and M.Num_Mesa = %s" % (numero_mesa)) 
     informacion = cursor.fetchall() 
     cone.close() 
     return informacion
 
 #Consultar si hay platos para cargar en treeView al abrir la ventana de una mesa 
 def cargar_plato_treeview(self, numero_mesa): 
     cone = self.crear() 
     cursor = cone.cursor() 
     cursor.execute("SELECT M.Cantidad as 'Cant.',P.Nombre_Plato as 'Descrip.', P.Precio as 'Pre.Uni.', TRUNCATE (Cantidad*P.Precio, 1) as 'Pre.Total' FROM mesa M, plato P WHERE M.Condicion like 'No Facturado' and M.idPlato = P.idPlato and M.Num_Mesa = %s" % (numero_mesa)) 
     info = cursor.fetchall() 
     cone.close() 
     return info
         
     
     
  
 
     
         