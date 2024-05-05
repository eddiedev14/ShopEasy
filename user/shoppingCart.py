import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/shoppingCart")

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
    120.0,
    anchor="nw",
    text="¡Finaliza los últimos detalles para completar tu compra en ShopEasy!",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    354.0,
    219.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    354.0,
    344.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    354.0,
    469.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    354.0,
    594.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    605.0,
    218.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    605.0,
    343.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    605.0,
    468.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    605.0,
    593.0,
    image=image_image_9
)

canvas.create_text(
    499.0,
    211.0,
    anchor="nw",
    text="$681",
    fill="#393939",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    499.0,
    336.0,
    anchor="nw",
    text="$681",
    fill="#393939",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    499.0,
    461.0,
    anchor="nw",
    text="$681",
    fill="#393939",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    499.0,
    586.0,
    anchor="nw",
    text="$681",
    fill="#393939",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    432.0,
    211.0,
    anchor="nw",
    text="1",
    fill="#393939",
    font=("Poppins SemiBold", 22 * -1)
)

canvas.create_text(
    432.0,
    336.0,
    anchor="nw",
    text="1",
    fill="#393939",
    font=("Poppins SemiBold", 22 * -1)
)

canvas.create_text(
    432.0,
    461.0,
    anchor="nw",
    text="1",
    fill="#393939",
    font=("Poppins SemiBold", 22 * -1)
)

canvas.create_text(
    432.0,
    586.0,
    anchor="nw",
    text="1",
    fill="#393939",
    font=("Poppins SemiBold", 22 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    100.0,
    219.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    100.0,
    344.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    100.0,
    469.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    100.0,
    594.0,
    image=image_image_13
)

canvas.create_text(
    154.0,
    194.0,
    anchor="nw",
    text="Italy Pizza",
    fill="#1E1E1E",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    154.0,
    319.0,
    anchor="nw",
    text="Italy Pizza",
    fill="#1E1E1E",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    154.0,
    444.0,
    anchor="nw",
    text="Italy Pizza",
    fill="#1E1E1E",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    154.0,
    569.0,
    anchor="nw",
    text="Italy Pizza",
    fill="#1E1E1E",
    font=("Poppins Medium", 18 * -1)
)

canvas.create_text(
    154.0,
    224.0,
    anchor="nw",
    text="Extra cheese and toping",
    fill="#1E1E1E",
    font=("Nunito Medium", 14 * -1)
)

canvas.create_text(
    154.0,
    349.0,
    anchor="nw",
    text="Extra cheese and toping",
    fill="#1E1E1E",
    font=("Nunito Medium", 14 * -1)
)

canvas.create_text(
    154.0,
    474.0,
    anchor="nw",
    text="Extra cheese and toping",
    fill="#1E1E1E",
    font=("Nunito Medium", 14 * -1)
)

canvas.create_text(
    154.0,
    599.0,
    anchor="nw",
    text="Extra cheese and toping",
    fill="#1E1E1E",
    font=("Nunito Medium", 14 * -1)
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
    x=448.0,
    y=213.0,
    width=12.0,
    height=6.0
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
    x=448.0,
    y=338.0,
    width=12.0,
    height=6.0
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
    x=448.0,
    y=463.0,
    width=12.0,
    height=6.0
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
    x=448.0,
    y=588.0,
    width=12.0,
    height=6.0
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
    x=448.0,
    y=225.0,
    width=12.0,
    height=6.0
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
    x=448.0,
    y=350.0,
    width=12.0,
    height=6.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=448.0,
    y=475.0,
    width=12.0,
    height=6.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=448.0,
    y=600.0,
    width=12.0,
    height=6.0
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    899.0,
    325.0,
    image=image_image_14
)

canvas.create_text(
    732.0,
    195.0,
    anchor="nw",
    text="Resumen:",
    fill="#FFFFFF",
    font=("Poppins Bold", 28 * -1)
)

canvas.create_text(
    732.0,
    247.0,
    anchor="nw",
    text="Subtotal: $300.000",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

canvas.create_text(
    732.0,
    287.0,
    anchor="nw",
    text="IVA: $50.000",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

canvas.create_text(
    732.0,
    327.0,
    anchor="nw",
    text="Subtotal: $350.000",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=727.0,
    y=387.0,
    width=343.0,
    height=54.0
)

canvas.create_text(
    50.0,
    74.0,
    anchor="nw",
    text="Carrito de Compras",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1070.0,
    97.0,
    image=image_image_15
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=942.0,
    y=81.0,
    width=31.0,
    height=31.0
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
    x=994.0,
    y=81.0,
    width=31.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()
