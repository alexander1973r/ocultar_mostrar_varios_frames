from tkinter import *
import sys

root = Tk()  # se crea la instanacia de la ventana
root.geometry("300x300")

# frame ACERCA
acerca = Frame(root)
acerca.pack()
label_a = Label(acerca, text= "ACERCA", font= ('Helvetica bold', 14))
label_a.pack()

# frame productos
productos = Frame(root)
label_b = Label(productos, text= "Productos", font= ('Helvetica bold', 14))
label_b.pack()
btn_b = Button(productos, text= "Ver Productos", font= ('Helvetica bold', 14))
btn_b.pack()

# frame Servicios
servicios = Frame(root)
label_b = Label(servicios, text= "Servicios", font= ('Helvetica bold', 14))
label_b.pack()

# funcion para mostrar
def mostrar_frame(arg):
    # ocultar todos los frames
    acerca.pack_forget()
    productos.pack_forget()
    servicios.pack_forget()

    # convertir str a clase
    def str_to_class(arg):
        return getattr(sys.modules[__name__], arg)

    # muestra el frame seleccionado
    str_to_class(arg).pack()


# create a toplevel menu
menubar = Menu(root)
root.config(menu=menubar)  # display the menu
menubar.add_command(label="Acerca",    command=lambda arg="acerca": mostrar_frame(arg))
menubar.add_command(label="Productos", command=lambda arg="productos": mostrar_frame(arg))
menubar.add_command(label="Servicios", command=lambda arg="servicios": mostrar_frame(arg))
menubar.add_command(label="Salir", command=root.quit)

root.mainloop()