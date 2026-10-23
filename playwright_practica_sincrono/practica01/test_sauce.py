from login_page import LoginPage
from menu_opciones import MenuOpciones
from ordenar_precios import OrdenarPrecios
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
        # assert precio_bajo == "$7.99", (f"❌ El ordenamiento falló, el precio fue: {precio_bajo}")
        # browser.close()

# if __name__ == "__main__":
#     ejecutar_prueba()