from pathlib import Path
import os, sys, subprocess, sqlite3
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/editProducts")

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
def searchProduct():
    # Get the product code entered by the user.
    product_code = entry_1.get()
    # Connect to the database.
    conn, cursor = connect_to_database()
    # Run the query to get the product details.
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (product_code,))
    product_details = cursor.fetchone()  # Gets the first row of the results.
    # Close the connection to the database.
    conn.close()
    # If the product is not found, display an error message.
    if not product_details:
        print("El producto no fue encontrado en la base de datos.")
        mb.showerror(title="Ha ocurrido un error", message="El producto no fue encontrado en la base de datos.")
        return
    # Update input values with product details.
    entry_2.delete(0, 'end')  # Clear the input before assigning a new value.
    entry_2.insert(0, product_details[1])  # Product name.
    entry_5.delete(0, 'end')  # Clear the input before assigning a new value.
    entry_5.insert(0, product_details[2])  # Product category.
    entry_3.delete(0, 'end')  # Clear the input before assigning a new value.
    entry_3.insert(0, product_details[3])  # Product description.
    entry_6.delete(0, 'end')  # Clear the input before assigning a new value.
    entry_6.insert(0, product_details[4])  # Stock.
    entry_4.delete(0, 'end')  # Clear the input before assigning a new value.
    entry_4.insert(0, product_details[5])  # Unit price.
def updateProduct():
    # Get the values entered in the inputs.
    product_code = entry_1.get()
    product_name = entry_2.get()
    product_category = entry_5.get()
    product_description = entry_3.get()
    product_stock = entry_6.get()
    product_price = entry_4.get()
    # Validate that the required fields are not empty.
    if not (product_code and product_name and product_category and product_stock and product_price):
        print("Por favor, complete todos los campos obligatorios.")
        mb.showerror(title="Error", message="Por favor, complete todos los campos obligatorios.")
        return
    # Validate that the stock and price are valid numbers.
    try:
        product_stock = int(product_stock)
        product_price = float(product_price)
    except ValueError:
        print("El stock y el precio deben ser números válidos.")
        mb.showerror(title="Error", message="El stock y el precio deben ser números válidos.")
        return
    # Connect to the database.
    conn, cursor = connect_to_database()
    # Run the SQL UPDATE query to update the records in the database.
    cursor.execute("UPDATE productos SET nombre = ?, categoria = ?, descripcion = ?, stock = ?, precio = ? WHERE codigo = ?",
                   (product_name, product_category, product_description, product_stock, product_price, product_code))
    # Commit changes to the database.
    conn.commit()
    # Close the connection.
    conn.close()
    # Show a success message.
    print("Los datos del producto se han actualizado correctamente.")
    mb.showinfo(title="Éxito", message="Los datos del producto se han actualizado correctamente.")

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
    294.0,
    45.0,
    anchor="nw",
    text="Editar Productos",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    91.0,
    anchor="nw",
    text="Controla y sigue de la mejor manera tu inventario de productos",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1062.0,
    77.0,
    image=image_image_10
)

canvas.create_text(
    294.0,
    132.0,
    anchor="nw",
    text="Código del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    239.0,
    anchor="nw",
    text="Nombre del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    346.0,
    anchor="nw",
    text="Descripción del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    453.0,
    anchor="nw",
    text="Precio Unitario",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    693.0,
    239.0,
    anchor="nw",
    text="Categoría del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    693.0,
    346.0,
    anchor="nw",
    text="Stock",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    485.0,
    191.5,
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
    y=169.0,
    width=364.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    485.0,
    298.5,
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
    y=276.0,
    width=364.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    485.0,
    405.5,
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
    y=383.0,
    width=364.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    485.0,
    512.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=303.0,
    y=490.0,
    width=364.0,
    height=43.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    884.0,
    298.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=702.0,
    y=276.0,
    width=364.0,
    height=43.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    884.0,
    405.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=702.0,
    y=383.0,
    width=364.0,
    height=43.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=updateProduct,
    relief="flat"
)
button_1.place(
    x=294.0,
    y=554.0,
    width=382.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=searchProduct,
    relief="flat"
)
button_2.place(
    x=693.0,
    y=165.0,
    width=287.0,
    height=49.0
)

canvas.create_rectangle(
    298.0,
    228.0,
    1075.0,
    229.0,
    fill="#E1E1E1",
    outline="")
window.resizable(False, False)
window.mainloop()
