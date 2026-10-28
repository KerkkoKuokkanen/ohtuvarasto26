import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-10, -10)
        self.varasto3 = Varasto(5, 10)
        self.varasto4 = Varasto(10, 5)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktio_luo_negatiivisen_varaston_tilavuus(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_konstruktio_luo_negatiivisen_varaston_saldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktio_saldo_enemmän_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_muuta_määrä_negatiivinen(self):
        self.varasto4.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto4.saldo, 5)

    def test_muuta_määrä_suuri(self):
        self.varasto4.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto4.saldo, 10)

    def test_ota_negatiivinen_varastosta(self):
        ret = self.varasto4.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto4.saldo, 5)
        self.assertAlmostEqual(ret, 0)

    def test_ota_varastosta_liikaa(self):
        ret = self.varasto4.ota_varastosta(100)
        self.assertAlmostEqual(self.varasto4.saldo, 0)
        self.assertAlmostEqual(ret, 5)
        
    def test_varasto_pring(self):
        s = str(self.varasto4)
        self.assertEqual(s, "saldo = 5, vielä tilaa 5")

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
