import unittest

from CLS.Vokker import Vokker
from CLS.VokkerConsole import VokkerConsole


class MyTestCase(unittest.TestCase):
    vokker = Vokker('test.vok')

    def test_console_shows_menue(self):
        self.vokker.open()
        self.vokker.read()

        cons = VokkerConsole(self.vokker)
        cons.show_menu()

if __name__ == '__main__':
    unittest.main()
