
from pathlib import Path
import unittest

class TestDevFlowStore(unittest.TestCase):
    def test_pagina_existe(self):
        self.assertTrue(Path("index.html").exists())

    def test_pagina_tem_titulo(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn("DevFlow Store", html)

    def test_botao_comprar_existe(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn('id="comprar"', html)

    def test_arquivos_de_estilo_e_script_existem(self):
        self.assertTrue(Path("style.css").exists())
        self.assertTrue(Path("script.js").exists())

    def test_mensagem_do_carrinho(self):
        js = Path("script.js").read_text(encoding="utf-8")
        self.assertIn("Produto adicionado ao carrinho!", js)

if __name__ == "__main__":
    unittest.main()
