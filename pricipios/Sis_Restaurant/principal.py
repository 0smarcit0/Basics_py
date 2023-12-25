import tkinter as tk 
from tkinter import messagebox as mb
from io import open
from tkinter import ttk
from datetime import datetime
import restaurantbd

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        
        self.master=master
        self.mobiliario()
        self.conectar = restaurantbd.Restaurant()
        
        
        self.pack()
    
    
    def mobiliario(self):
        self.mesa1 = tk.Button(self.master,bg="orange",text="mesa1",fg="white",width=10,height=5,command=lambda:self.pedido(1)).place(x=100,y=100)
        self.mesa2 = tk.Button(self.master,bg="orange",text="mesa2",fg="white",width=10,height=5,command=lambda:self.pedido(2)).place(x=200,y=100)
        self.mesa3 = tk.Button(self.master,bg="orange",text="mesa3",fg="white",width=10,height=5,command=lambda:self.pedido(3)).place(x=300,y=100)
        self.mesa4 = tk.Button(self.master,bg="orange",text="mesa4",fg="white",width=10,height=5,command=lambda:self.pedido(4)).place(x=100,y=200)
        self.mesa5 = tk.Button(self.master,bg="orange",text="mesa5",fg="white",width=10,height=5,command=lambda:self.pedido(5)).place(x=200,y=200)
        self.mesa6 = tk.Button(self.master,bg="orange",text="mesa6",fg="white",width=10,height=5,command=lambda:self.pedido(6)).place(x=300,y=200)
        
        self.generar = tk.Button(self.master,bg="green",text="generar reporte de caja",fg="white",width=17,height=6).place(x=100,y=450)
        self.salir = tk.Button(self.master,bg="red",text="salir del programa",fg="white",width=15,height=6,command=self.master.destroy).place(x=250,y=450)
        self.caja = tk.Button(self.master,bg="grey",text="caja",fg="white",width=15,height=6,state="disabled").place(x=700,y=450)
        self.barra = tk.Button(self.master,bg="brown",fg="white",text="barra",width=8,height=30,state="disabled").place(x=700,y=0)
        self.cocina = tk.Button(self.master,bg="brown",fg="white",text="cocina",width=8,height=20,state="disabled").place(x=800,y=0)
        
        
    def pedido(self,numero_mesa):
        self.pedido_seleccion =tk.Toplevel(self.master,bg="lightblue",width=800,height=600,)
        self.pedido_seleccion.title("hola")
        
        
        
        self.sopa = tk.IntVar()
        self.pollo = tk.IntVar()
        self.pez = tk.IntVar()
        self.ensalada = tk.IntVar()
        self.refresh = tk.IntVar()
        self.cerdo = tk.IntVar()
        self.natural = tk.IntVar()
        self.torta = tk.IntVar()
        self.carne= tk.IntVar()
        self.natural=tk.IntVar()
        
        #creamos el widget treeview que almacenara el pedido cargado en la mesa
        
        columns =("cant. ","descrip.","P. Unit.","Tot")
        self.pedido_carga = ttk.Treeview(self.pedido_seleccion,height=20,columns=columns,show="headings")
        self.pedido_carga.grid(row=0,column=0,sticky="news")
        #se estandariza el Treeview, asignando las columnas
        for col in columns:
            self.pedido_carga.heading(col,text=col)
            self.pedido_carga.column(col,width=100,anchor=tk.CENTER)
        
        #se inserta el scrollbar en formar vertical al treeview de forma que si el pedido es mas grande se pueda visualizar 
        self.barra_bajada=tk.Scrollbar(self.pedido_seleccion,orient=tk.VERTICAL,command=self.pedido_carga.yview)
        self.barra_bajada.grid(row=0,column=1,sticky="ns")
        self.pedido_carga.config(yscrollcommand=self.barra_bajada.set)
        #titulo de los menus
        self.title_menu=tk.Label(self.pedido_seleccion,text="Menú",bg="lightblue",fg="white",font=(18)).place(x=150,y=10)
        self.title_entrada=tk.Label(self.pedido_seleccion,text="Entrada",bg="lightblue",fg="white",font=(18)).place(x=350,y=45)
        self.title_principal=tk.Label(self.pedido_seleccion,text="plato principal",bg="lightblue",fg="white",font=(18)).place(x=425,y=45)
        self.title_bebida=tk.Label(self.pedido_seleccion,text="Bebida",bg="lightblue",fg="white",font=(18)).place(x=540,y=45)
        self.title_postre=tk.Label(self.pedido_seleccion,text="postre",bg="lightblue",fg="white",font=(18)).place(x=620,y=45)
        
        
        #botones
        self.sopa_dia=tk.Checkbutton(self.pedido_seleccion,text="sopa del dia", variable=self.sopa,onvalue=1,offvalue=0)
        self.sopa_dia.place(x=420,y=70)
        self.ensalada_dia=tk.Checkbutton(self.pedido_seleccion,text="ensalada rica", variable=self.ensalada,onvalue=1,offvalue=0)
        self.ensalada_dia.place(x=520,y=70)
        self.plato1=tk.Checkbutton(self.pedido_seleccion,text="cerdo", variable=self.cerdo,onvalue=1,offvalue=0)
        self.plato1.place(x=620,y=70)
        self.plato2=tk.Checkbutton(self.pedido_seleccion,text="pollito", variable=self.pollo,onvalue=1,offvalue=0)
        self.plato2.place(x=720,y=70)
        self.plato3=tk.Checkbutton(self.pedido_seleccion,text="carne", variable=self.carne,onvalue=1,offvalue=0)
        self.plato3.place(x=820,y=70)
        self.plato4=tk.Checkbutton(self.pedido_seleccion,text="prezcado frito", variable=self.pez,onvalue=1,offvalue=0)
        self.plato4.place(x=920,y=70)
        self.bebida1=tk.Checkbutton(self.pedido_seleccion,text="cocacola", variable=self.refresh,onvalue=1,offvalue=0)
        self.bebida1.place(x=670,y=140)
        self.bebida2=tk.Checkbutton(self.pedido_seleccion,text="jugo natural", variable=self.natural,onvalue=1,offvalue=0)
        self.bebida2.place(x=560,y=140)
        self.postre=tk.Checkbutton(self.pedido_seleccion,text="torta de chocolate", variable=self.torta,onvalue=1,offvalue=0)
        self.postre.place(x=420,y=140)
        
        #creamos el combobox
        self.cantidad_sopa = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_sopa.place(x=420,y=100)
        self.cantidad_ensalada = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_ensalada.place(x=520,y=100)
        self.cantidad_plato1 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_plato1.place(x=620,y=100)
        self.cantidad_plato2 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_plato2.place(x=720,y=100)
        self.cantidad_plato3 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_plato3.place(x=820,y=100)
        self.cantidad_plato4 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_plato4.place(x=920,y=100)
        self.cantidad_bebida1 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_bebida1.place(x=670,y=180)
        self.cantidad_bebida2 = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_bebida2.place(x=560,y=180)
        self.cantidad_postre = ttk.Combobox(self.pedido_seleccion,values=[1,2,3,4,5,6,7,8,9,10],width=10,height=10)
        self.cantidad_postre.place(x=420,y=180)
        
        #mostrar en treeview lso platos cargados previaente para la mesa seleccionada
        
        recepcion_platos =self.conectar.cargar_plato_treeview(numero_mesa)
        #limpiamos el treeview
        for i in self.pedido_carga.get_children():
            self.pedido_carga.delete(i)
            
        for i in recepcion_platos:
            self.pedido_carga.insert("","end",value=i)
        
        
        self.cargar=tk.Button(self.pedido_seleccion,text="cargar pedido",bg="orange",width=15,height=5,command=lambda:self.cargar_pedido(numero_mesa))
        self.cargar.place(x=300,y=500)
        self.pagar=tk.Button(self.pedido_seleccion,text="pagar",bg="green",width=15,height=5,command=self.pago)
        self.pagar.place(x=450,y=500)
        self.eliminar=tk.Button(self.pedido_seleccion,text="eliminar pedido",bg="red",width=15,height=5)
        self.eliminar.place(x=575,y=500)
        
    
    def cargar_pedido(self,numero_mesa):
        bandera_seleccionado = 0
        bandera_cantidad = 0
        enviar=[]
        cantidad=[]
        recepcion="esta vacia"
        
        datos =(self.sopa.get(),self.ensalada.get(),self.cerdo.get(),self.pollo.get(),self.carne.get(),
                self.pez.get(),self.refresh.get(),self.natural.get(),self.torta.get())
        
        cantidades=(self.cantidad_sopa.get(),self.cantidad_ensalada.get(),self.cantidad_plato1.get(),
                    self.cantidad_plato2.get(),self.cantidad_plato3.get(),self.cantidad_plato4.get(),
                    self.cantidad_bebida1.get(),self.cantidad_bebida2.get(),self.cantidad_postre.get(),)
        
        for i in datos:
            for j in cantidades:
                
                if i == self.sopa.get() and (self.sopa.get()) and j == self.cantidad_sopa.get() and (self.cantidad_sopa.get()):
                    enviar.append(1) 
                    self.sopa.set(0) 
                    cantidad.append(self.cantidad_sopa.get()) 
                    self.cantidad_sopa.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.sopa.get()) and not (self.cantidad_sopa.get()) or not (self.sopa.get()) and (self.cantidad_sopa.get()): 
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                
                elif i == self.ensalada.get() and (self.ensalada.get()) and j == self.cantidad_ensalada.get() and (self.cantidad_ensalada.get()): 
                    enviar.append(2) 
                    self.ensalada.set(0) 
                    cantidad.append(self.cantidad_ensalada.get()) 
                    self.cantidad_ensalada.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.ensalada.get()) and not (self.cantidad_ensalada.get()) or not (self.ensalada.get()) and (self.cantidad_ensalada.get()):
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                
                elif i == self.carne.get() and (self.carne.get()) and j == self.cantidad_plato1.get() and (self.cantidad_plato1.get()): 
                    enviar.append(3) 
                    self.carne.set(0) 
                    cantidad.append(self.cantidad_plato1.get()) 
                    self.cantidad_plato1.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.carne.get()) and not (self.cantidad_plato1.get()) or not (self.carne.get()) and (self.cantidad_plato1.get()): 
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                    
                elif i == self.pollo.get() and (self.pollo.get()) and j == self.cantidad_plato2.get() and (self.cantidad_plato2.get()):
                    enviar.append(4) 
                    self.pollo.set(0) 
                    cantidad.append(self.cantidad_plato2.get()) 
                    self.cantidad_plato2.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.pollo.get()) and not (self.cantidad_plato2.get()) or not (self.pollo.get()) and (self.cantidad_plato2.get()): 
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                    
                elif i == self.cerdo.get() and (self.cerdo.get()) and j == self.cantidad_plato3.get() and (self.cantidad_plato3.get()):
                    enviar.append(5) 
                    self.cerdo.set(0) 
                    cantidad.append(self.cantidad_plato3.get()) 
                    self.cantidad_plato3.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.cerdo.get()) and not (self.cantidad_plato3.get()) or not (self.cerdo.get()) and (self.cantidad_plato3.get()): 
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                    
                elif i == self.pez.get() and (self.pez.get()) and j == self.cantidad_plato4.get() and (self.cantidad_plato4.get()):
                    enviar.append(6) 
                    self.pez.set(0) 
                    cantidad.append(self.cantidad_plato4.get()) 
                    self.cantidad_plato4.set('')
                    bandera_seleccionado = 1 
                    
                elif (self.pez.get()) and not (self.cantidad_plato4.get()) or not (self.pez.get()) and (self.cantidad_plato4.get()):
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                    
                elif i == self.refresh.get() and (self.refresh.get()) and j == self.cantidad_bebida1.get() and (self.cantidad_bebida1.get()):
                    enviar.append(7) 
                    self.refresh.set(0) 
                    cantidad.append(self.cantidad_bebida1.get()) 
                    self.cantidad_bebida1.set('') 
                    bandera_seleccionado = 1 
                    
                elif (self.refresh.get()) and not (self.cantidad_bebida1.get()) or not (self.refresh.get()) and (self.cantidad_bebida1.get()):
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                elif i == self.natural.get() and (self.natural.get()) and j == self.cantidad_bebida2.get() and (self.cantidad_bebida2.get()):
                    enviar.append(8) 
                    self.natural.set(0) 
                    cantidad.append(self.cantidad_bebida2.get()) 
                    self.cantidad_bebida2.set('') 
                    bandera_seleccionado = 1 
                elif (self.natural.get()) and not (self.cantidad_bebida2.get()) or not (self.natural.get()) and (self.cantidad_bebida2.get()):
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                elif i == self.torta.get() and (self.torta.get()) and j == self.cantidad_postre.get() and (self.cantidad_postre.get()):
                    enviar.append(9) 
                    self.torta.set(0) 
                    cantidad.append(self.cantidad_postre.get()) 
                    self.cantidad_postre.set('')
                    bandera_seleccionado = 1 
                elif (self.torta.get()) and not (self.cantidad_postre.get()) or not (self.torta.get()) and (self.cantidad_postre.get()):
                    bandera_cantidad = 1 
                    bandera_seleccionado = 1 
                
        if bandera_seleccionado == 0: 
           mb.showinfo("Información", "Debe Seleccionar algún Plato") 
                
        elif bandera_cantidad == 1: 
           mb.showerror("Error", "Ingrese todas las Cantidades") 
                
        else: 
          cargar_datos = (enviar, cantidad) 
          recepcion = self.conectar.cargar(cargar_datos, numero_mesa) 
          
          for i in self.pedido_carga.get_children(): 
            self.pedido_carga.delete(i) 
          for i in recepcion:
            self.pedido_carga.insert('', 'end', value = i) 
          
        bandera_cantidad = 0 
          
        bandera_seleccionado = 0
                    
            
    def pago(self):
        self.n1=tk.StringVar()
        self.n2=tk.StringVar()
        
        self.ventana_pago=tk.Toplevel(self.master,width=800,height=700,bg="lightblue")
        self.ventana_pago.title("pago")
        
        self.pagar.config(state="disabled")
        
        
        self.detalle = tk.Text(self.ventana_pago, bg="orange",width=20,height=20)
        self.detalle.place(x=90,y=50)
        
        self.factura = tk.Label(self.ventana_pago,text="desarrollo de factura",bg="lightblue",fg="white")
        self.factura.place(x=90,y=20)
        self.cliente = tk.Label(self.ventana_pago,text="Razón social:",bg="lightblue",fg="white")
        self.cliente.place(x=350,y=50)
        self.documento = tk.Label(self.ventana_pago,text="C.I / RIF: ",bg="lightblue",fg="white")
        self.documento.place(x=350,y=90)
        self.forma_pago = tk.Label(self.ventana_pago,text="Formas de pago",bg="lightblue",fg="white")
        self.forma_pago.place(x=400,y=450)
        
        
        self.entrada1=tk.Entry(self.ventana_pago,textvariable=self.n1)
        self.entrada1.place(x=460,y=50)
        self.entrada2=tk.Entry(self.ventana_pago,textvariable=self.n2)
        self.entrada2.place(x=460,y=80)
        
        self.efectivo=tk.Button(self.ventana_pago,text="pago en efectivo",bg="green",width=15,height=5)
        self.efectivo.place(x=250,y=500)
        self.electronico=tk.Button(self.ventana_pago,text="pago electronico",bg="green",width=15,height=5)
        self.electronico.place(x=400,y=500)
        self.imprimir=tk.Button(self.ventana_pago,text="imprimir",bg="orange",width=15,height=5)
        self.imprimir.place(x=550,y=500)
        
        
#creamos la ventana principal con sus caracteristicas

app = App
ventana =tk.Tk()
ventana.geometry("1200x600")
ventana.wm_title("Sistema Restaurant")
ventana.config(bg="lightblue", relief="sunken", bd=30,cursor="hand2")
app(master=ventana)
ventana.mainloop()

        