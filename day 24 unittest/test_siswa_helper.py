import unittest
from siswa_helper import cek_lulus

class TestSiswa (unittest.TestCase):
    def test_nilai_80_lulus(self):
        lulus  = cek_lulus(80)
        self.assertEqual(lulus,"Lulus")
        
        
    def test_nilai_60_tidak_lulus(self):
        lulus2 = cek_lulus(60)
        self.assertEqual(lulus2, "Tidak lulus")
unittest.main()