
from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page: Page):
        self.page = page
        #declaro mis localizadore
        self.ingresa_user = page.get_by_placeholder("Username")
        self.ingresa_password = page.get_by_placeholder("Password")
        self.boton_login = page.get_by_role("button", name="Login")

    def ingresar_usuario(self,usuario: str):
        self.ingresa_user.fill(usuario)

    def ingresar_password(self,password: str):
        self.ingresa_password.fill(password)

    def selecciona_boton_Ingresar(self):
        self.boton_login.click()

    def inicia_sesion(self, usuario: str, password: str):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.selecciona_boton_Ingresar()

