import tkinter as tk
from tkinter import messagebox as mb
import PruebaDB

class Aplicacion(tk.Frame):
    def __init__(self,master =None):
        super().__init__(master)
        self.master = master
        self.nombres = PruebaDB.Nombres()
        self.pack()
        self.widgets()
    
    def widgets(self):
        self.nombre = tk.StringVar()
        self.encontrado = tk.StringVar()
        self.eliminar = tk.StringVar()
        self.nuevo_valor=tk.StringVar()
        self.idnuevo_valor=tk.StringVar()
        
        self.titulo1 =tk.Label(self.master,text="ingrese el nombre: ").place(x=50,y=20)
        self.entrada1=tk.Entry(self.master,textvariable=self.nombre).place(x=50,y=40)
        
        self.titulo2 =tk.Label(self.master,text="consulta: ").place(x=50,y=60)
        self.entrada2=tk.Entry(self.master,textvariable=self.encontrado,state="readonly").place(x=50,y=80)
        
        self.titulo3 =tk.Label(self.master,text="ingrese el identificador a eliminar: ").place(x=50,y=100)
        self.entrada3=tk.Entry(self.master,textvariable=self.eliminar).place(x=50,y=120)
        
        self.titulo4 =tk.Label(self.master,text="ingrese el nuevo nombre: ").place(x=50,y=140)
        self.entrada4=tk.Entry(self.master,textvariable=self.nuevo_valor).place(x=50,y=160)
        
        self.titulo5 =tk.Label(self.master,text="ingrese el ID del nuevo nombre: ").place(x=50,y=180)
        self.entrada5=tk.Entry(self.master,textvariable=self.idnuevo_valor).place(x=50,y=200)
        
        
        self.boton1 =tk.Button(self.master,text="consultar",fg="red",command=self.consultar_nombres).place(x=50,y=300)
        
        self.boton2 =tk.Button(self.master,text="almacenar",fg="red",command=self.cargar_nombres).place(x=120,y=300)
        
        self.boton3 =tk.Button(self.master,text="eliminar",fg="red",command=self.eliminar_nombres).place(x=50,y=325)
        
        self.boton4 =tk.Button(self.master,text="modificar",fg="red",command=self.modificar_nombres).place(x=120,y=325)
         
    
    
    def modificar_nombres(self):
        datos=(self.nuevo_valor.get(),self.idnuevo_valor.get(),)
        self.nombres.modificacion(datos)
        mb.showinfo("info","se modifico con exito")
        self.nuevo_valor.set("")
        self.idnuevo_valor.set("")
        
    def eliminar_nombres(self):
        datos=(self.eliminar.get(),)
        self.nombres.eliminar(datos)
        mb.showinfo("info","el nombre ha sido eliminado")
        self.eliminar.set("")
        
    def cargar_nombres(self):
         datos = (self.nombre.get(),)
         self.nombres.cargar(datos)
         mb.showinfo("info","los datos fueron cargadoss")
         self.nombre.set("")
    def consultar_nombres(self):
        datos =(self.nombre.get(),)
        respuesta =self.nombres.consultar(datos)
        self.encontrado.set(respuesta)
        
        

app = Aplicacion
ventana =tk.Tk()
ventana.geometry("350x400")
ventana.wm_title("prueba")
app(master=ventana)
ventana.mainloop()
        
            