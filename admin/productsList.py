from pathlib import Path
import os, sys, subprocess, sqlite3, xlsxwriter
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
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
#commands for the options and buttons.
def menu():
    # Construir la ruta al archivo addProducts.py
    admin_dashboard_path = os.path.join(script_dir, "adminDashboard.py")
    subprocess.Popen(['python', admin_dashboard_path])
    sys.exit(0)
def addProducts():
    # Construir la ruta al archivo addProducts.py
    path = os.path.join(script_dir, "addProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)
def deleteProducts():
    # Construir la ruta al archivo deleteProducts.py
    path = os.path.join(script_dir, "deleteProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)
def editProducts():
    # Construir la ruta al archivo editProducts.py
    path = os.path.join(script_dir, "editProducts.py")
    subprocess.Popen(['python', path])
    sys.exit(0)
def productsList():
    # Construir la ruta al archivo productsList.py
    path = os.path.join(script_dir, "productsList.py")
    subprocess.Popen(['python', path])
    sys.exit(0)
def salesList():
    # Construir la ruta al archivo salesList.py
    path = os.path.join(script_dir, "salesList.py")
    subprocess.Popen(['python', path])
    sys.exit(0)
def signOff():
    # Make the path for the file adminLogin.py.
    path = LOGIN_PATH
    subprocess.Popen(['python', path])
    sys.exit(0)
def connect_to_database():
    conn = sqlite3.connect('shopeasy.db')
    cursor = conn.cursor()
    return conn, cursor
def showProducts_v1():
    # Connect to the database.
    conn, cursor = connect_to_database()
    # Run the query to get all products.
    cursor.execute("SELECT * FROM productos")
    all_products = cursor.fetchall()  # Gets all rows of the results.
    # Close the connection to the database.
    conn.close()

    # Display the products in a table format.
    for index, product in enumerate(all_products):
        print(f"Producto {index + 1}:")
        print(f"Código: {product[0]}")
        print(f"Nombre: {product[1]}")
        print(f"Categoría: {product[2]}")
        print(f"Descripción: {product[3]}")
        print(f"Stock: {product[4]}")
        print(f"Precio: {product[5]}")
        print("---------------------------")
def showProducts_v2():
    # Connect to the database.
    conn, cursor = connect_to_database()
    # Run the query to get all products.
    cursor.execute("SELECT * FROM productos")
    all_products = cursor.fetchall()  # Gets all rows of the results.
    # Close the connection to the database.
    conn.close()
    # Update the texts with product details in the GUI.
    for index, product in enumerate(all_products):
        product_code_text.config(text=f"Código: {product[0]}")
        product_name_text.config(text=f"Nombre: {product[1]}")
        category_text.config(text=f"Categoría: {product[2]}")
        description_text.config(text=f"Descripción: {product[3]}")
        stock_text.config(text=f"Stock: {product[4]}")
        price_text.config(text=f"Precio: {product[5]}")
        # Optionally, you can add some delay here if you want to see each product one by one.
        window.update()  # Update the GUI to reflect changes.
def productsList():
    # Show all products.
    showProducts_v1()
def exportToExcel():
    try:
        # Connect to the database.
        conn, cursor = connect_to_database()
        # Run the query to get all products.
        cursor.execute("SELECT * FROM productos")
        all_products = cursor.fetchall()  # Gets all rows of the results.
        # Close the connection to the database.
        conn.close()
        # Create a new Excel workbook and worksheet.
        workbook = xlsxwriter.Workbook(os.path.join(os.path.expanduser("~"), "Downloads", "productos.xlsx"))
        worksheet = workbook.add_worksheet()
        # Write headers.
        headers = ["Código", "Nombre", "Categoría", "Descripción", "Stock", "Precio", "Imagen"]
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        # Write product data.
        for row, product in enumerate(all_products, start=1):
            for col, value in enumerate(product):
                worksheet.write(row, col, value)
        # Close the workbook.
        workbook.close()
        # Show success message.
        mb.showinfo("Lista descargada", "Se ha creado el archivo Excel 'productos.xlsx' en la carpeta de Descargas.")
    except Exception as e:
        # Show error message.
        mb.showerror("Error", f"No se pudo crear el archivo Excel.\n\nError: {str(e)}")

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
# Create the editproductsOption Button
editproductsOption = Button(
    window,
    text="Menu",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#347AE2",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=menu
)
# Place the deleteproductsOption Button
editproductsOption.place(x=82, y=110)
# Option icon.
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    122.0,
    image=image_image_2
)
# Create the editproductsOption Button
editproductsOption = Button(
    window,
    text="Editar Productos",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#7C8DB5",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=editProducts
)
# Place the deleteproductsOption Button
editproductsOption.place(x=82, y=196)
# Option icon.
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    63.0,
    207.0,
    image=image_image_3
)
# Create the addproductsOption Button
addproductsOption = Button(
    window,
    text="Añadir Productos",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#7C8DB5",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=addProducts
)
# Place the addproductsOption Button
addproductsOption.place(x=80, y=153)
# Option icon.
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    59.0,
    165.0,
    image=image_image_4
)
# Create the deleteproductsOption Button
deleteproductsOption = Button(
    window,
    text="Eliminar Productos",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#7C8DB5",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=deleteProducts
)
# Place the deleteproductsOption Button
deleteproductsOption.place(x=82, y=239)
# Option icon.
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    64.0,
    251.0,
    image=image_image_5
)
# Create the productsListOption Button
productsListOption = Button(
    window,
    text="Listar Productos",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#7C8DB5",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=productsList
)
# Place the productsListOption Button
productsListOption.place(x=82, y=282)
# Option icon.
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    64.0,
    293.0,
    image=image_image_6
)
# Create the saleListOption Button
salesListOption = Button(
    window,
    text="Listar Ventas",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#7C8DB5",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=salesList
)
# Place the salesListOption Button
salesListOption.place(x=82, y=325)
# Option icon.
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

# Create the signOffOption Button
signOffOption = Button(
    window,
    text="Cerrar Sesión",
    bg="#FFFFFF",  # Set background color to match window background
    fg="#FF3B30",  # Set text color
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,  # Set border width to 0 to remove border
    highlightthickness=0,  # Set highlight thickness to 0 to remove border highlight
    command=signOff
)
# Place the signOffOption Button
signOffOption.place(x=82.00146484375, y=578)
# Option icon.
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
dowloadButton = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=exportToExcel, #Call exportToExcel function when clicked
    relief="flat"
)
dowloadButton.place(
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
