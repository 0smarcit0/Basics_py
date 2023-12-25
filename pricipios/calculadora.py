import tkinter as tk
import ast

i =0
class Calculadora(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master =master
        self.widgets()
        
        self.grid()
        

        
        
        
        
    def widgets(self,):
        self.entrada=tk.Entry(self.master)
        self.entrada.grid(columnspan=6,row=0,sticky="nswe")
        
        #botones
        self.uno =tk.Button(self.master,width=10,height=5,text="1",command=lambda:self.insertar(1))
        self.uno.grid(column=0,row=1,sticky="nswe")
    
        self.dos =tk.Button(self.master,width=10,height=5,text="2",command=lambda:self.insertar(2))
        self.dos.grid(column=1,row=1,sticky="nswe")
        self.tres =tk.Button(self.master,width=10,height=5,text="3",command=lambda:self.insertar(3))
        self.tres.grid(column=2,row=1,sticky="nswe")
        
        self.cuatro =tk.Button(self.master,width=10,height=5,text="4",command=lambda:self.insertar(4))
        self.cuatro.grid(column=0,row=2,sticky="nswe")
        self.cinco =tk.Button(self.master,width=10,height=5,text="5",command=lambda:self.insertar(5))
        self.cinco.grid(column=1,row=2,sticky="nswe")
        self.seis =tk.Button(self.master,width=10,height=5,text="6",command=lambda:self.insertar(6))
        self.seis.grid(column=2,row=2,sticky="nswe")
        
        self.siete =tk.Button(self.master,width=10,height=5,text="7",command=lambda:self.insertar(7))
        self.siete.grid(column=0,row=3,sticky="nswe")
        self.ocho =tk.Button(self.master,width=10,height=5,text="8",command=lambda:self.insertar(8))
        self.ocho.grid(column=1,row=3,sticky="nswe")
        self.nueve =tk.Button(self.master,width=10,height=5,text="9",command=lambda:self.insertar(9))
        self.nueve.grid(column=2,row=3,sticky="nswe")
        
        self.cero =tk.Button(self.master,width=10,height=5,text="0",command=lambda:self.insertar(0))
        self.cero.grid(column=0,row=4,sticky="nswe")
        
        self.igual =tk.Button(self.master,width=10,height=5,text="=",command=self.calcular)
        self.igual.grid(column=1,row=4,sticky="nswe")
        
        self.punto =tk.Button(self.master,width=10,height=5,text=".",command=lambda:self.insertar_operador("."))
        self.punto.grid(column=2,row=4,sticky="nswe")
        
        self.suma =tk.Button(self.master,width=10,height=5,text="+",command=lambda:self.insertar_operador("+"))
        self.suma.grid(column=3,row=1,sticky="nswe")
        self.resta =tk.Button(self.master,width=10,height=5,text="-",command=lambda:self.insertar_operador("-"))
        self.resta.grid(column=3,row=2,sticky="nswe")
        self.multiplicacion =tk.Button(self.master,width=10,height=5,text="*",command=lambda:self.insertar_operador("*"))
        self.multiplicacion.grid(column=3,row=3,sticky="nswe")
        self.division =tk.Button(self.master,width=10,height=5,text="/",command=lambda:self.insertar_operador("/"))
        self.division.grid(column=3,row=4,sticky="nswe")
        
        
        self.elevar =tk.Button(self.master,width=10,height=5,text="**",command=lambda:self.insertar_operador("**"))
        self.elevar.grid(column=5,row=1,sticky="nswe")
        self.elevar2 =tk.Button(self.master,width=10,height=5,text="**2",command=lambda:self.insertar_operador("**2"))
        self.elevar2.grid(column=4,row=1,sticky="nswe")
        self.resto =tk.Button(self.master,width=10,height=5,text="%",command=lambda:self.insertar_operador("%"))
        self.resto.grid(column=4,row=2,sticky="nswe")
        self.borrar =tk.Button(self.master,width=10,height=5,text="DLT",command=self.undo)
        self.borrar.grid(column=4,row=3,sticky="nswe")
        self.borrartodo =tk.Button(self.master,width=10,height=5,text="DLTALL",command=self.clear)
        self.borrartodo.grid(column=4,row=4,sticky="nswe")
        self.parentesis1 =tk.Button(self.master,width=10,height=5,text="(",command=lambda:self.insertar_operador("("))
        self.parentesis1.grid(column=5,row=2,sticky="nswe")
        self.parentesis2 =tk.Button(self.master,width=10,height=5,text=")",command=lambda:self.insertar_operador(")"))
        self.parentesis2.grid(column=5,row=3,sticky="nswe")
    
    
    
    def undo(self):
        entrada_state=self.entrada.get()
        if len(entrada_state):
            entrada_new_state = entrada_state[:-1]
            self.clear()
            self.entrada.insert(0,entrada_new_state)
        else:
            self.clear()
            self.entrada.insert(0,"error")
            
            
    
    def clear(self):
        self.entrada.delete(0,"end")
             
    def insertar(self,n):
        global i
        
        self.entrada.insert(i,n)
        i=i+1
        
    def insertar_operador(self,operador):
        global i 
        op = len(operador)
        
        self.entrada.insert(i,operador)
        
        i+=op
    
    
    def calcular(self):
      entrada_state = self.entrada.get()
      try:
        parsed_expression = ast.parse(entrada_state, mode='eval')
        result = eval(compile(parsed_expression, '<string>', 'eval'))
        self.clear()
        self.entrada.insert(0, result)
     
      except Exception as e:
        self.entrada.insert(0, "error")  # Inserta el mensaje de error primero
        self.clear()  # Luego limpia el cuadro de entrada

        
    




app = Calculadora

ventana =tk.Tk()
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.columnconfigure(3,weight=1)
ventana.rowconfigure(3,weight=1)
ventana.columnconfigure(4,weight=1)
ventana.rowconfigure(4,weight=1)
#ventana.geometry("300x400")
ventana.wm_title("Calculadora")
app(master=ventana)
ventana.mainloop()  



"""root = tk.Frame()
root.grid() 

entrada=tk.Entry(root)
entrada.grid(row=0,columnspan=6,sticky="we")

uno =tk.Button(root,width=10,height=5,text="1")
uno.grid(column=0,row=1)
dos =tk.Button(root,width=10,height=5,text="2")
dos.grid(column=1,row=1)
tres =tk.Button(root,width=10,height=5,text="3")
tres.grid(column=2,row=1)


root.mainloop()"""