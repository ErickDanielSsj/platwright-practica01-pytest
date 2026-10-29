from playwright.sync_api import Page, Locator


class AgregaProducto:
    def __init__(self, page : Page):
        self.page = page
        #Declaramos localizadores
        self.agrega_producto_Onesie: Locator = page.locator('[name="add-to-cart-sauce-labs-onesie"]')
        self.agregar_producto_bike: Locator = page.locator('[name="add-to-cart-sauce-labs-bike-light"]')
        self.icono_carrito: Locator = page.locator(".shopping_cart_link")
        self.button_check_out: Locator = page.get_by_role("button", name="checkout")

    def agregar_productoOnesie(self) -> None:
        self.agrega_producto_Onesie.click()

    def agregar_productoBike(self) -> None:
        self.agregar_producto_bike.click()


    def selecciona_icono_carrito(self) -> None:
        self.icono_carrito.click()