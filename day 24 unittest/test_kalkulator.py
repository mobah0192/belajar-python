import unittest
from kalkulator import tambah ,kurang

class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        hasil = tambah(2, 3)
        self.assertEqual(hasil, 5)
        
    def test_tambah2(self):
            hasil2 = tambah(5, 5)
            self.assertEqual(hasil2, 10)
        
    def test_kurang(self):
        hasil_kurang = kurang(10,5)
        self.assertEqual(hasil_kurang ,5)
        
    def test_kurang2(self):
            hasil_kurang2 = kurang(15,5)
            self.assertEqual(hasil_kurang2 ,10)
    

unittest.main()