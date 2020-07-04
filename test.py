import unittest

import main

class TestStringMethods(unittest.TestCase):

    def _equals(self, arabic, roman):
        self.assertEqual(main.convert(arabic), roman)
    
    def _equalsList(self, l):
        for arabic, roman in l:
            self._equals(arabic, roman)

    def test_one(self):
        self._equals(1, 'I')
    
    def test_literals(self):
        pairs = [(k, v) for k,v in main.literal_map.items()]
        for arabic, roman in pairs:
            self._equals(arabic, roman)
    
    def test_two(self):
        self._equals(2, 'II')

    def test_three(self):
        self._equals(3, 'III')
    
    def test_twenty(self):
        self._equals(20, 'XX')

    def test_thirty(self):
        self._equals(30, 'XXX')
    
    def test_thirty(self):
        self._equals(30, 'XXX')
    
    def test_doubles_and_triples(self):
        self._equalsList([
            (200, 'CC'),
            (300, 'CCC'),
            (2000, 'MM'),
            (3000, 'MMM')
        ])
    
    def test_six(self):
        self._equals(6, 'VI')

    def test_eight(self):
        self._equals(8, 'VIII')

    def test_quotient_remainder(self):
        self._equalsList([
            (7, 'VII'),
            (11, 'XI'),
            (12, 'XII'),
            (13, 'XIII'),
            (15, 'XV'),
            (16, 'XVI'),
            (21, 'XXI'),
        ])
    
    def test_four(self):
        self._equals(4, 'IV')
    
    def test_nine(self):
        self._equals(9, 'IX')
    
    def test_fourteen(self):
        self._equals(14, 'XIV')

    def test_thirty_nine(self):
        self._equals(39, 'XXXIX')
    
    def test_forty(self):
        self._equals(40, 'XL')
    
    def test_forty_one(self):
        self._equals(41, 'XLI')
    
    def test_ninety(self):
        self._equals(90, 'XC')
        
    def test_ninety_one(self):
        self._equals(91, 'XCI')
    
    def test_eighty_eight(self):
        self._equals(88, 'LXXXVIII')
    
    def test_nineteen_hundred_and_three(self):
        self._equals(1903, 'MCMIII')

if __name__ == '__main__':
    unittest.main()