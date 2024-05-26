from pathlib import Path
import os, sys, subprocess, sqlite3, shutil
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

CURRENT_DIR = Path(__file__).resolve().parent
RELATIVE_PATH = Path("../assets/addProducts")
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
LOGIN_PATH = CURRENT_DIR / ("../login/adminLogin.py")
IMAGES_PATH = CURRENT_DIR / ("../images")
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

def uploadProctImage():
    print("Upload_Product_Image clicked")
    global uploadedProctImage
    uploadedProctImage = filedialog.askopenfilename(title="Select Image File", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    saveImageInFolder()
    if uploadedProctImage:
        if uploadedProctImage.lower().endswith('.png'):
            print(f"Selected image file: {uploadProctImage}")
            return uploadedProctImage
        else:
            print("Error: Invalid file. Please select a .png file.")
            mb.showerror(title="Error", message="Por favor seleccione un archivo .png")
            return None
    else:
        print("Error: No file selected.")
        return None
def saveImageInFolder():
    global productImage
    if not uploadedProctImage:
        print("Error: No image file selected.")
        return
    if not os.path.exists(uploadedProctImage):
        print("Error: The selected image file does not exist.")
        return
    try:
        shutil.copy2(uploadedProctImage, IMAGES_PATH)
        print(f"The image has been successfully copied to {IMAGES_PATH}")
        productImage = os.path.basename(uploadedProctImage)
    except FileNotFoundError:
        print("Error: The source file does not exist.")
    except PermissionError:
        print("Error: Permission denied to write to the destination folder.")
    except Exception as e:
        print(f"Error unknown when copying image: {e}")
def chageImageProctName(newName):
    global productImage
    os.rename(IMAGES_PATH / productImage, IMAGES_PATH / f"{newName}.png")
    productImage=f"{newName}.png"
def addProduct():
    print("Add_Product_Button clicked")
    product_code = entry_1.get().strip()
    product_category = entry_2.get().strip()
    product_stock = entry_3.get().strip()
    product_name = entry_4.get().strip()
    product_description = entry_5.get().strip()
    product_price = entry_6.get().strip()
    chageImageProctName(product_name)
    product_image = productImage
    
    print (f'entry_1 = {product_code}, entry_2 = {product_category}, entry_3 = {product_stock}, entry_4 = {product_name}, entry_5 = {product_description}, entry_6 = {product_price}, image = {productImage}.')

    if not all([product_code, product_category, product_stock, product_name, product_description, product_price]):
        print("Error: All fields are required.")
        mb.showerror(title="Ha ocurrido un error", message="Rellana todos los campos del formulario.")
        return
    if product_image is None:
        print("Error: Image wasn't uploaded.")
        mb.showerror(title="Ha ocurrido un error", message="Por favor suba una imagen para el producto.")
        return

    try:
        product_stock = int(product_stock)
        product_price = float(product_price)
    except ValueError:
        print("Error: Stock must be an integer and price must be a number.")
        mb.showerror(title="Datos invalidos", message="El stock debe ser un numero entero y el precio un numero real.")
        return
    
    db_path = CURRENT_DIR / ("../shopeasy.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO productos (codigo, nombre, categoria, descripcion, stock, precio, imagen)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                       (product_code, product_name, product_category, product_description, product_stock, product_price, product_image))
        conn.commit()
        print("Product added successfully!")
        mb.showinfo(title="Producto agregado", message="El producto fue agregado exitosamente.")
    except Exception as e:
        print(f"Error adding product: {e}")
        mb.showerror(title="Ha ocurrido un error", message="No ha sido posible añadir el producto.")
    conn.close()

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
    101.0,
    anchor="nw",
    text="Añadir Productos",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    294.0,
    147.0,
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
    191.0,
    anchor="nw",
    text="Código del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    293.0,
    anchor="nw",
    text="Categoría del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    395.0,
    anchor="nw",
    text="Stock",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    191.0,
    anchor="nw",
    text="Nombre del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    293.0,
    anchor="nw",
    text="Descripción del Producto",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    703.0,
    395.0,
    anchor="nw",
    text="Precio Unitario",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    485.0,
    250.5,
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
    y=228.0,
    width=364.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    485.0,
    352.5,
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
    y=330.0,
    width=364.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    485.0,
    454.5,
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
    y=432.0,
    width=364.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    894.0,
    250.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=712.0,
    y=228.0,
    width=364.0,
    height=43.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    894.0,
    352.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=712.0,
    y=330.0,
    width=364.0,
    height=43.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    894.0,
    454.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=712.0,
    y=432.0,
    width=364.0,
    height=43.0
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
addProduct_Button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=addProduct,
    relief="flat"
)
addProduct_Button.place(
    x=703.0,
    y=511.0,
    width=382.0,
    height=54.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
uploadProctImage_Button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=uploadProctImage,
    relief="flat"
)
uploadProctImage_Button.place(
    x=294.0,
    y=511.0,
    width=382.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()