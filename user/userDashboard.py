import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
import sqlite3
from PIL import Image

cedula = sys.argv[1]

CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/userDashboard")
RELATIVE_PATH2 = Path("../images")

# Combinamos la ruta actual con la parte relativa para obtener la ruta absoluta
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
IMAGES_PATH = CURRENT_DIR / RELATIVE_PATH2

def relative_to_assets(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return ASSETS_PATH / Path(path)

def relative_to_images(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return IMAGES_PATH / Path(path)

#Obtenemos el nombre del usuario que acaba de ingresar
def getName(cedula):
    db = sqlite3.connect('shopeasy.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE cedula=? AND tipo=?", (cedula, "Usuario"))
    user = cursor.fetchone()
    #Retornamos el nombre del usuario que tenga esa cedula
    return user[1]

window = Tk()

#Definimos dimensiones, nombre de la ventana, favicon y background-color
window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")

db = sqlite3.connect('shopeasy.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM productos")
products = cursor.fetchmany(9)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 639,
    width = 1137,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.create_text(
    50.0,
    74.0,
    anchor="nw",
    text=f"Bienvenido de vuelta, {getName(cedula)}",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    50.0,
    120.0,
    anchor="nw",
    text="Visualiza nuestra oferta de productos y adquiérelos en instantes",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

canvas.place(x = 0, y = 0)

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
    x=942.0,
    y=81.0,
    width=31.0,
    height=31.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    112.0,
    47.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1070.0,
    97.0,
    image=image_image_2
)

#Verificamos que exista el elemento 1 y creamos su componente
try:
    product = products[0]

    image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"),
    )
    image_3 = canvas.create_image(
        209.0,
        216.0,
        image=image_image_3
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
        x=279.0,
        y=244.0,
        width=13.125,
        height=13.125
    )

    button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=314.0,
        y=244.0,
        width=13.125,
        height=13.125
    )

    button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_20 = Button(
        image=button_image_20,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_20 clicked"),
        relief="flat"
    )
    button_20.place(
        x=340.0,
        y=240.0,
        width=20.0,
        height=20.0
    )

    #Necesitamos redimensionar la imagen para que se vea bien para eso, usamos PIL
    imagen = Image.open(relative_to_images(product[6]))
    #Obtenemos ancho y alto de la imagen
    ancho, alto = imagen.size
    #Validamos si el ancho y alto es diferente a 96x96, para ese caso debemos redimensionar la imagen
    if ancho != 96 and alto != 96:
        #Le damos tamaño de 96px x 96px
        imagenRedimensionada = imagen.resize((96, 96))
        #Actualizamos la imagen
        imagenRedimensionada.save(f"images/{product[6]}")

    image_image_12 = PhotoImage(file=relative_to_images(product[6]))
    image_12 = canvas.create_image(
        104.0,
        216.0,
        image=image_image_12,
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = '{:,}'.format(product[5])
    precioFormateado = precioFormateado[:-2]

    canvas.create_text(
        164.0,
        174.0,
        anchor="nw",
        text=product[1],
        fill="#000000",
        font=("DMSans Medium", 13 * -1)
    )
    
    canvas.create_text(
        164.0,
        197.0,
        anchor="nw",
        text=product[3],
        fill="#979797",
        font=("Inter", 9 * -1)
    )
    
    canvas.create_text(
        164.0,
        237.0,
        anchor="nw",
        text=f"${precioFormateado} COP",
        fill="#3381DB",
        font=("Inter Bold", 12 * -1)
    )

#En caso de que no exista no lo creamos
except IndexError:
    pass



image_image_4 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_4 = canvas.create_image(
    209.0,
    354.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_5 = canvas.create_image(
    209.0,
    492.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_6 = canvas.create_image(
    567.0,
    216.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_7 = canvas.create_image(
    567.0,
    354.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_8 = canvas.create_image(
    567.0,
    492.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_9 = canvas.create_image(
    925.0,
    216.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_10 = canvas.create_image(
    925.0,
    354.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_11 = canvas.create_image(
    925.0,
    492.0,
    image=image_image_11
)



button_image_3 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=280.0,
    y=382.0,
    width=13.125,
    height=13.125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=279.9375,
    y=519.9375,
    width=13.125,
    height=13.125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=637.9375,
    y=243.9375,
    width=13.125,
    height=13.125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=637.9375,
    y=381.9375,
    width=13.125,
    height=13.125
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=637.9375,
    y=519.9375,
    width=13.125,
    height=13.125
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=996.0,
    y=242.0,
    width=13.125,
    height=13.125
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=996.0,
    y=378.0,
    width=13.125,
    height=13.125
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=996.0,
    y=518.0,
    width=13.125,
    height=13.125
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=313.9375,
    y=381.9375,
    width=13.125,
    height=13.125
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=313.9375,
    y=519.9375,
    width=13.125,
    height=13.125
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=671.9375,
    y=243.9375,
    width=13.125,
    height=13.125
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=671.9375,
    y=381.9375,
    width=13.125,
    height=13.125
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=671.9375,
    y=519.9375,
    width=13.125,
    height=13.125
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=1030.0,
    y=242.0,
    width=13.125,
    height=13.125
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=1030.0,
    y=378.0,
    width=13.125,
    height=13.125
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=1030.0,
    y=518.0,
    width=13.125,
    height=13.125
)


canvas.create_text(
    164.0,
    375.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    164.0,
    513.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    522.0,
    237.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    522.0,
    375.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    522.0,
    513.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    880.0,
    237.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    880.0,
    375.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    880.0,
    513.0,
    anchor="nw",
    text="$3.500.700 COP",
    fill="#3381DB",
    font=("Inter Bold", 12 * -1)
)

canvas.create_text(
    164.0,
    313.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    164.0,
    448.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    522.0,
    174.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    522.0,
    313.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    522.0,
    448.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    880.0,
    174.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    880.0,
    313.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)

canvas.create_text(
    880.0,
    448.0,
    anchor="nw",
    text="Laptop",
    fill="#000000",
    font=("DMSans Medium", 13 * -1)
)



canvas.create_text(
    164.0,
    335.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    164.0,
    473.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    522.0,
    197.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    522.0,
    335.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    522.0,
    473.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    880.0,
    197.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    880.0,
    335.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    880.0,
    473.0,
    anchor="nw",
    text="Intel Core I7 - Ram 16GB - 256 Gb SSD",
    fill="#979797",
    font=("Inter", 9 * -1)
)

canvas.create_text(
    298.0625,
    245.0625,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    299.0625,
    383.0625,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    299.0,
    521.0,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    657.0,
    245.0,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    657.0,
    383.0,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    657.0,
    521.0,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    1015.0625,
    243.0625,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    1015.0625,
    379.0625,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)

canvas.create_text(
    1015.0625,
    519.0625,
    anchor="nw",
    text="0",
    fill="#979797",
    font=("Inter Bold", 9 * -1)
)
"""


image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    104.0,
    354.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    104.0,
    492.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    462.0,
    216.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    462.0,
    354.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    462.0,
    492.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    820.0,
    216.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    820.0,
    354.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    820.0,
    492.0,
    image=image_image_20
)
"""

button_image_21 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=697.0,
    y=239.0,
    width=20.0,
    height=20.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=1052.0,
    y=239.0,
    width=20.0,
    height=20.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=1052.0,
    y=375.0,
    width=20.0,
    height=20.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=1052.0,
    y=514.0,
    width=20.0,
    height=20.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=697.0,
    y=378.0,
    width=20.0,
    height=20.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=697.0,
    y=517.0,
    width=20.0,
    height=20.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
button_27.place(
    x=340.0,
    y=377.0,
    width=20.0,
    height=20.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_28 clicked"),
    relief="flat"
)
button_28.place(
    x=340.0,
    y=517.0,
    width=20.0,
    height=20.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_29 clicked"),
    relief="flat"
)
button_29.place(
    x=994.0,
    y=81.0,
    width=31.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()
