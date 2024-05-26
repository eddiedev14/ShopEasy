import sqlite3
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as mb
import subprocess
import sys

script_dir = os.path.dirname(__file__)

CURRENT_DIR = Path(__file__).resolve().parent

RELATIVE_PATH = Path("../assets/adminLogin")

ASSETS_PATH = CURRENT_DIR / RELATIVE_PATH

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1137x639")
window.title("ShopEasy")
window.iconbitmap('assets/main/shopEasyLogo.ico')
window.configure(bg = "#FFFFFF")

def validateLogin():
    cedula = cedulaEntry.get()
    password = passwordEntry.get()

    if cedula == "" and password == "":
        mb.showerror(title="Ha ocurrido un error", message="Rellena todos los campos del formulario")
    else:
        db = sqlite3.connect('shopeasy.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE cedula=? AND contraseña=? AND tipo=?", (cedula, password, "Admin"))
        user = cursor.fetchone()
        
        if user == None:
            mb.showerror(title="Usuario no encontrado", message="Los datos que se ingresaron no coinciden con ningun usuario en la base de datos")
        else:                
            user_login_path = os.path.join(script_dir, "../admin/adminDashboard.py")
            subprocess.Popen(['python', user_login_path, cedula])
            sys.exit(0)

def userLogin():
    user_login_path = os.path.join(script_dir, "userLogin.py")
    subprocess.Popen(['python', user_login_path])
    sys.exit(0)

def userRegister():
    user_login_path = os.path.join(script_dir, "userRegister.py")
    subprocess.Popen(['python', user_login_path])
    sys.exit(0)
        
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
canvas.create_rectangle(
    0.0,
    0.0,
    1137.0,
    263.0,
    fill="#0089EC",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    789.0,
    333.0,
    image=image_image_1
)

loginClientButton = Button(
    text="Iniciar sesión como Cliente",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    foreground="#0089ED",
    background="#fff",
    command=userLogin
)

loginClientButton.place(
    x=599.0,
    y=522.0,
)

registerClientButton = Button(
    text="Crear cuenta como Cliente",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    foreground="#0089ED",
    background="#fff",
    command=userRegister
)

registerClientButton.place(
    x=599.0,
    y=547.0,
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validateLogin,
    relief="flat"
)
button_1.place(
    x=599.0,
    y=458.0,
    width=382.0,
    height=54.0
)

canvas.create_text(
    599.0,
    220.0,
    anchor="nw",
    text="Ingresa tu Cédula",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

canvas.create_text(
    598.0,
    336.0,
    anchor="nw",
    text="Ingresa tu Contraseña",
    fill="#000000",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    790.0,
    279.5,
    image=entry_image_1
)
cedulaEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
cedulaEntry.place(
    x=608.0,
    y=257.0,
    width=364.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    789.0,
    395.5,
    image=entry_image_2
)
passwordEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    show="*",
    fg="#000716",
    highlightthickness=0
)
passwordEntry.place(
    x=607.0,
    y=373.0,
    width=364.0,
    height=43.0
)

canvas.create_text(
    599.0,
    131.0,
    anchor="nw",
    text="Login (Gerente)",
    fill="#000000",
    font=("Poppins Medium", 45 * -1)
)

canvas.create_text(
    599.0,
    99.0,
    anchor="nw",
    text="Bienvenido a ShopEasy",
    fill="#000000",
    font=("Roboto Regular", 21 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    208.0,
    68.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    283.0,
    308.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()