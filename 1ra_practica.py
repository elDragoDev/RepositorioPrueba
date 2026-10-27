# codigo sin pep8
# importamos Tkinter
import tkinter as tk

# creamos nuestras variables para empezar a operar
ventana = tk.Tk()
ventana.title("My window")
ventana.geometry("600x600")

# nuestras variables para el contenido de la ventana de Tkinter
tag = tk.Label(ventana, text="habla Manuel dile a Yair hola", bg="blue")
tag_2 = tk.Label(ventana, text="fuerza Colombia", bg="yellow")
tag_3 = tk.Label(ventana, text="el mauro es el goat", bg="red")
tag.pack(side=tk.LEFT)
tag_2.pack(side=tk.BOTTOM)
tag_3.pack(fill="both", expand=True, side=tk.RIGHT)


def Mensaje():
    # esta es una subventana que debe despregarse al presionar un boton especifico
    sub_ventana2 = tk.Tk()
    sub_ventana2.title("tu goat")
    sub_ventana2.geometry("400x400")
    # estos tags son mensajes de la subventana
    tag_4 = tk.Label(sub_ventana2, text="Nada mal", bg="green")
    tag_4.pack()


def Mensaje2():
    # esta es otra subventana de Tkinter
    sub_ventana = tk.Toplevel()
    sub_ventana.title("el true goat messi")
    sub_ventana.geometry("400x400")

    # estas variables guardan texto que el ususario quiera al presionar "guardar"
    tag_monday = tk.Label(sub_ventana, text="Aquí aparecerá el texto")
    tag_monday.pack(pady=10)

    t = tk.Text(sub_ventana, width=30, height=4, font=("Times New Roman", 14))

    t.pack(pady=10)

    def TextodeCaja():
        # esta funcion es lo que permite obtener el texto a guardar
        text20 = t.get("1.0", "end-1c")
        tag_monday["text"] = text20

    # variables de botones de la subventana
    boton_2 = tk.Button(sub_ventana, text="subir", padx=40, pady=50, command=Mensaje)
    boton_2.pack()

    boton_3 = tk.Button(
        sub_ventana, text="guardar", padx=40, pady=50, command=TextodeCaja
    )
    boton_3.pack()


# variable de boton
boton_1 = tk.Button(ventana, text="pegame", padx=60, pady=40, command=Mensaje2)
boton_1.pack()


ventana.mainloop()
