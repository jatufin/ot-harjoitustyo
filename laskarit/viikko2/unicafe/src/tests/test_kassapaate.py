import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myydyt_edulliset_on_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_luodun_kassapaatteen_myydyt_maukkaat_on_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)        

    def test_kateisella_edullisesti_kassa_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_kateisella_maukkaasti_kassa_kasvaa_oikein(self):        
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_edullisesti_vaihtoraha_on_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        
    def test_kateisella_maukkaasti_vaihtoraha_on_oikein(self):        
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)        

    def test_kateisella_myytyjen_edullisten_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_myytyjen_maukkaiden_lounaiden_maara_kasvaa_oikein(self):        
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisella_edullisesti_jos_ei_tarpeeksi_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisella_maukkaasti_jos_ei_tarpeeksi_rahamaara_ei_muutu(self):        
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_edullisesti_jos_ei_tarpeeksi_palautetaan_oikein(self):
        kateinen = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(vaihtoraha, kateinen)

    def test_kateisella_maukkaasti_jos_ei_tarpeeksi_palautetaan_oikein(self):        
        kateinen = 300
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(vaihtoraha, kateinen)
        
    def test_kateisella_edullisesti_jos_ei_tarpeeksi_myytyjen_maara_ei_muutu(self):        
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisella_maukkaasti_jos_ei_tarpeeksi_myytyjen_maara_ei_muutu(self):   
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)        
        

    def test_kortilla_edullisesti_jos_tarpeeksi_veloitetaan_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_kortilla_edullisesti_jos_tarpeeksi_palautetaan_true(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)

    def test_kortilla_maukkaasti_jos_tarpeeksi_veloitetaan_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_kortilla_maukkaasti_jos_tarpeeksi_palautetaan_true(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(tulos, True)
        
    def test_kortilla_myytyjen_edullisten_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_myytyjen_maukkaiden_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)        

    def test_kortilla_edullisesti_jos_ei_tarpeeksi_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        # saldo on nyt 200
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)        
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kortilla_maukkaastiedullisesti_jos_ei_tarpeeksi_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        # saldo on nyt 200
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)        
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_kortilla_edullisesti_jos_ei_tarpeeksi_palautetaa_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        # saldo on nyt 200
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)        
        self.assertEqual(tulos, False)

    def test_kortilla_maukkaasti_jos_ei_tarpeeksi_palautetaa_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        # saldo on nyt 200
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)        
        self.assertEqual(tulos, False)        

    def test_kortilla_edullisesti_jos_ei_tarpeeksi_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        # saldo on nyt 200
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)        
        self.assertEqual(self.kassapaate.edulliset, 0)        

    def test_kortilla_maukkaasti_jos_ei_tarpeeksi_myytyjen_maara_ei_muutu(self):        
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)        
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        # saldo on nyt 250
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)        
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_ostettaessa_edullisesti_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_ostettaessa_maukkaasti_rahamaara_ei_muutu(self):        
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttia_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_korttia_ladattaessa_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortin_lataaminen_negatiivisella_summalla_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)        
