

# Importamos la libreria de playwright
from playwright.sync_api import Locator, Page



#Creamos nuestra clase


class Verificar:

    #Iniciamos constructor
    def __init__(self, page: Page):
        self.boton_checkOut: Locator = page.get_by_role("button", name="checkout")
        self.input_nombre: Locator = page.get_by_placeholder("First Name")
        self.input_apellido: Locator = page.get_by_placeholder("Last Name")
        self.input_cp: Locator = page.get_by_placeholder("Zip/Postal Code")

    #Defino mis metodos

    def selecciona_boton_cehckout(self) -> None:
        self.boton_checkOut.click()

    def ingresa_nombre(self,nombre: str) -> None:
        self.input_nombre.fill(nombre)

    def ingresa_apellido(self, apellido: str) -> None:
        self.input_apellido.fill(apellido)

    def ingresa_codigoPostal(self, cp: str) -> None:
        self.input_cp.fill(cp)