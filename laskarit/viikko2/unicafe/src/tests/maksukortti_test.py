import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_rahan_ottaminen_vahentaa_saldoa_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")        
        
    def test_rahan_ottaminen_ei_muuta_saldoa_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")        
        
    def test_rahan_ottaminen_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        riittaa = self.maksukortti.ota_rahaa(5)
        self.assertEqual(riittaa, True)        

    def test_rahan_ottaminen_palauttaa_false_jos_rahaa_ei_ole_tarpeeksi(self):
        ei_riita = self.maksukortti.ota_rahaa(20)
        self.assertEqual(ei_riita, False)       

    
