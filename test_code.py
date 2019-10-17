import unittest
from class_change import enPiT as eP

class enPitTest(unittest.TestCase):

    def setup(self):
        #開始処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_read_sales(self):
        self.assertEqual('4200', eP.read_sales(self)) 
    
    def test_soldout(self):
        self.assertAlmostEqual(True, eP.soldout(self,0))

    def test_soldout2(self):
        self.assertAlmostEqual(False, eP.soldout(self,1))

    def test_read_stock(self):
        self.assertAlmostEqual("ヘルシーバーガー🍔",eP.read_stock(self))

if __name__ == "__main__":
    unittest.main()