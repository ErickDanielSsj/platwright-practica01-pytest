#Se realiza la importacion de la libreria de playwright
from playwright.sync_api import Locator, Page

#Se crea la clase
class MenuOpciones:
    def __init__(self, page: Page):
        self.page = page
        self.menu_opciones_btn: Locator = page.get_by_role("button", name="Open Menu")
        self.opcion_logout: Locator = page.locator('#logout_sidebar_link')

    def abrir_menu_opciones(self) -> None:
        self.menu_opciones_btn.click()

    # def opcion_logout_visible(self)-> bool:
    #     self.opcion_logout.wait_for(state='visible')
    #     return self.opcion_logout.is_visible()
