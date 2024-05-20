import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import sys
import sqlite3
from PIL import Image
import ast
import subprocess
import json

cedula = sys.argv[1]

#Validamos que se haya pasado un segundo parametro
if len(sys.argv) > 2:
    #Obtenemos el arreglo en string
    cartProducts_str = sys.argv[2]
    # Convert the string to a list of dictionaries
    cartProducts = ast.literal_eval(cartProducts_str)
else:
    cartProducts = []

CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/userDashboard")
RELATIVE_PATH2 = Path("../images")

# Combinamos la ruta actual con la parte relativa para obtener la ruta absoluta
ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH
IMAGES_PATH = CURRENT_DIR / RELATIVE_PATH2

def relative_to_assets(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return ASSETS_PATH / Path(path)

def relative_to_images(path: str) -> Path:
    # Combinamos la ruta de los assets con la ruta proporcionada
    return IMAGES_PATH / Path(path)

# Obtener la ruta del directorio actual del script para abrir los demás archivos
script_dir = os.path.dirname(__file__)

def openShoppingCart():
    # Construir la ruta al archivo userLogin.py
    shopping_cart_path = os.path.join(script_dir, "shoppingCart.py")
    
   # Convert the list of dictionaries to a string
    cartProducts_str = json.dumps(cartProducts)

    subprocess.Popen(['python', shopping_cart_path, cartProducts_str, cedula])
    sys.exit(0)

def logout():
    # Construir la ruta al archivo userLogin.py
    logout_path = os.path.join(script_dir, "../login/userLogin.py")

    subprocess.Popen(['python', logout_path])
    sys.exit(0)

#Obtenemos el nombre del usuario que acaba de ingresar
def getName(cedula):
    db = sqlite3.connect('shopeasy.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE cedula=? AND tipo=?", (cedula, "Usuario"))
    user = cursor.fetchone()
    #Retornamos el nombre del usuario que tenga esa cedula
    return user[1]

#Función para redimensionar imagen
def redimensionateImg(imagePath):
    #Necesitamos redimensionar la imagen para que se vea bien para eso, usamos PIL
    imagen = Image.open(relative_to_images(imagePath))
    #Obtenemos ancho y alto de la imagen
    ancho, alto = imagen.size
    #Validamos si el ancho y alto es diferente a 96x96, para ese caso debemos redimensionar la imagen
    if ancho != 96 and alto != 96:
        #Le damos tamaño de 96px x 96px
        imagenRedimensionada = imagen.resize((96, 96))
        #Actualizamos la imagen
        imagenRedimensionada.save(f"images/{imagePath}")

#Función para formatear precio del producto con punto de mil
def formatPrice(price):
    precioFormateado = '{:,}'.format(price)
    return precioFormateado[:-2]

#Función para automatizar la creación del nombre del producto, descripción y precio
def createTitle(text, x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill="#000000",
        font=("DMSans Medium", 13 * -1)
    )

def createDescription(text, x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill="#979797",
        font=("Inter", 9 * -1)
    )

def createPrice(text, x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text=f"${text} COP",
        fill="#3381DB",
        font=("Inter Bold", 12 * -1)
    )

def createCounter(x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text="0",
        fill="#979797",
        font=("Inter Bold", 9 * -1)
    )

#Disminuir valor del contador
def decreaseCounter(counter):
    # Para obtener el contenido del elemento creado:
    value = int(canvas.itemcget(counter, "text"))

    #Solo disminuiremos si el valor es mayor que 0, ya que si no el valor seria negativo
    if value > 0:
        newValue = value - 1
        canvas.itemconfig(counter, text=str(newValue))

#Aumentar valor del contador
def increaseCounter(counter, stock):
    # Para obtener el contenido del elemento creado:
    value = int(canvas.itemcget(counter, "text"))

    #Validamos para que no se pase del stock
    if value < int(stock):
        newValue = value + 1
        canvas.itemconfig(counter, text=str(newValue))

def addProduct(counter, title, description, price, imgFile, stock):
    quantity = int(canvas.itemcget(counter, "text"))
    productTitle = canvas.itemcget(title, "text")
    productDescription = canvas.itemcget(description, "text")
    productPrice = canvas.itemcget(price, "text")
    productPrice = productPrice[1:-4]
    productPrice = int(productPrice.replace(",", ""))

    subtotal = quantity * productPrice

    #Actualizamos en caso de que exista o lo agregamos
    for i in cartProducts:
        if i["Nombre"] == productTitle and i["Descripcion"] == productDescription and i["Precio Unitario"] == productPrice and i["Imagen"] == imgFile and i["Stock"] == stock:
            #Como sabemos que el elemento existe, encontramos el indice
            index = cartProducts.index(i)
            
            #Actualizamos valores y actualizamos la lista
            i["Cantidad"] += quantity
            i["Subtotal"] += subtotal
            cartProducts[index] = i

            #Mostramos mensaje
            messagebox.showinfo("Carrito Actualizado", "El producto ha sido actualizado en el carrito de compras exitosamente")
            
            #Retornamos para que no se ejecute el código de abajo
            return

    #Creamos el diccionario
    newProductCard = {
        "Nombre": productTitle,
        "Descripcion": productDescription,
        "Cantidad": quantity,
        "Precio Unitario": productPrice,
        "Subtotal": subtotal,
        "Imagen": imgFile,
        "Stock": stock
    }

    #Agregammos diccionario a la lista
    cartProducts.append(newProductCard)

    #Mostramos mensaje
    messagebox.showinfo("Carrito Actualizado", "El producto ha sido añadido al carrito de compras exitosamente")

window = Tk()

#Definimos dimensiones, nombre de la ventana, favicon y background-color
window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")

#Cargamos los productos de la base de datos y obtenemos 9 de ellos
db = sqlite3.connect('shopeasy.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM productos")
products = cursor.fetchmany(9)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 639,
    width = 1137,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.create_text(
    50.0,
    74.0,
    anchor="nw",
    text=f"Bienvenido de vuelta, {getName(cedula)}",
    fill="#000000",
    font=("Poppins Medium", 28 * -1)
)

canvas.create_text(
    50.0,
    120.0,
    anchor="nw",
    text="Visualiza nuestra oferta de productos y adquiérelos en instantes",
    fill="#7C8DB5",
    font=("Poppins Regular", 16 * -1)
)

canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=openShoppingCart,
    relief="flat"
)
button_1.place(
    x=942.0,
    y=81.0,
    width=31.0,
    height=31.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    112.0,
    47.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1070.0,
    97.0,
    image=image_image_2
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_29.place(
    x=994.0,
    y=81.0,
    width=31.0,
    height=31.0
)

#Verificamos que exista el elemento 1 y creamos su componente
try:
    product = products[0]
    stock_1 = product[4]
    product_imagen_1 = product[6]

    image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"),
    )
    image_3 = canvas.create_image(
        209.0,
        216.0,
        image=image_image_3
    )

    #Redimensionar imagen
    redimensionateImg(product[6])

    #Colocar imagen del producto
    image_image_12 = PhotoImage(file=relative_to_images(product_imagen_1))
    image_12 = canvas.create_image(
        104.0,
        216.0,
        image=image_image_12,
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_1 = createTitle(product[1], 164.0, 174.0)
    description_1 = createDescription(f"{product[3]} (Quedan {stock_1} UND)", 164.0, 197.0)
    price_1 = createPrice(precioFormateado, 164.0, 237.0)
    counter_1 = createCounter(298.0625,245.0625)

    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: decreaseCounter(counter_1)
    )
    button_2.place(
        x=279.0,
        y=244.0,
        width=13.125,
        height=13.125
    )

    button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: increaseCounter(counter_1, stock_1)
    )
    button_11.place(
        x=314.0,
        y=244.0,
        width=13.125,
        height=13.125
    )

    button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_20 = Button(
        image=button_image_20,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_1, title_1, description_1, price_1, product_imagen_1, stock_1)
    )
    button_20.place(
        x=340.0,
        y=240.0,
        width=20.0,
        height=20.0
    )

