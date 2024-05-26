from pathlib import Path
import os, sys, subprocess, sqlite3
from tkinter import Tk, Canvas, Button, PhotoImage

CURRENT_DIR = Path(__file__).resolve().parent
RELATIVE_PATH = Path("../assets/adminDashboard")
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
LOGIN_PATH = CURRENT_DIR / ("../login/adminLogin.py")

script_dir = os.path.dirname(__file__)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def getProductsCount():
    db_path = CURRENT_DIR / ("../shopeasy.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def getTotalIncomes():
    db_path = CURRENT_DIR / ("../shopeasy.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(total) FROM ventas")
    total_income = cursor.fetchone()[0]
    conn.close()
    return total_income if total_income is not None else 0

def getUsersCount():
    db_path = CURRENT_DIR / ("../shopeasy.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE tipo != 'Admin'")
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count

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
    image=image_image_3)

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

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    62.0,
    590.0,
    image=image_image_8
)

canvas.create_rectangle(
    302.0,
    189.0,
    498.0,
    328.0,
    fill="#FFADAD",
    outline="")

canvas.create_rectangle(
    531.0,
    189.0,
    727.0,
    328.0,
    fill="#9EC7FF",
    outline="")

canvas.create_rectangle(
    759.0,
    189.0,
    955.0,
    328.0,
    fill="#96FFAD",
    outline="")

canvas.create_text(
    294.0,
    101.0,
    anchor="nw",
    text="Bienvenido de vuelta, George",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    147.0,
    anchor="nw",
    text="Conoce las estadísticas generales de tu empresa",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    314.0,
    201.0,
    anchor="nw",
    text="Productos Totales",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

product_count = getProductsCount()
canvas.create_text(
    379.0,
    241.0,
    anchor="nw",
    text=f"{product_count}",
    fill="#161E54",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    314.0,
    289.0,
    anchor="nw",
    text="Productos añadidos",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

canvas.create_text(
    549.0,
    201.0,
    anchor="nw",
    text="Ingresos Totales",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

total_incomes = getTotalIncomes()
canvas.create_text(
    549.0,
    245.0,
    anchor="nw",
    text=f"${total_incomes:,.2f}",
    fill="#161E54",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    549.0,
    289.0,
    anchor="nw",
    text="Pesos colombianos",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

canvas.create_text(
    771.0,
    201.0,
    anchor="nw",
    text="Usuarios Registrados",
    fill="#161E54",
    font=("Poppins Medium", 18 * -1)
)

user_count = getUsersCount()
canvas.create_text(
    771.0,
    245.0,
    anchor="nw",
    text=f"{user_count}",
    fill="#161E54",
    font=("Poppins Bold", 36 * -1)
)

canvas.create_text(
    771.0,
    289.0,
    anchor="nw",
    text="Usuarios",
    fill="#161E54",
    font=("Roboto Regular", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=addProducts,
    relief="flat"
)
button_1.place(
    x=302.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=editProducts,
    relief="flat"
)
button_2.place(
    x=432.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=deleteProducts,
    relief="flat"
)
button_3.place(
    x=562.0,
    y=349.0,
    width=108.0,
    height=97.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=productsList,
    relief="flat"
)
button_4.place(
    x=302.0,
    y=455.0,
    width=108.0,
    height=97.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=salesList,
    relief="flat"
)
button_5.place(
    x=432.0,
    y=455.0,
    width=108.0,
    height=97.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    886.0,
    534.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1062.0,
    131.0,
    image=image_image_10
)
window.resizable(False, False)

window.mainloop()