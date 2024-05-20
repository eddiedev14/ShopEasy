import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as mb
from datetime import datetime
import sqlite3
import sys
import ast
import subprocess
import json

cartProducts_str = sys.argv[1]
cedula = sys.argv[2]

# Convert the string to a list of dictionaries
cartProducts = ast.literal_eval(cartProducts_str)

# Obtener la ruta del directorio actual del script para abrir los demás archivos
script_dir = os.path.dirname(__file__)

# Obtenemos la ruta del archivo actual
CURRENT_DIR = Path(__file__).resolve().parent

# Definimos la parte relativa de la ruta en donde se encuentran los assets
RELATIVE_PATH = Path("../assets/shoppingCart")
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

window = Tk()

#Definimos dimensiones, nombre de la ventana, favicon y background-color
window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")

def createTitle(text, x, y):
    canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill="#1E1E1E",
        font=("Poppins Medium", 18 * -1)
    )

def createDescription(text, x, y):
    canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill="#1E1E1E",
        font=("Nunito Medium", 14 * -1)
    )

def createCounter(text, x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill="#393939",
        font=("Poppins SemiBold", 22 * -1)
    )

def createPrice(text, x, y):
    return canvas.create_text(
        x,
        y,
        anchor="nw",
        text="$"+str(text),
        fill="#393939",
        font=("Poppins Medium", 14 * -1)
    )

def openCatalog():
    # Construir la ruta al archivo userDashboard.py
    dashboard_path = os.path.join(script_dir, "userDashboard.py")
    # Convert the list of dictionaries to a string
    cartProducts_str = json.dumps(cartProducts)
    #Se pasa como parametro la cedula para obtener el nombre
    subprocess.Popen(['python', dashboard_path, cedula, cartProducts_str])
    sys.exit(0)

def calculateTotal(subtotalText, ivaText, totalText):
    subtotalAcumulator = 0

    #Recorremos los productos y actualizamos el acumulador
    for i in cartProducts:
        subtotalIndividual = int(i["Subtotal"])
        subtotalAcumulator += subtotalIndividual

    #Calculamos el iva y el total a pagar
    iva = round(subtotalAcumulator * 0.19)
    total = round(subtotalAcumulator + iva)

    #Actualizamos el texto del elemento
    canvas.itemconfig(subtotalText, text=f"Subtotal: ${subtotalAcumulator}")
    canvas.itemconfig(ivaText, text=f"Iva: ${iva}")
    canvas.itemconfig(totalText, text=f"Total: ${total}")

def updateProduct(product, action, counter, individualSubtotal, subtotalText, ivaText, totalText):
    #Obtenemos el valor de la cantidad y la actualizamos dependiendo de la acción
    quantity = int(product["Cantidad"])
    stock = int(product["Stock"])
    precioUnitario = int(product["Precio Unitario"])

    if quantity >= 0 and quantity < stock and action == "sum":
        quantity += 1
    elif quantity > 1 and quantity <= stock and action == "minus":
        quantity -= 1

    #Actualizamos el texto de la ventana
    canvas.itemconfig(counter, text=str(quantity))

    #Obtenemos el indice del objeto para actualizarlo
    index = cartProducts.index(product)

    #Calculamos el subtotal individual
    individualSubtotalValue = precioUnitario * quantity
    canvas.itemconfig(individualSubtotal, text=f"${str(individualSubtotalValue)}")

    #Actualizamos la variable cantidad y el producto del carrito
    product["Cantidad"] = quantity
    product["Subtotal"] = individualSubtotalValue
    cartProducts[index] = product

    calculateTotal(subtotalText, ivaText, totalText)