#En caso de que no exista no lo creamos
except IndexError:
    pass

#Verificamos que exista el elemento 2 y creamos su componente

try:
    product = products[1]
    stock_2 = product[4]
    product_imagen_2 = product[6]

    image_image_6 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_6 = canvas.create_image(
        567.0,
        216.0,
        image=image_image_6
    )

    redimensionateImg(product[6])

    image_image_15 = PhotoImage(
    file=relative_to_images(product_imagen_2))
    image_15 = canvas.create_image(
        462.0,
        216.0,
        image=image_image_15
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_2 = createTitle(product[1], 522.0, 174.0)
    description_2 = createDescription(f"{product[3]} (Quedan {stock_2} UND)", 522.0, 197.0)
    price_2 = createPrice(precioFormateado, 522.0, 237.0)
    counter_2 = createCounter(657.0, 245.0)

    button_image_5 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_2),
        relief="flat"
    )
    button_5.place(
        x=637.9375,
        y=243.9375,
        width=13.125,
        height=13.125
    )

    button_image_14 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_2, stock_2),
        relief="flat"
    )
    button_14.place(
        x=671.9375,
        y=243.9375,
        width=13.125,
        height=13.125
    )

    button_image_21 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_21 = Button(
        image=button_image_21,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_2, title_2, description_2, price_2, product_imagen_2, stock_2)
    )
    button_21.place(
        x=697.0,
        y=239.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

#Verificamos que exista el elemento 3 y creamos su componente
try:
    product = products[2]
    stock_3 = product[4]
    product_imagen_3 = product[6]

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_9 = canvas.create_image(
        925.0,
        216.0,
        image=image_image_9
    )

    redimensionateImg(product[6])

    image_image_18 = PhotoImage(
    file=relative_to_images(product_imagen_3))
    image_18 = canvas.create_image(
        820.0,
        216.0,
        image=image_image_18
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])
    
    title_3 = createTitle(product[1], 880.0, 174.0)
    description_3 = createDescription(f"{product[3]} (Quedan {stock_3} UND)", 880.0, 197.0)
    price_3 = createPrice(precioFormateado, 880.0, 237.0)
    counter_3 = createCounter(1015.0625, 243.0625)

    button_image_8 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_3),
        relief="flat"
    )
    button_8.place(
        x=996.0,
        y=242.0,
        width=13.125,
        height=13.125
    )

    button_image_17 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_17 = Button(
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_3, stock_3),
        relief="flat"
    )
    button_17.place(
        x=1030.0,
        y=242.0,
        width=13.125,
        height=13.125
    )

    button_image_22 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_22 = Button(
        image=button_image_22,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_3, title_3, description_3, price_3, product_imagen_3, stock_3)
    )
    button_22.place(
        x=1052.0,
        y=239.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

#Verificamos que exista el elemento 4 y creamos su componente
try:
    product = products[3]
    stock_4 = product[4]
    product_imagen_4 = product[6]

    image_image_4 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_4 = canvas.create_image(
        209.0,
        354.0,
        image=image_image_4
    )

    redimensionateImg(product[6])

    image_image_13 = PhotoImage(
    file=relative_to_images(product_imagen_4))
    image_13 = canvas.create_image(
        104.0,
        354.0,
        image=image_image_13
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_4 = createTitle(product[1], 164.0, 313.0)
    description_4 = createDescription(f"{product[3]} (Quedan {stock_4} UND)", 164.0, 335.0)
    price_4 = createPrice(precioFormateado, 164.0, 375.0)
    counter_4 = createCounter(299.0625, 383.0625)

    button_image_3 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command= lambda: decreaseCounter(counter_4)
    )
    button_3.place(
        x=280.0,
        y=382.0,
        width=13.125,
        height=13.125
    )

    button_image_12 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command= lambda: increaseCounter(counter_4, stock_4)
    )
    button_12.place(
        x=313.9375,
        y=381.9375,
        width=13.125,
        height=13.125
    ) 

    button_image_27 = PhotoImage(
        file=relative_to_assets("button_20.png"))
    button_27 = Button(
        image=button_image_27,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_4, title_4, description_4, price_4, product_imagen_4, stock_4)
    )
    button_27.place(
        x=340.0,
        y=377.0,
        width=20.0,
        height=20.0
    ) 

