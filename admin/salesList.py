from pathlib import Path
import os, sys, subprocess, sqlite3, xlsxwriter
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Button, PhotoImage

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/productsList")

# Combinamos la ruta actual con la parte relativa para obtener la ruta absoluta
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
# Get the login path.
LOGIN_PATH = CURRENT_DIR / ("../login/adminLogin.py")

# Obtener la ruta del directorio actual del script para abrir los demás archivos
script_dir = os.path.dirname(__file__)

def relative_to_assets(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return ASSETS_PATH / Path(path)

# Commands for the options and buttons.
def menu():
    admin_dashboard_path = os.path.join(script_dir, "adminDashboard.py")
    subprocess.Popen(['python', admin_dashboard_path])
    sys.exit(0)

def addProducts():
    path = os.path.join(script_dir, "addProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)

def deleteProducts():
    path = os.path.join(script_dir, "deleteProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)

def editProducts():
    path = os.path.join(script_dir, "editProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)

def productsList():
    path = os.path.join(script_dir, "productsList.py")
    subprocess.Popen(['python', path])
    sys.exit(0)

def salesList():
    path = os.path.join(script_dir, "salesList.py")
    subprocess.Popen(['python', path])
    sys.exit(0)

def signOff():
    path = LOGIN_PATH
    subprocess.Popen(['python', path])
    sys.exit(0)

def connect_to_database():
    conn = sqlite3.connect('shopeasy.db')
    cursor = conn.cursor()
    return conn, cursor

def showSales(canvas):
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM ventas")
    sales = cursor.fetchall()
    conn.close()

    y_positions = [290, 357, 424, 491, 562]
    for i, sale in enumerate(sales[:5]):
        product_code = sale[0]
        product_name = sale[1]
        category = sale[2]
        description = sale[3]
        stock = sale[4]
        price = sale[5]
        
        canvas.create_text(319, y_positions[i], anchor="nw", text=product_code, fill="#535353", font=("RubikRoman Regular", 15* -1))
        canvas.create_text(390, y_positions[i], anchor="nw", text=product_name, fill="#535353", font=("RubikRoman Regular", 15* -1))
        canvas.create_text(542, y_positions[i], anchor="nw", text=category, fill="#535353", font=("RubikRoman Regular", 15* -1))
        canvas.create_text(690, y_positions[i], anchor="nw", text=description, fill="#535353", font=("RubikRoman Regular", 15* -1))
        canvas.create_text(895, y_positions[i], anchor="nw", text=stock, fill="#535353", font=("RubikRoman Regular", 15* -1))
        canvas.create_text(1003, y_positions[i], anchor="nw", text=price, fill="#535353", font=("RubikRoman Regular", 15* -1))

def exportToExcel():
    try:
        conn, cursor = connect_to_database()
        cursor.execute("SELECT * FROM productos")
        all_products = cursor.fetchall()
        conn.close()
        
        workbook = xlsxwriter.Workbook(os.path.join(os.path.expanduser("~"), "Downloads", "productos.xlsx"))
        worksheet = workbook.add_worksheet()
        
        headers = ["Código", "Nombre", "Categoría", "Descripción", "Stock", "Precio", "Imagen"]
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        
        for row, product in enumerate(all_products, start=1):
            for col, value in enumerate(product):
                worksheet.write(row, col, value)
        
        workbook.close()
        mb.showinfo("Lista descargada", "Se ha creado el archivo Excel 'productos.xlsx' en la carpeta de Descargas.")
    except Exception as e:
        mb.showerror("Error", f"No se pudo crear el archivo Excel.\n\nError: {str(e)}")

window = Tk()

# Definimos dimensiones, nombre de la ventana, favicon y background-color
window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=639,
    width=1137,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(112.0, 47.0, image=image_image_1)

# Menu Button
menuOption = Button(
    window,
    text="Menu",
    bg="#FFFFFF",
    fg="#347AE2",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=menu
)
menuOption.place(x=82, y=110)
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(64.0, 122.0, image=image_image_2)

# Edit Products Button
editproductsOption = Button(
    window,
    text="Editar Productos",
    bg="#FFFFFF",
    fg="#7C8DB5",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=editProducts
)
editproductsOption.place(x=82, y=196)
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(63.0, 207.0, image=image_image_3)

# Add Products Button
addproductsOption = Button(
    window,
    text="Añadir Productos",
    bg="#FFFFFF",
    fg="#7C8DB5",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=addProducts
)
addproductsOption.place(x=80, y=153)
image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(59.0, 165.0, image=image_image_4)

# Delete Products Button
deleteproductsOption = Button(
    window,
    text="Eliminar Productos",
    bg="#FFFFFF",
    fg="#7C8DB5",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=deleteProducts
)
deleteproductsOption.place(x=82, y=239)
image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(64.0, 251.0, image=image_image_5)

# List Products Button
productsListOption = Button(
    window,
    text="Listar Productos",
    bg="#FFFFFF",
    fg="#7C8DB5",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=productsList
)
productsListOption.place(x=82, y=282)
image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(64.0, 293.0, image=image_image_6)

# List Sales Button
salesListOption = Button(
    window,
    text="Listar Ventas",
    bg="#FFFFFF",
    fg="#7C8DB5",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=salesList
)
salesListOption.place(x=82, y=325)
image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(63.0, 336.0, image=image_image_7)

# Sign Off Button
signOffOption = Button(
    window,
    text="Cerrar Sesión",
    bg="#FFFFFF",
    fg="#FF0000",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=signOff
)
signOffOption.place(x=82, y=585)
image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(63.0, 597.0, image=image_image_9)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1064.0,
    104.0,
    image=image_image_10
)

# UI Elements for Product List
canvas.create_text(
    296.0,
    79.0,
    anchor="nw",
    text="Listado de Ventas ",
    fill="#000000",
    font=("Poppins Bold", 28 * -1)
)
canvas.create_text(
    296.0,
    124.0,
    anchor="nw",
    text="Controla y sigue de la mejor manera tu inventario de productos",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
dowloadButton = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=exportToExcel,
    relief="flat"
)
dowloadButton.place(
    x=296.0,
    y=161.0,
    width=287.0,
    height=49.0
)

canvas.create_text(
    298.0,
    231.0,
    anchor="nw",
    text="Código",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
canvas.create_text(
    390.0,
    232.0,
    anchor="nw",
    text="Usuario",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
canvas.create_text(
    542.0,
    232.0,
    anchor="nw",
    text="Productos",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
canvas.create_text(
    749.0,
    232.0,
    anchor="nw",
    text="Subtotal",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
canvas.create_text(
    887.0,
    232.0,
    anchor="nw",
    text="Total",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
canvas.create_text(
    984.0,
    232.0,
    anchor="nw",
    text="Fecha",
    fill="#535353",
    font=("Poppins SemiBold", 16 * -1)
)
# Call the function to display products on the canvas
showSales(canvas)

window.resizable(False, False)
window.mainloop()
