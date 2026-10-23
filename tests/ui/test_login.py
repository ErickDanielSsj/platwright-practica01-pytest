from playwright.sync_api import Page, expect
from pages.login_page import LoginPage



def test_login(page:Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user",
        "secret_sauce")
    expect(page.locator(".title")).to_have_text("Products")