from random import randint
import unittest

from playwright.sync_api import sync_playwright


class TestMenuListar(unittest.TestCase):
    def test_listar_user(self):
        with sync_playwright() as playwright:
            navegador = playwright.chromium.launch(
                headless=False,
                slow_mo=1500
            )
            pagina = navegador.new_page()

            pagina.goto("http://127.0.0.1:5000/")
            pagina.locator("#menu-listar").click()
            self.assertEqual(pagina.url, 
                             "http://127.0.0.1:5000/listar")
            
            navegador.close()