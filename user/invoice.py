import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as mb
import sys
import ast
import subprocess
import json
from fpdf import FPDF

sale_str = sys.argv[1]
cart_str = sys.argv[2]
cedula = sys.argv[3]

# Convert the string to a list of dictionaries
sale = ast.literal_eval(sale_str)

# Obtener la ruta del directorio actual del script para abrir los demás archivos
script_dir = os.path.dirname(__file__)

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/invoice")

# Combinamos la ruta actual con la parte relativa para obtener la ruta absoluta
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH

def relative_to_assets(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return ASSETS_PATH / Path(path)

def openShoppingCart():
    # Construir la ruta al archivo invoice.py
    invoice_path = os.path.join(script_dir, "shoppingCart.py")
    #Se pasa como parametro la venta
    subprocess.Popen(['python', invoice_path, cart_str, cedula])
    sys.exit(0)

def createRectangle(x1, y1, x2, y2):
    canvas.create_rectangle(
    x1,
    y1,
    x2,
    y2,
    fill="#F5F5F5",
    outline="")

def createTableText(x, y, text):
    canvas.create_text(
    x,
    y,
    anchor="nw",
    text=text,
    fill="#535353",
    font=("RubikRoman Regular", 15 * -1)
    )

def generatePDF():
    #Trabajamos con POO para crear un objeto de la clase PDF con unos métodos definidos
    class PDF(FPDF):
        def header(self):
            # Logo
            self.image('assets/Logo.png', 10, 8, 33)
            # Título
            self.set_font('Arial', 'B', 24)
            self.cell(0, 10, 'Facturación', 0, 1, 'C')
            self.ln(10)

        def footer(self):
            # Número de página
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

    # Crear instancia de PDF
    pdf = PDF()
    pdf.add_page()

    # Agregar texto
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Usuario: {sale["Usuario"]}', 0, 1)
    pdf.cell(0, 10, f'Fecha: {sale["Fecha"]}', 0, 1)

    # Agregar tabla
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(35, 10, 'N°', 1)
    pdf.cell(35, 10, 'Nombre', 1)
    pdf.cell(35, 10, 'Cantidad', 1)
    pdf.cell(35, 10, 'Precio Unidad', 1)
    pdf.cell(35, 10, 'Subtotal', 1)
    pdf.ln()

    # Agregar filas a la tabla
    pdf.set_font('Arial', '', 12)

    acumulator = 0

    for row in sale["Productos"]:
        acumulator += 1
        pdf.cell(35, 10, str(acumulator), 1)
        pdf.cell(35, 10, str(row["Nombre"]), 1)
        pdf.cell(35, 10, str(row["Cantidad"]), 1)
        pdf.cell(35, 10, str(row["Precio Unitario"]), 1)
        pdf.cell(35, 10, str(row["Subtotal"]), 1)
        pdf.ln()

    #Mostramos información final
    total = sale["Total"]
    total = int(total[1:])
    subtotal = round(total / 1.19)
    iva = round(subtotal * 0.19)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Subtotal: {str(subtotal)} COP', 0, 1)
    pdf.cell(0, 10, f'IVA: {str(iva)} COP', 0, 1)
    pdf.cell(0, 10, f'Total: {str(total)} COP', 0, 1)

    # Ruta de guardado del PDF en la carpeta de descargas
    file_path = os.path.join(os.path.expanduser("~"), "Downloads", "facturacion.pdf")
    pdf.output(file_path)
    mb.showinfo(title="PDF Generado", message="El PDF ha sido creado correctamente en la carpeta Descargas")

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
    command=openShoppingCart,
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
    text=sale["Usuario"],
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    335.0,
    172.0,
    anchor="nw",
    text=f"{sale['Total']} COP",
    fill="#000000",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    521.0,
    172.0,
    anchor="nw",
    text=sale["Fecha"],
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
    50.0,
    231.0,
    anchor="nw",
    text="N°",
    fill="#535353",
    font=("Rubik Medium", 16 * -1)
)

try:
    product = sale["Productos"][0]
    product_name_1 = product["Nombre"]
    product_quantity_1 = product["Cantidad"]
    product_unitary_1 = product["Precio Unitario"]
    product_subtotal_1 = product["Subtotal"]

    createRectangle(40.0, 264.0, 695.0, 320.0)
    createTableText(64.0, 282.0, "1")
    createTableText(135.0, 282.0, product_name_1)
    createTableText(375.0, 282.0, product_quantity_1)
    createTableText(482.0, 282.0, f"${product_unitary_1}")
    createTableText(595.0, 282.0, f"${product_subtotal_1}")
except IndexError:
    pass

try:
    product = sale["Productos"][1]
    product_name_2 = product["Nombre"]
    product_quantity_2 = product["Cantidad"]
    product_unitary_2 = product["Precio Unitario"]
    product_subtotal_2 = product["Subtotal"]

    createRectangle(42.0, 327.0, 697.0, 383.0)
    createTableText(66.0, 345.0, "2")
    createTableText(137.0, 345.0, product_name_2)
    createTableText(377.0, 345.0, product_quantity_2)
    createTableText(484.0, 345.0, f"${product_unitary_2}")
    createTableText(597.0, 345.0, f"${product_subtotal_2}")

except IndexError:
    pass

try:
    product = sale["Productos"][2]
    product_name_3 = product["Nombre"]
    product_quantity_3 = product["Cantidad"]
    product_unitary_3 = product["Precio Unitario"]
    product_subtotal_3 = product["Subtotal"]

    createRectangle(42.0, 390.0, 697.0, 446.0)
    createTableText(66.0, 408.0, "3")
    createTableText(137.0, 408.0, product_name_3)
    createTableText(377.0, 408.0, product_quantity_3)
    createTableText(484.0, 408.0, f"${product_unitary_3}")
    createTableText(597.0, 408.0, f"${product_subtotal_3}")

except IndexError:
    pass

try:
    product = sale["Productos"][3]
    product_name_4 = product["Nombre"]
    product_quantity_4 = product["Cantidad"]
    product_unitary_4 = product["Precio Unitario"]
    product_subtotal_4 = product["Subtotal"]

    createRectangle(42.0, 453.0, 697.0, 509.0)
    createTableText(66.0, 471.0, "4")
    createTableText(137.0, 471.0, product_name_4)
    createTableText(377.0, 471.0, product_quantity_4)
    createTableText(484.0, 471.0, f"${product_unitary_4}")
    createTableText(597.0, 471.0, f"${product_subtotal_4}")

except IndexError:
    pass

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= generatePDF,
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
    command=openShoppingCart,
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