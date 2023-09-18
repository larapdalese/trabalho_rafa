import unittest
import module as ut

class numero_de_dias_entre_datas(unittest.TestCase):
    def teste(self):
        self.assertEqual(ut.numero_de_dias_entre_datas("22 de novembro de 2020","25 de novembro de 2020"), 3)
    def teste_data_negativa(self):
        self.assertEqual(ut.numero_de_dias_entre_datas("-22 de novembro de 2020","22 de novembro de 2020"), "digite uma data válida")
        
if __name__ == "__main__":
    unittest.main()
