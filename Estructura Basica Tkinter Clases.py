from tkinter import *

class NOMBRE_CLASE(Tk):
    def __init__(self):
        #Heredamos de la clase Tk con super
        super().__init__()
        #Definimos los atributos de la ventana
        self.title("Titulo")
        self.geometry("400x650")
        
        #IntVar y StringVar aqui
        self.VARIABLE_STRING_VAR = StringVar()
        self.VARIABLE_INT_VAR = IntVar()
        
        #Opcional ajuste de celdas grid
        for i in range(9): #cantidad de filas ≡
            self.grid_rowconfigure(i, weight=1)
        for j in range(1): #cantidad de columnas ---
            self.grid_columnconfigure(j, weight=1)
        
        #Opcional creamos el frame
        self.FRAME = Frame(self, bg="gray", padx=20, pady=10)
        self.FRAME.grid(row=0, column=0)
               
        #Creamos los widgets
        self.LABEL = Label(self, text = "Texto", bg = "red")
        self.LABEL.grid(row=1, column=0)
        
        self.BOTON = Button(self, text="Saludar", command = self.SALUDAR)
        self.BOTON.grid(row=2, column=0)
        
        self.CHECKBUTTON = Checkbutton(self, text="Seleccionar", command = self.SELECCIONAR)
        self.CHECKBUTTON.grid(row=3, column=0)
        
        self.RADIOBUTTON1 = Radiobutton(self, text="Opción 1", variable=self.VARIABLE_INT_VAR, value=1, command=self.RADIOB_ACCION)
        self.RADIOBUTTON1.grid(row=4, column=0)
        self.RADIOBUTTON2 = Radiobutton(self, text="Opción 2", variable=self.VARIABLE_INT_VAR, value=2, command=self.RADIOB_ACCION)
        self.RADIOBUTTON2.grid(row=5, column=0)
        self.RADIOBUTTON3 = Radiobutton(self, text="Opción 3", variable=self.VARIABLE_INT_VAR, value=3, command=self.RADIOB_ACCION)
        self.RADIOBUTTON3.grid(row=6, column=0)
        
        self.ENTRY = Entry(self, width=40, bg="green")
        self.ENTRY.grid(row=7, column=0)
        
    def SALUDAR(self):
        print("hola")
     
    def SELECCIONAR(self):
        print("Se ha clickeado")
        
    def RADIOB_ACCION(self):
        opcion_elegida = self.VARIABLE_INT_VAR.get()
        print("Opción seleccionada:", opcion_elegida)
                
        
        
#Bucle que mantiene la interfaz abierta
if __name__ == "__main__":
    app = NOMBRE_CLASE()
    app.mainloop()        
        
        