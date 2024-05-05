from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/adminDashboard")

# Combinamos la ruta actual con la parte relativa para obtener la ruta absoluta
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH

def relative_to_assets(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return ASSETS_PATH / Path(path)

window = Tk()

#Definimos dimensiones, nombre de la ventana, favicon y background-color
window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 639,
    width = 1137,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    112.0,
    47.0,
    image=image_image_1
)

canvas.create_text(
    82.0,
    110.0,
    anchor="nw",
    text="Menu",
    fill="#347AE2",
    font=("Poppins Medium", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    122.0,
    image=image_image_2
)

canvas.create_text(
    82.0,
    196.0,
    anchor="nw",
    text="Editar Productos",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    63.0,
    207.0,
    image=image_image_3
)

canvas.create_text(
    80.0,
    153.0,
    anchor="nw",
    text="Añadir Productos",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    59.0,
    165.0,
    image=image_image_4
)

canvas.create_text(
    82.0,
    239.0,
    anchor="nw",
    text="Eliminar Productos",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    64.0,
    251.0,
    image=image_image_5
)

canvas.create_text(
    82.5,
    282.0,
    anchor="nw",
    text="Listar Productos",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    64.0,
    293.0,
    image=image_image_6
)

canvas.create_text(
    82.0,
    325.0,
    anchor="nw",
    text="Listar Ventas",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    64.0,
    337.0,
    image=image_image_7
)

canvas.create_rectangle(
    246.0,
    110.0,
    247.00002146229144,
    602.0,
    fill="#E6EDFF",
    outline="")

canvas.create_text(
    82.00146484375,
    578.0,
    anchor="nw",
    text="Cerrar Sesión",
    fill="#FF3B30",
    font=("Poppins Medium", 16 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    62.0,
    590.0,
    image=image_image_8
)

canvas.create_rectangle(
    302.0,
    189.0,
    498.0,
    328.0,
    fill="#FFADAD",
    outline="")

canvas.create_rectangle(
    531.0,
    189.0,
    727.0,
    328.0,
    fill="#9EC7FF",
    outline="")

canvas.create_rectangle(
    759.0,
    189.0,
    955.0,
    328.0,
    fill="#96FFAD",
    outline="")

canvas.create_text(
    294.0,
    101.0,
    anchor="nw",
    text="Bienvenido de vuelta, George",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    147.0,
    anchor="nw",
    text="Conoce las estadísticas generales de tu empresa",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    314.0,
    201.0,
    anchor="nw",
    text="Productos Totales",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    314.0,
    245.0,
    anchor="nw",
    text="24",
    fill="#161E54",
    font=("Poppins Medium", 36 * -1)
)

canvas.create_text(
    314.0,
    289.0,
    anchor="nw",
    text="Productos añadidos",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

canvas.create_text(
    549.0,
    201.0,
    anchor="nw",
    text="Ingresos Totales",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    549.0,
    245.0,
    anchor="nw",
    text="200.000",
    fill="#161E54",
    font=("Poppins Medium", 36 * -1)
)

canvas.create_text(
    549.0,
    289.0,
    anchor="nw",
    text="Pesos colombianos",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

canvas.create_text(
    771.0,
    201.0,
    anchor="nw",
    text="Usuarios Activos",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    771.0,
    245.0,
    anchor="nw",
    text="24",
    fill="#161E54",
    font=("Poppins Medium", 36 * -1)
)

canvas.create_text(
    771.0,
    289.0,
    anchor="nw",
    text="Usuarios",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=302.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=432.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=562.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=302.0,
    y=455.0,
    width=108.0,
    height=97.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=432.0,
    y=455.0,
    width=108.0,
    height=97.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=562.0,
    y=455.0,
    width=108.0,
    height=97.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    886.0,
    534.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1062.0,
    131.0,
    image=image_image_10
)
window.resizable(False, False)

window.mainloop()