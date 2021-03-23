import unittest
from CLS.vokker_cls import vokker


class MyTestCase(unittest.TestCase):

    def test_init_instance(self):
        
        lection=vokker('instance.vok')


    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
