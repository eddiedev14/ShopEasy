from pathlib import Path
import os, sys, subprocess, sqlite3
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label

CURRENT_DIR = Path(__file__).resolve().parent
RELATIVE_PATH = Path("../assets/deleteProducts")
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
LOGIN_PATH = CURRENT_DIR / ("../login/adminLogin.py")
script_dir = os.path.dirname(__file__)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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

def searchProduct():
    product_code = entry_1.get()
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (product_code,))
    product_details = cursor.fetchone()
    conn.close()
    if not product_details:
        print("El producto no fue encontrado en la base de datos.")
        mb.showerror(title="Ha ocurrido un error", message="El producto no fue encontrado en la base de datos.")
        return
    product_name_text.config(text="Nombre del Producto: " + product_details[1])
    category_text.config(text="Categoría del Producto: " + product_details[2])
    description_text.config(text="Descripción del Producto: " + product_details[3])
    stock_text.config(text="Stock: " + str(product_details[4]))
    price_text.config(text="Precio Unitario: " + str(product_details[5]))

def deleteProduct():
        product_code = entry_1.get()
        connection, cursor = connect_to_database()
        cursor.execute("DELETE FROM productos WHERE codigo = ?", (product_code,))
        connection.commit()
        connection.close()
        mb.showinfo(title="Producto eliminado", message="El producto fue eliminado exitosamente.")
        print("Producto eliminado exitosamente.")
        return
    
window = Tk()
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

editproductsOption = Button(
    window,
    text="Menu",
    bg="#FFFFFF",
    fg="#347AE2",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=menu
)
editproductsOption.place(x=82, y=110)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    122.0,
    image=image_image_2
)

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

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    63.0,
    207.0,
    image=image_image_3
)

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

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    59.0,
    165.0,
    image=image_image_4
)

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

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    64.0,
    251.0,
    image=image_image_5
)

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

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    64.0,
    293.0,
    image=image_image_6
)

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

signOffOption = Button(
    window,
    text="Cerrar Sesión",
    bg="#FFFFFF",
    fg="#FF3B30",
    font=("Poppins Medium", 16 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=signOff
)
signOffOption.place(x=82.00146484375, y=578)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))

image_9 = canvas.create_image(
    62.0,
    590.0,
    image=image_image_9
)

canvas.create_text(
    294.0,
    105.0,
    anchor="nw",
    text="Eliminar Productos",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    151.0,
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
    192.0,
    anchor="nw",
    text="Código del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    485.0,
    251.5,
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
    y=229.0,
    width=364.0,
    height=43.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
deleteProduct_Button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=deleteProduct,
    relief="flat"
)
deleteProduct_Button.place(
    x=294.0,
    y=511.0,
    width=382.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
searchProduct_Button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=searchProduct,
    relief="flat"
)
searchProduct_Button.place(
    x=693.0,
    y=225.0,
    width=287.0,
    height=49.0
)

canvas.create_rectangle(
    298.0,
    288.0,
    1075.0,
    289.0,
    fill="#E1E1E1",
    outline="")

product_name_text = Label(
window,
text="Nombre del Producto: ",
bg="#FFFFFF",
fg="#7C8DB5",
font=("Poppins Bold", 16 * -1)
)
product_name_text.place(x=294.0, y=311.0)

category_text = Label(
window,
text="Categoría del Producto:",
bg="#FFFFFF",
fg="#7C8DB5",
font=("Poppins Bold", 16 * -1)
)
category_text.place(x=294.0, y=348.0)

description_text = Label(
window,
text="Descripción del Producto:",
bg="#FFFFFF",
fg="#7C8DB5",
font=("Poppins Bold", 16 * -1),
)
description_text.place(x=294.0, y=385.0)

stock_text = Label(
window,
text="Stock:",
bg="#FFFFFF",
fg="#7C8DB5",
font=("Poppins Bold", 16 * -1)
)
stock_text.place(x=294.0, y=422.0)

price_text = Label(
window,
text="Precio Unitario: ",
bg="#FFFFFF",
fg="#7C8DB5",
font=("Poppins Bold", 16 * -1)
)
price_text.place(x=294.0, y=459.0)

window.resizable(False, False)
window.mainloop()