import unittest
from senha import gerar_senha

class TestGeradorSenha(unittest.TestCase):

    def test_tamanho_senha(self):
        senha = gerar_senha(12)
        self.assertEqual(len(senha), 12)

    def test_sem_numeros(self):
        senha = gerar_senha(10, usar_numeros=False)
        self.assertFalse(any(char.isdigit() for char in senha))

    def test_com_numeros(self):
        senha = gerar_senha(10, usar_numeros=True)
        self.assertTrue(any(char.isdigit() for char in senha))

    def test_sem_simbolos(self):
        senha = gerar_senha(10, usar_simbolos=False)
        self.assertFalse(any(not char.isalnum() for char in senha))

    def test_senha_diferente(self):
        senha1 = gerar_senha(10)
        senha2 = gerar_senha(10)
        self.assertNotEqual(senha1, senha2)

if __name__ == "__main__":
    unittest.main()