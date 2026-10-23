#Se importa la libreria de playwright
from playwright.sync_api import Locator, Page


#Se crea la clase
class OrdenarPrecios:
    def __init__(self, page: Page):
        self.icono_filtro: Locator = page.get_by_role("combobox")
        self.obtiene_precio: Locator = page.locator('.inventory_item_price')

    def seleccionaFiltro(self) -> None:
        self.icono_filtro.select_option('lohi')

    #Aqui se puede el tipo de dato string
    def obtienePrecios(self) -> str:
        # Devuelve el texto del primer producto de la lista (ej: "$7.99")
        return self.obtiene_precio.first.inner_text()
        