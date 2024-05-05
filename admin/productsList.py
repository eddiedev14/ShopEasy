import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/productsList")

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
    247.00002146229235,
    602.0,
    fill="#E6EDFF",
    outline="")

canvas.create_text(
    82.001953125,
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
    82.001953125,
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
    296.0,
    79.0,
    anchor="nw",
    text="Listado de Productos",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    296.0,
    124.0,
    anchor="nw",
    text="Controla y sigue de la mejor manera tu inventario de productos",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    296.0,
    124.0,
    anchor="nw",
    text="Controla y sigue de la mejor manera tu inventario de productos",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1064.0,
    104.0,
    image=image_image_10
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
    x=296.0,
    y=161.0,
    width=287.0,
    height=49.0
)

canvas.create_rectangle(
    296.0,
    274.0,
    1087.0,
    330.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    296.0,
    341.0,
    1087.0,
    397.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    296.0,
    408.0,
    1087.0,
    464.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    296.0,
    477.0,
    1087.0,
    533.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    296.0,
    544.0,
    1087.0,
    600.0,
    fill="#F5F5F5",
    outline="")

canvas.create_text(
    895.0,
    232.0,
    anchor="nw",
    text="Stock",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    973.0,
    232.0,
    anchor="nw",
    text="Precio Unidad",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    690.0,
    232.0,
    anchor="nw",
    text="Descripción",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    542.0,
    232.0,
    anchor="nw",
    text="Categoría",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    388.0,
    232.0,
    anchor="nw",
    text="Nombre",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    296.0,
    231.0,
    anchor="nw",
    text="Código",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    319.0,
    290.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    319.0,
    357.0,
    anchor="nw",
    text="2",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    319.0,
    424.0,
    anchor="nw",
    text="3",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    321.0,
    491.0,
    anchor="nw",
    text="4",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    319.0,
    562.0,
    anchor="nw",
    text="5",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    390.0,
    292.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    390.0,
    359.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    390.0,
    426.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    390.0,
    493.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    390.0,
    562.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    542.0,
    291.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    542.0,
    358.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    542.0,
    425.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    542.0,
    492.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    542.0,
    561.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    690.0,
    291.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    690.0,
    358.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    690.0,
    425.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    690.0,
    492.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    690.0,
    561.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 16 * -1)
)

canvas.create_text(
    895.0,
    291.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    895.0,
    358.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    895.0,
    425.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    895.0,
    492.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    895.0,
    561.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    1003.0,
    291.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    1003.0,
    358.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    1003.0,
    425.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    1003.0,
    492.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    1003.0,
    561.0,
    anchor="nw",
    text="Lorem",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
