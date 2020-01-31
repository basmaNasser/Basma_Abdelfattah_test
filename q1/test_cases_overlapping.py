import unittest
from overlapping import overlapping


class testCases(unittest.TestCase):

    def test1(self):
        results = overlapping((1,5),(2,6))
        
        self.assertEqual(results,"overlapping")

    def test2(self):
        results = overlapping((1,5),(6,8))
        
        self.assertEqual(results,"no overlapping")

    def test3(self):
      
        results = overlapping((1,5),(8,6))
        
        self.assertEqual(results,"no overlapping")

            
    def test4(self):
        results = overlapping((3,5),(3,10))
        
        self.assertEqual(results,"overlapping")

    def test5(self):
        results = overlapping((1,2),(0,4))
        
        self.assertEqual(results,"no overlapping")
        
    def test6(self):
        results = overlapping((1,2),(0,1.5))
        
        self.assertEqual(results,"overlapping")
        
    def test7(self):
        results = overlapping((-1,-5),(-3,-6))
        
        self.assertEqual(results,"overlapping")
        
    def test8(self):
        results = overlapping((-1,2),(0,-2))
        
        self.assertEqual(results,"overlapping")
        
    def test9(self):
        results = overlapping((-1,-3),(1,3))
        
        self.assertEqual(results,"no overlapping")
        
    def test10(self):
        results = overlapping((5,5),(5,5))
        
        self.assertEqual(results,"overlapping")

# main method
if __name__ == '__main__':
    unittest.main()
