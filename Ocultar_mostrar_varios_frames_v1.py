from tkinter import *  # carga pquete tkinter

root = Tk()  # se crea la instanacia de la ventana
root.geometry("400x150")

# Frame A
# frm_A = Frame(root)
# frm_A.pack()

boton_prueba = Button(root, text="Boton de Prueba")
boton_prueba.pack()


# boton para accion
btn=Button(root, text="Click ocultar")
btn.pack()

# Ocultar
def hide_widget(e):
   boton_prueba.pack_forget()

# Mostrar
def show_widget(e):
   boton_prueba.pack()


# # eventos
btn.bind('<Button-1>', hide_widget)




root.mainloop()