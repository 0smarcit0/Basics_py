import tkinter as tk 
from tkinter import messagebox as MB

class App(tk.Frame):
    def __init__(self,master =None):
        super().__init__(master)
        self.master = master
        self.marcos()
        self.labels()
        self.entry()
        self.botones()
        self.hola()
        self.menu = tk.Menu(self.master)
        self.master.config(menu =self.menu)
        self.menuarchivo=tk.Menu(self.menu,tearoff=0)
        self.menueditar=tk.Menu(self.menu,tearoff=0)
        self.menuayuda=tk.Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="archivo",menu=self.menuarchivo)
        self.menu.add_cascade(label="editar",menu=self.menueditar)
        self.menu.add_cascade(label="ayuda",menu=self.menuayuda)
        self.menuarchivo.add_command(label="nuevo")
        self.menuarchivo.add_command(label="abrir")
        self.menuarchivo.add_command(label="guardar")
        self.menuarchivo.add_command(label="cerrar")
        self.menuarchivo.add_separator()
        self.menuarchivo.add_command(label="salir",command=self.master.quit)
        self.pack()
        
        
        
        
        
    def marcos(self):
        self.marco =tk.Frame(ventana)
        self.marco.pack()
        self.marco.config(width=400, height=400)
        self.marco.config(bg="red")
        self.marco.config(cursor="")
        self.marco.config(relief="sunken")
        self.marco.config(bd=20)
        self.marco.pack(fill="x")
        self.marco.pack(fill="y")
        self.marco.pack(fill="both")
        self.marco.pack(fill="both",expand=1)
            
        self.marcoinf = tk.Frame(self.marco)
        self.marcoinf.pack(fill="x")
        self.marcoinf.pack(fill="y")
        self.marcoinf.pack(fill="both")
        self.marcoinf.pack(fill="both",expand=1)
        self.marcoinf.config(width=200,height=200)
        self.marcoinf.config(bg="green")
        self.marcoinf.config(relief="solid")
        
    
    def labels(self):
    
      tk.Label(self.marcoinf,text="primer numero",fg="white",bg="green",font=("Georgia",14),).place(x = 20, y =60)
      tk.Label(self.marcoinf,text="segundo numero",fg="white",bg="green",font=("Georgia",14),).place(x = 20, y =90)
      tk.Label(self.marcoinf,text="resulado",fg="white",bg="green",font=("Georgia",14),).place(x = 20, y=120)
      self.mostrar=tk.Label
      self.mostrar(self.marcoinf).place(x=50,y=250)
      self.check=tk.Label(self.marcoinf,text="que quiere merendar").place(x=50,y=330)
      self.check2=tk.Label(self.marcoinf)
      self.check2.place(x=50, y=360)
      
      
      #texto:
      #tk.Text(self.marcoinf,bg="orange",width=100,height=200).place(x= 100, y= 150)
    
    def entry(self):
        self.n1 = tk.StringVar()
        self.n2 = tk.StringVar()
        self.resultado = tk.StringVar()
        self.opcion = tk.IntVar()
        self.pastel = tk.IntVar()
        self.dona =tk.IntVar()
        
        
        tk.Entry(self.marcoinf,textvariable=self.n1).place (x=170, y = 70)
        tk.Entry(self.marcoinf,textvariable=self.n2).place (x= 170, y = 100)
        tk.Entry(self.marcoinf,textvariable=self.resultado,state="disabled").place (x= 170, y = 130)
    
    def botones(self):
        tk.Button(self.marcoinf, text="sumar",command=self.sumar).place(x=50,y=200)
        tk.Button(self.marcoinf, text="restar",command=self.resta).place(x=100,y=200)
        tk.Button(self.marcoinf, text="multiplicar",command=self.multi).place(x=150,y=200)
        tk.Button(self.marcoinf, text="dividir",command=self.dividir).place(x=225,y=200)
        tk.Button(self.marcoinf,text="salida",fg="red",command=self.master.destroy).place(x=350,y=200)
        
        #tk.Radiobutton(self.marcoinf,text="op1",variable=self.opcion,value=1,command=self.seleccion).place(x=50,y=250)
        #tk.Radiobutton(self.marcoinf,text="op2",variable=self.opcion,value=2,command=self.seleccion).place(x=50,y=280)
       #tk.Radiobutton(self.marcoinf,text="op3",variable=self.opcion,value=3,command=self.seleccion).place(x=50,y=310)
       
       
        self.selec=tk.Checkbutton(self.marcoinf,text="pastel", variable=self.pastel,onvalue=1,offvalue=0,command=self.seleccheck)
        self.selec.place(x=200,y=250)
        self.selec2=tk.Checkbutton(self.marcoinf,text="dona", variable=self.dona,onvalue=1,offvalue=0,command=self.seleccheck)
        self.selec2.place(x=200,y=280)
        
        self.botonprueba =tk.Button(self.marcoinf,text="prueba",command=self.prueba).place(x=260,y=260)
        self.boton2 = tk.Button(self.marcoinf,text="acceso a nueva ventana",command=self.nuevoacceso).place(x=300,y=280)
        
        
    
    def hola(self):
        print("hola")
    
    def borrar(self):
        self.n1.set("")
        self.n2.set("")
    
    def sumar(self):
        self.resultado.set(float(self.n1.get()) + float(self.n2.get())) 
        self.borrar()
    
    def resta(self):
        self.resultado.set(float(self.n1.get()) - float(self.n2.get())) 
        self.borrar()
    
    def multi(self):
        self.resultado.set(float(self.n1.get()) * float(self.n2.get())) 
        self.borrar()
    
    def dividir(self):
        self.resultado.set(float(self.n1.get()) / float(self.n2.get())) 
        self.borrar()
    
    def seleccion(self):
        self.mostrar.config(text= "opcion ".format(self.opcion.get()))
    
    
    def seleccheck(self):
        self.cadena=""
        
        if self.pastel and self.dona:
            self.cadena=""
        
        if(self.pastel.get()):self.cadena+="pastel"
        else:
            self.cadena +="no quiero"
        if(self.dona.get()):self.cadena+="dona"
        
        else:
            self.cadena +="no quiero nada"
        
        self.check2.config(text=self.cadena)
            
        
    def prueba(self):
        MB.showinfo("popout de test", "esta es una prueba")
    
    def nuevoacceso(self):
        self.nuevaventana=tk.Toplevel(self.master)
        self.nuevolabel=tk.Label(self.nuevaventana,text="new")
        self.texto =tk.Text(self.nuevaventana,bg="blue",width=200,height=200)
        self.newboton=tk.Button(self.nuevaventana,text="new")
        self.nuevaventana.title("holanew")
        self.nuevolabel.pack()
        self.texto.pack()
        self.newboton.pack()
        







ventana = tk.Tk()
ventana.wm_title("papu")
ventana.wm_geometry("500x500")
ventana.config(bg="light blue")
ventana.config(cursor="pirate")
ventana.config(relief="sunken",bd=25)

app = App(master=ventana)
ventana.mainloop()


