#print("resultado")
import mysql.connector

"""miconexion =mysql.connector.connect(host="localhost", user="root",password="1234",db="pruebadb")
cur =miconexion.cursor()
cur.execute("SELECT idMiTabla1, Nombre FROM pruebadb.mitabla1")

for idMiTabla1, Nombre in cur.fetchall():
    print(idMiTabla1,"-",Nombre)


miconexion.close()
"""

class Nombres:
    def crear(self):
        miconexion =mysql.connector.connect(host="localhost", user="root",password="1234",db="pruebadb")
        return miconexion
    
    def cargar(self,datos):
        cone =self.crear()
        cursor = cone.cursor()
        #sql =("INSERT INTO mitabla1(Nombre) VALUES ('%s')" %(datos))
        #cursor.execute(sql,datos)
        cursor.execute("INSERT INTO mitabla1(Nombre) VALUES ('%s')" %(datos))
        cone.commit()
        cone.close()
        
    def consultar(self,datos):
        fila ="No existe"
        cone =self.crear()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM mitabla1 WHERE Nombre LIKE %s", datos)
        for fila in cursor:
            print(fila)
        cone.close()
        if len(fila)>0:
            return fila
        else:
            return fila
    
    def eliminar(self,datos):
        cone =self.crear()
        cursor = cone.cursor()
        cursor.execute("DELETE FROM mitabla1 WHERE idMiTabla1= %s",datos)
        cone.commit()
        cone.close()
        
    def modificacion(self,datos):
        cone =self.crear()
        cursor = cone.cursor()
        cursor.execute("UPDATE mitabla1 SET Nombre= %s WHERE idMiTabla1= %s",datos)
        cone.commit()
        cone.close()