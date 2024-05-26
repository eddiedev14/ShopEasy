from pathlib import Path
import os, sys, subprocess, sqlite3
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

CURRENT_DIR = Path(__file__).resolve().parent
RELATIVE_PATH = Path("../assets/editProducts")
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
    entry_2.delete(0, 'end')
    entry_2.insert(0, product_details[1])
    entry_5.delete(0, 'end')
    entry_5.insert(0, product_details[2])
    entry_3.delete(0, 'end')
    entry_3.insert(0, product_details[3])
    entry_6.delete(0, 'end')
    entry_6.insert(0, product_details[4])
    entry_4.delete(0, 'end')
    entry_4.insert(0, product_details[5])

def updateProduct():
    product_code = entry_1.get()
    product_name = entry_2.get()
    product_category = entry_5.get()
    product_description = entry_3.get()
    product_stock = entry_6.get()
    product_price = entry_4.get()
    if not (product_code and product_name and product_category and product_stock and product_price):
        print("Por favor, complete todos los campos obligatorios.")
        mb.showerror(title="Error", message="Por favor, complete todos los campos obligatorios.")
        return
    try:
        product_stock = int(product_stock)
        product_price = float(product_price)
    except ValueError:
        print("El stock y el precio deben ser números válidos.")
        mb.showerror(title="Error", message="El stock y el precio deben ser números válidos.")
        return
    conn, cursor = connect_to_database()
    cursor.execute("UPDATE productos SET nombre = ?, categoria = ?, descripcion = ?, stock = ?, precio = ? WHERE codigo = ?",
                   (product_name, product_category, product_description, product_stock, product_price, product_code))
    conn.commit()
    conn.close()
    print("Los datos del producto se han actualizado correctamente.")
    mb.showinfo(title="Éxito", message="Los datos del producto se han actualizado correctamente.")

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