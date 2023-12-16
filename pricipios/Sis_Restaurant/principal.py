import tkinter as tk 
from tkinter import messagebox as mb


class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        
        self.master=master
        self.mobiliario()
        
        self.pack()
    
    
    def mobiliario(self):
        self.mesa1 = tk.Button(self.master,bg="orange",text="mesa1",fg="white",width=10,height=5,command=self.pedido).place(x=100,y=100)
        self.mesa2 = tk.Button(self.master,bg="orange",text="mesa2",fg="white",width=10,height=5).place(x=200,y=100)
        self.mesa3 = tk.Button(self.master,bg="orange",text="mesa3",fg="white",width=10,height=5).place(x=300,y=100)
        self.mesa4 = tk.Button(self.master,bg="orange",text="mesa4",fg="white",width=10,height=5).place(x=100,y=200)
        self.mesa5 = tk.Button(self.master,bg="orange",text="mesa5",fg="white",width=10,height=5).place(x=200,y=200)
        self.mesa6 = tk.Button(self.master,bg="orange",text="mesa6",fg="white",width=10,height=5).place(x=300,y=200)
        
        self.generar = tk.Button(self.master,bg="green",text="generar reporte de caja",fg="white",width=17,height=6).place(x=100,y=450)
        self.salir = tk.Button(self.master,bg="red",text="salir del programa",fg="white",width=15,height=6,command=self.master.destroy).place(x=250,y=450)
        self.caja = tk.Button(self.master,bg="grey",text="caja",fg="white",width=15,height=6,state="disabled").place(x=700,y=450)
        self.barra = tk.Button(self.master,bg="brown",fg="white",text="barra",width=8,height=30,state="disabled").place(x=700,y=0)
        self.cocina = tk.Button(self.master,bg="brown",fg="white",text="cocina",width=8,height=20,state="disabled").place(x=800,y=0)
        
        
    def pedido(self):
        self.pedido_seleccion =tk.Toplevel(self.master,bg="lightblue",width=800,height=600)
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
        
        #text de pedido
        
        self.pedido_txt=tk.Text(self.pedido_seleccion,bg="white",width=30,height=20).place(x=50,y=50)
        
        #titulo de los menus
        self.title_menu=tk.Label(self.pedido_seleccion,text="Menú",bg="lightblue",fg="white",font=(18)).place(x=150,y=10)
        self.title_entrada=tk.Label(self.pedido_seleccion,text="Entrada",bg="lightblue",fg="white",font=(18)).place(x=350,y=45)
        self.title_principal=tk.Label(self.pedido_seleccion,text="plato principal",bg="lightblue",fg="white",font=(18)).place(x=425,y=45)
        self.title_bebida=tk.Label(self.pedido_seleccion,text="Bebida",bg="lightblue",fg="white",font=(18)).place(x=540,y=45)
        self.title_postre=tk.Label(self.pedido_seleccion,text="postre",bg="lightblue",fg="white",font=(18)).place(x=620,y=45)
        
        
        #botones
        self.sopa_dia=tk.Checkbutton(self.pedido_seleccion,text="sopa del dia", variable=self.sopa,onvalue=1,offvalue=0)
        self.sopa_dia.place(x=325,y=70)
        self.ensalada_dia=tk.Checkbutton(self.pedido_seleccion,text="ensalada rica", variable=self.ensalada,onvalue=1,offvalue=0)
        self.ensalada_dia.place(x=325,y=100)
        self.plato1=tk.Checkbutton(self.pedido_seleccion,text="cerdo", variable=self.cerdo,onvalue=1,offvalue=0)
        self.plato1.place(x=430,y=70)
        self.plato2=tk.Checkbutton(self.pedido_seleccion,text="pollito", variable=self.pollo,onvalue=1,offvalue=0)
        self.plato2.place(x=430,y=100)
        self.plato3=tk.Checkbutton(self.pedido_seleccion,text="carne", variable=self.carne,onvalue=1,offvalue=0)
        self.plato3.place(x=430,y=130)
        self.plato4=tk.Checkbutton(self.pedido_seleccion,text="prezcado frito", variable=self.pez,onvalue=1,offvalue=0)
        self.plato4.place(x=430,y=160)
        self.bebida1=tk.Checkbutton(self.pedido_seleccion,text="cocacola", variable=self.refresh,onvalue=1,offvalue=0)
        self.bebida1.place(x=530,y=70)
        self.bebida2=tk.Checkbutton(self.pedido_seleccion,text="jugo natural", variable=self.natural,onvalue=1,offvalue=0)
        self.bebida2.place(x=530,y=100)
        self.postre=tk.Checkbutton(self.pedido_seleccion,text="torta de chocolate", variable=self.torta,onvalue=1,offvalue=0)
        self.postre.place(x=620,y=70)
        
        self.cargar=tk.Button(self.pedido_seleccion,text="cargar pedido",bg="orange",width=15,height=5).place(x=300,y=500)
        self.pagar=tk.Button(self.pedido_seleccion,text="pagar",bg="green",width=15,height=5).place(x=450,y=500)
        self.eliminar=tk.Button(self.pedido_seleccion,text="eliminar pedido",bg="red",width=15,height=5).place(x=575,y=500)
        
    








#creamos la ventana principal con sus caracteristicas

app = App
ventana =tk.Tk()
ventana.geometry("1200x600")
ventana.wm_title("Sistema Restaurant")
ventana.config(bg="lightblue", relief="sunken", bd=30,cursor="hand2")
app(master=ventana)
ventana.mainloop()

        