def buyShoppingCart(totalText):
    #Validamos que hayan productos en el carrito
    if len(cartProducts) > 0:
        #Validamos de que la venta quiera realizarse
        answer = mb.askquestion(title="Confirmación de Compra", message="¿Desea efectuar la compra de su carrito?")

        if answer == "yes":
            #Para la venta se necesita el nombre del usuario, total a pagar, fecha y la lista de los productos 
            
            #Obtenemos el nombre a partir de la cedula
            db = sqlite3.connect('shopeasy.db')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE cedula=? AND tipo=?", (cedula, "Usuario"))
            user = cursor.fetchone()
            #Retornamos el nombre del usuario que tenga esa cedula
            username = user[1]

            #Obtenemos los demás elementos
            shoppingCartTotal = canvas.itemcget(totalText, 'text')
            shoppingCartTotal = shoppingCartTotal[7:]

            # Obtener la fecha y hora actual
            actualDate = datetime.now()

            # Formatear la fecha y hora en el formato deseado
            formattedDate = actualDate.strftime("%d/%m/%Y %H:%M")

            sale = {
                "Usuario": username,
                "Total": shoppingCartTotal,
                "Fecha": formattedDate,
                "Productos": cartProducts
            }

            # Convertir el diccionario a una cadena JSON
            sale_str = json.dumps(sale)
            cart_str = json.dumps(cartProducts)

            #Antes de enviar al usuario a invoice.py se debe de efectuar los cambios en el inventario especificamente en la cantidad
            for i in cartProducts:
                productName = i["Nombre"]
                productUnitaryPrice = float(i["Precio Unitario"])
                productStock = i["Stock"]
                productImage = i["Imagen"]
                newStock = productStock-i["Cantidad"]

                #Hacemos un update a la cantidad
                db = sqlite3.connect('shopeasy.db')
                cursor = db.cursor()
                cursor.execute("UPDATE productos SET stock = ? WHERE nombre=? AND stock=? AND precio=? AND imagen=?", (newStock, productName, productStock, productUnitaryPrice, productImage))
                db.commit()

            # Construir la ruta al archivo invoice.py
            invoice_path = os.path.join(script_dir, "invoice.py")
            #Se pasa como parametro la venta y el carrito vació
            subprocess.Popen(['python', invoice_path, sale_str, "[]", cedula])

            sys.exit(0)
        else:
            return
    else:
        mb.showerror(title="Error", message="Todavía no se ha agregado ningun producto al carrito de compras")
    
def deleteProduct(product):
    #Validamos que se quiera eliminar
    answer = mb.askquestion(title="Eliminar Producto", message="¿Desea eliminar el producto de su carrito?")

    if answer == "yes":
        #Encontramos el indice y lo eliminamos
        index = cartProducts.index(product)
        cartProducts.pop(index)

        #Cerramos el archivo y lo volvemos a abrir
        shopping_cart_path = os.path.join(script_dir, "shoppingCart.py")
        
        # Convert the list of dictionaries to a string
        cartProducts_str = json.dumps(cartProducts)

        subprocess.Popen(['python', shopping_cart_path, cartProducts_str, cedula])
        sys.exit(0)
    else:
        return

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

subtotal_text = canvas.create_text(
    732.0,
    247.0,
    anchor="nw",
    text="Subtotal: $0",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

iva_text = canvas.create_text(
    732.0,
    287.0,
    anchor="nw",
    text="IVA: $0",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

total_text = canvas.create_text(
    732.0,
    327.0,
    anchor="nw",
    text="Total: $0",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1)
)

calculateTotal(subtotal_text, iva_text, total_text)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: buyShoppingCart(total_text),
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
    command=openCatalog,
    relief="flat"
)
button_11.place(
    x=994.0,
    y=81.0,
    width=31.0,
    height=31.0
)

