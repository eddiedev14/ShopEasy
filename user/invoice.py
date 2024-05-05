import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/invoice")

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
    50.0,
    74.0,
    anchor="nw",
    text="Resumen de la Compra",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1070.0,
    97.0,
    image=image_image_2
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
    x=942.0,
    y=81.0,
    width=31.0,
    height=31.0
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
    x=994.0,
    y=81.0,
    width=31.0,
    height=31.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    368.0,
    170.0,
    image=image_image_3
)

canvas.create_text(
    69.0,
    145.0,
    anchor="nw",
    text="Usuario:",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    335.0,
    145.0,
    anchor="nw",
    text="Total a Pagar",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    521.0,
    145.0,
    anchor="nw",
    text="Fecha:",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    69.0,
    172.0,
    anchor="nw",
    text="Eddie Santiago Delgado",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    335.0,
    172.0,
    anchor="nw",
    text="$500.000 COP",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    521.0,
    172.0,
    anchor="nw",
    text="4/05/2024 13:00",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    134.0,
    232.0,
    anchor="nw",
    text="Producto",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    350.0,
    232.0,
    anchor="nw",
    text="Cantidad",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    454.0,
    232.0,
    anchor="nw",
    text="Precio Unidad",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    615.0,
    232.0,
    anchor="nw",
    text="Total",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_text(
    42.0,
    231.0,
    anchor="nw",
    text="Código",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

canvas.create_rectangle(
    40.0,
    264.0,
    695.0,
    320.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    42.0,
    327.0,
    697.0,
    383.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    42.0,
    390.0,
    697.0,
    446.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    42.0,
    453.0,
    697.0,
    509.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    42.0,
    516.0,
    697.0,
    572.0,
    fill="#F5F5F5",
    outline="")

canvas.create_text(
    64.0,
    282.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    66.0,
    345.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    66.0,
    408.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    66.0,
    471.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    66.0,
    534.0,
    anchor="nw",
    text="1",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    135.0,
    282.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    137.0,
    345.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    137.0,
    408.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    137.0,
    471.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    137.0,
    534.0,
    anchor="nw",
    text="Lorem Ipsum",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    375.0,
    282.0,
    anchor="nw",
    text="50",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    377.0,
    345.0,
    anchor="nw",
    text="50",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    377.0,
    408.0,
    anchor="nw",
    text="50",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    377.0,
    471.0,
    anchor="nw",
    text="50",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    377.0,
    534.0,
    anchor="nw",
    text="50",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    482.0,
    282.0,
    anchor="nw",
    text="$5.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    484.0,
    345.0,
    anchor="nw",
    text="$5.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    484.0,
    408.0,
    anchor="nw",
    text="$5.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    484.0,
    471.0,
    anchor="nw",
    text="$5.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    484.0,
    534.0,
    anchor="nw",
    text="$5.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    595.0,
    282.0,
    anchor="nw",
    text="$2.500.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    597.0,
    345.0,
    anchor="nw",
    text="$2.500.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    597.0,
    408.0,
    anchor="nw",
    text="$2.500.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    597.0,
    471.0,
    anchor="nw",
    text="$2.500.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
)

canvas.create_text(
    597.0,
    534.0,
    anchor="nw",
    text="$2.500.000",
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
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
    x=711.0,
    y=145.0,
    width=382.0,
    height=54.0
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
    x=711.0,
    y=211.0,
    width=382.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
