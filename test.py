import unittest
from main import search_for_patterns


class TestData(unittest.TestCase):
    def test_rabin_algo1(self):
        pattern = "LMN"
        text = "QLMNOP"
        self.assertEqual(search_for_patterns(text, pattern), [1])

    def test_rabin_algo2(self):
        pattern = "amor"
        text = "Benefactor more ipsule ti camo comendante, mui viera, vamonos, mui amor"
        self.assertEqual(search_for_patterns(text, pattern), [67])

    def test_rabin_algo3(self):
        pattern = "happiness"
        text = "there is nothing that reminds me about being happy"
        self.assertEqual(search_for_patterns(text, pattern), [])

    def test_rabin_algo4(self):
        pattern = "punk"
        text = "not quite yet p u n k"
        self.assertEqual(search_for_patterns(text, pattern), [])

    def test_rabin_algo5(self):
        pattern = "Lock"
        text = "what about CAPSLOCKING"
        self.assertEqual(search_for_patterns(text, pattern), [])

    def test_rabin_algo6(self):
        pattern = "MENIN"
        text = "Lorem ipsum dolor sit amet,MENIN consectetur adipiscing elit, sed do eiusmod tempor MENINincididunt ut labore et dolore magna aliqua. Scelerisque viverra mauris in aliquam sem fringilla. Imperdiet proin fermentum leo vel orci porta non. Arcu dui vivamus arcu felis bibendum ut tristique. Eu turpis egestas pretium aenean. Commodo elit at imperdiet dui accumsan sit. Sit amet consectetur adipiscing elit duis. Tempor commodo ullamcorper a lacus vestibulum sed. Sed augue lacus viverra vitae congue eu consequat ac. Id ornare arcu odio ut sem nulla pharetra. Est ante in nibh mauris cursus mattis molestie a iaculis. Auctor urna nunc id cursus metus aliquam. Orci dapibus ultrices in iaculis. Facilisi nullam vehicula ipsum a arcu cursus vitae. MENIN"
        self.assertEqual(search_for_patterns(text, pattern), [27, 84, 743])

    def test_rabin_algo7(self):
        pattern = "A"
        text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        self.assertEqual(search_for_patterns(text, pattern), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])