try:
    product_1 = cartProducts[0]
    imagePath_1 = product_1["Imagen"]
    title_1 = product_1["Nombre"]
    quantity_1 = product_1["Cantidad"]
    description_1 = product_1["Descripcion"]
    price_1 = product_1["Subtotal"]

    image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        354.0,
        219.0,
        image=image_image_2
    )

    button_image_15 = PhotoImage(
    file=relative_to_assets("image_6.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: deleteProduct(product_1),
        relief="flat"
    )
    button_15.place(
        x=605.0,
        y=210.0,
    )

    image_image_10 = PhotoImage(
    file=relative_to_images(imagePath_1))
    image_10 = canvas.create_image(
        100.0,
        219.0,
        image=image_image_10
    )

    createTitle(title_1, 154.0, 194.0)
    createDescription(description_1, 154.0, 224.0)
    counter_1 = createCounter(quantity_1, 432.0, 211.0)
    individual_subtotal_1 = createPrice(price_1, 499.0, 211.0)

    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_1, "sum", counter_1, individual_subtotal_1, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_1.place(
        x=455.0,
        y=213.0,
        width=12.0,
        height=6.0
    )

    button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_1, "minus", counter_1, individual_subtotal_1, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_5.place(
        x=455.0,
        y=225.0,
        width=12.0,
        height=6.0
    )

except IndexError:
    pass

try:
    product_2 = cartProducts[1]
    imagePath_2 = product_2["Imagen"]
    title_2 = product_2["Nombre"]
    quantity_2 = product_2["Cantidad"]
    description_2 = product_2["Descripcion"]
    price_2 = product_2["Subtotal"]

    image_image_3 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_3 = canvas.create_image(
        354.0,
        344.0,
        image=image_image_3
    )

    button_image_16 = PhotoImage(
    file=relative_to_assets("image_6.png"))
    button_16 = Button(
        image=button_image_16,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: deleteProduct(product_2),
        relief="flat"
    )
    button_16.place(
        x=605.0,
        y=335.0,
    )

    image_image_11 = PhotoImage(
    file=relative_to_images(imagePath_2))
    image_11 = canvas.create_image(
        100.0,
        344.0,
        image=image_image_11
    )

    createTitle(title_2, 154.0, 319.0)
    createDescription(description_2, 154.0, 349.0)
    counter_2 = createCounter(quantity_2, 432.0, 336.0)
    individual_subtotal_2 = createPrice(price_2, 499.0, 336.0)

    button_image_2 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_2, "sum", counter_2, individual_subtotal_2, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_2.place(
        x=455.0,
        y=338.0,
        width=12.0,
        height=6.0
    )

    button_image_6 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_2, "minus", counter_2, individual_subtotal_2, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_6.place(
        x=455.0,
        y=350.0,
        width=12.0,
        height=6.0
    )
except IndexError:
    pass

try:
    product_3 = cartProducts[2]
    imagePath_3 = product_3["Imagen"]
    title_3 = product_3["Nombre"]
    quantity_3 = product_3["Cantidad"]
    description_3 = product_3["Descripcion"]
    price_3 = product_3["Subtotal"]

    image_image_4 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_4 = canvas.create_image(
        354.0,
        469.0,
        image=image_image_4
    )

    button_image_17 = PhotoImage(
    file=relative_to_assets("image_6.png"))
    button_17 = Button(
        image=button_image_17,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: deleteProduct(product_3),
        relief="flat"
    )
    button_17.place(
        x=605.0,
        y=460.0,
    )

    image_image_12 = PhotoImage(
    file=relative_to_images(imagePath_3))
    image_12 = canvas.create_image(
        100.0,
        469.0,
        image=image_image_12
    )

    createTitle(title_3, 154.0, 444.0)
    createDescription(description_3, 154.0, 474.0)
    counter_3 = createCounter(quantity_3, 432.0, 461.0)
    individual_subtotal_3 = createPrice(price_3, 499.0, 461.0)

    button_image_3 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_3, "sum", counter_3, individual_subtotal_3, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_3.place(
        x=455.0,
        y=463.0,
        width=12.0,
        height=6.0
    )

    button_image_7 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_3, "minus", counter_3, individual_subtotal_3, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_7.place(
        x=455.0,
        y=475.0,
        width=12.0,
        height=6.0
    )
except IndexError:
    pass

try:
    product_4 = cartProducts[3]
    imagePath_4 = product_4["Imagen"]
    title_4 = product_4["Nombre"]
    quantity_4 = product_4["Cantidad"]
    description_4 = product_4["Descripcion"]
    price_4 = product_4["Subtotal"]

    image_image_5 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_5 = canvas.create_image(
        354.0,
        594.0,
        image=image_image_5
    )

    button_image_18 = PhotoImage(
    file=relative_to_assets("image_6.png"))
    button_18 = Button(
        image=button_image_18,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: deleteProduct(product_4),
        relief="flat"
    )
    button_18.place(
        x=605.0,
        y=585.0,
    )

    image_image_13 = PhotoImage(
    file=relative_to_images(imagePath_3))
    image_13 = canvas.create_image(
        100.0,
        594.0,
        image=image_image_13
    )

    createTitle(title_4, 154.0, 569.0)
    createDescription(description_4, 154.0, 599.0)
    counter_4 = createCounter(quantity_4, 432.0, 586.0)
    individual_subtotal_4 = createPrice(price_4, 499.0, 586.0)

    button_image_4 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command= updateProduct(product_4, "sum", counter_4, individual_subtotal_4, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_4.place(
        x=455.0,
        y=588.0,
        width=12.0,
        height=6.0
    )

    button_image_8 = PhotoImage(
    file=relative_to_assets("button_5.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: updateProduct(product_4, "minus", counter_4, individual_subtotal_4, subtotal_text, iva_text, total_text), #Usamos lambda para poder pasar el argumento
        relief="flat"
    )
    button_8.place(
        x=455.0,
        y=600.0,
        width=12.0,
        height=6.0
    )
except IndexError:
    pass

window.resizable(False, False)
window.mainloop()
