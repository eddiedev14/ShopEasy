import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/addProducts")

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
    368.0,
    anchor="nw",
    text="Configuración",
    fill="#7C8DB5",
    font=("Poppins Medium", 16 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    64.0,
    379.49700927734375,
    image=image_image_8
)

canvas.create_text(
    82.00146484375,
    578.0,
    anchor="nw",
    text="Cerrar Sesión",
    fill="#FF3B30",
    font=("Poppins Medium", 16 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    62.0,
    590.0,
    image=image_image_9
)

canvas.create_text(
    294.0,
    101.0,
    anchor="nw",
    text="Añadir Productos",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    147.0,
    anchor="nw",
    text="Controla y sigue de la mejor manera tu inventario de productos",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1062.0,
    131.0,
    image=image_image_10
)

canvas.create_text(
    294.0,
    191.0,
    anchor="nw",
    text="Código del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    293.0,
    anchor="nw",
    text="Categoría del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    395.0,
    anchor="nw",
    text="Stock",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    191.0,
    anchor="nw",
    text="Nombre del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    293.0,
    anchor="nw",
    text="Descripción del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    395.0,
    anchor="nw",
    text="Precio Unitario",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    485.0,
    250.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=303.0,
    y=228.0,
    width=364.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    485.0,
    352.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=303.0,
    y=330.0,
    width=364.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    485.0,
    454.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=303.0,
    y=432.0,
    width=364.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    894.0,
    250.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=712.0,
    y=228.0,
    width=364.0,
    height=43.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    894.0,
    352.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=712.0,
    y=330.0,
    width=364.0,
    height=43.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    894.0,
    454.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=712.0,
    y=432.0,
    width=364.0,
    height=43.0
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
    x=703.0,
    y=511.0,
    width=382.0,
    height=54.0
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
    x=294.0,
    y=511.0,
    width=382.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