except IndexError:
    pass

#Verificamos que exista el elemento 5 y creamos su componente
try:
    product = products[4]
    stock_5 = product[4]
    product_imagen_5 = product[6]

    image_image_7 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_7 = canvas.create_image(
        567.0,
        354.0,
        image=image_image_7
    )

    redimensionateImg(product[6])

    image_image_16 = PhotoImage(
    file=relative_to_images(product_imagen_5))
    image_16 = canvas.create_image(
        462.0,
        354.0,
        image=image_image_16
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_5 = createTitle(product[1], 522.0, 313.0)
    description_5 = createDescription(f"{product[3]} (Quedan {stock_5} UND)", 522.0, 335.0)
    price_5 = createPrice(precioFormateado, 522.0, 375.0)
    counter_5 = createCounter(657.0, 383.0)

    button_image_6 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_5),
        relief="flat"
    )
    button_6.place(
        x=637.9375,
        y=381.9375,
        width=13.125,
        height=13.125
    )

    button_image_15 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_5, stock_5),
        relief="flat"
    )
    button_15.place(
        x=671.9375,
        y=381.9375,
        width=13.125,
        height=13.125
    )

    button_image_25 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_25 = Button(
        image=button_image_25,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_5, title_5, description_5, price_5, product_imagen_5, stock_5)
    )
    button_25.place(
        x=697.0,
        y=378.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

#Verificamos que exista el elemento 6 y creamos su componente
try:
    product = products[5]
    stock_6 = product[4]
    product_imagen_6 = product[6]

    image_image_10 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_10 = canvas.create_image(
        925.0,
        354.0,
        image=image_image_10
    )

    redimensionateImg(product[6])

    image_image_19 = PhotoImage(
    file=relative_to_images(product_imagen_6))
    image_19 = canvas.create_image(
        820.0,
        354.0,
        image=image_image_19
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_6 = createTitle(product[1], 880.0, 313.0)
    description_6 = createDescription(f"{product[3]} (Quedan {stock_6} UND)", 880.0, 335.0)
    price_6 = createPrice(precioFormateado, 880.0, 375.0)
    counter_6 = createCounter(1015.0625, 379.0625)

    button_image_9 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_6),
        relief="flat"
    )
    button_9.place(
        x=996.0,
        y=378.0,
        width=13.125,
        height=13.125
    )

    button_image_18 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_18 = Button(
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_6, stock_6),
        relief="flat"
    )
    button_18.place(
        x=1030.0,
        y=378.0,
        width=13.125,
        height=13.125
    )

    button_image_23 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_23 = Button(
        image=button_image_23,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_6, title_6, description_6, price_6, product_imagen_6, stock_6)
    )
    button_23.place(
        x=1052.0,
        y=375.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

#Verificamos que exista el elemento 7 y creamos su componente
try:
    product = products[6]
    stock_7 = product[4]
    product_imagen_7 = product[6]

    image_image_5 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_5 = canvas.create_image(
        209.0,
        492.0,
        image=image_image_5
    )

    redimensionateImg(product[6])

    image_image_14 = PhotoImage(
    file=relative_to_images(product_imagen_7))
    image_14 = canvas.create_image(
        104.0,
        492.0,
        image=image_image_14
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_7 = createTitle(product[1], 164.0, 448.0)
    description_7 = createDescription(f"{product[3]} (Quedan {stock_7} UND)", 164.0, 473.0)
    price_7= createPrice(precioFormateado, 164.0, 513.0)
    counter_7 = createCounter(299.0, 521.0)

    button_image_4 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command= lambda:decreaseCounter(counter_7)
    )
    button_4.place(
        x=279.9375,
        y=519.9375,
        width=13.125,
        height=13.125
    )

    button_image_13 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command= lambda:increaseCounter(counter_7, stock_7)
    )
    button_13.place(
        x=313.9375,
        y=519.9375,
        width=13.125,
        height=13.125
    )

    button_image_28 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_28 = Button(
        image=button_image_28,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_7, title_7, description_7, price_7, product_imagen_7, stock_7)
    )
    button_28.place(
        x=340.0,
        y=517.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

#Verificamos que exista el elemento 8 y creamos su componente
try:
    product = products[7]
    stock_8 = product[4]
    product_imagen_8 = product[6]

    image_image_8 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_8 = canvas.create_image(
        567.0,
        492.0,
        image=image_image_8
    )

    redimensionateImg(product[6])

    image_image_17 = PhotoImage(
    file=relative_to_images(product_imagen_8))
    image_17 = canvas.create_image(
        462.0,
        492.0,
        image=image_image_17
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_8 = createTitle(product[1], 522.0, 448.0)
    description_8 = createDescription(f"{product[3]} (Quedan {stock_8} UND)", 522.0, 473.0)
    price_8 = createPrice(product[3], 522.0, 513.0)
    counter_8 = createCounter(657.0,521.0)

    button_image_7 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_8),
        relief="flat"
    )
    button_7.place(
        x=637.9375,
        y=519.9375,
        width=13.125,
        height=13.125
    )

    button_image_16 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_16 = Button(
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_8, stock_8),
        relief="flat"
    )
    button_16.place(
        x=671.9375,
        y=519.9375,
        width=13.125,
        height=13.125
    )

    button_image_26 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_26 = Button(
        image=button_image_26,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_8, title_8, description_8, price_8, product_imagen_8, stock_8)
    )
    button_26.place(
        x=697.0,
        y=517.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

try:
    product = products[8]
    stock_9 = product[4]
    product_imagen_9 = product[6]

    image_image_11 = PhotoImage(
    file=relative_to_assets("image_3.png"))
    image_11 = canvas.create_image(
        925.0,
        492.0,
        image=image_image_11
    )

    redimensionateImg(product[6])

    image_image_20 = PhotoImage(
    file=relative_to_images(product_imagen_9))
    image_20 = canvas.create_image(
        820.0,
        492.0,
        image=image_image_20
    )

    #Formateamos el numero para que tenga el punto de mil y no se vea el .0
    precioFormateado = formatPrice(product[5])

    title_9 = createTitle(product[1], 880.0, 448.0)
    description_9 = createDescription(f"{product[3]} (Quedan {stock_9} UND)", 880.0, 473.0)
    price_9 = createPrice(precioFormateado, 880.0, 513.0)
    counter_9 = createCounter(1015.0625, 519.0625)

    button_image_10 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: decreaseCounter(counter_9),
        relief="flat"
    )
    button_10.place(
        x=996.0,
        y=518.0,
        width=13.125,
        height=13.125
    )

    button_image_19 = PhotoImage(
    file=relative_to_assets("button_11.png"))
    button_19 = Button(
        image=button_image_19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: increaseCounter(counter_9, stock_9),
        relief="flat"
    )
    button_19.place(
        x=1030.0,
        y=518.0,
        width=13.125,
        height=13.125
    )

    button_image_24 = PhotoImage(
    file=relative_to_assets("button_20.png"))
    button_24 = Button(
        image=button_image_24,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: addProduct(counter_9, title_9, description_9, price_9, product_imagen_9, stock_9)
    )
    button_24.place(
        x=1052.0,
        y=514.0,
        width=20.0,
        height=20.0
    )

except IndexError:
    pass

window.resizable(False, False)
window.mainloop()