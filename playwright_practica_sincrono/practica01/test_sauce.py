from login_page import LoginPage
from menu_opciones import MenuOpciones
from ordenar_precios import OrdenarPrecios
from agrega_producto_carrito import AgregaProducto
from verificar import Verificar
# from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect


def test_ejecutar_prueba(page: Page):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        #Se importa metodo de la clase LoginPage
        iniciar_sesion = LoginPage(page)
        iniciar_sesion.inicia_sesion("standard_user", "secret_sauce")
        #Se impota el metodo de la clase menuopciones
        menu_opciones = MenuOpciones(page)
        menu_opciones.abrir_menu_opciones()

        # assert menu_opciones.opcion_logout_visible(),('La prueba falla') ## SE REMPLAZA VALIDACION
        expect(menu_opciones.opcion_logout).to_be_visible()
        print('La prueba paso')
        page.screenshot(path="menu.png")
        print('Seleccionara el filtro de precio')

        #Se importa metodo del menu ordenas precios
        filtroPrecios = OrdenarPrecios(page)
        filtroPrecios.seleccionaFiltro()
        page.screenshot(path='filtro.png')

        #Verificacion de precio 
        precio_bajo = filtroPrecios.obtienePrecios()
        print(f"💰 El primer producto ahora cuesta: {precio_bajo}")
        expect(filtroPrecios.obtiene_precio.first).to_have_text("$7.99")
        page.screenshot(path='precios.png')
        # assert precio_bajo == "$7.99", (f"❌ El ordenamiento falló, el precio fue: {precio_bajo}")
        # browser.close()

        # crea el ojeto de la nueva clase de tipo agregar producto
        agregaProducto = AgregaProducto(page)
        #Invoca metodo agregar producto
        agregaProducto.agregar_productoOnesie()
        page.screenshot(path='agrega_producto.png')
        agregaProducto.agregar_productoBike()
        page.screenshot(path='agrega_productoBike.png')
        agregaProducto.selecciona_icono_carrito()
        page.screenshot(path="icono_carrito.png")
        page.wait_for_timeout(1000)
        #Se importa la clase verificar y se crea el objeto
        verificar = Verificar(page)
        #Se invican los metodos de la clase
        verificar.selecciona_boton_cehckout()
        page.screenshot(path="boton.png")
        verificar.ingresa_nombre("Erick")
        verificar.ingresa_apellido("Vera")
        verificar.ingresa_codigoPostal("55450")


# if __name__ == "__main__":
#     ejecutar_prueba()