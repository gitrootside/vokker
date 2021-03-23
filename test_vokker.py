import unittest

from CLS.Vokker_cls import Vokker


class MyTestCase(unittest.TestCase):

    def test_init_instance(self):
        lection = Vokker('instance.vok')
        self.assertIsInstance(lection, Vokker)

    def test_create_new_datafile(self):
        datafile = 'test.vok'
        lection = Vokker(datafile)
        bool = lection.open()
        self.assertTrue(bool)

        # def test_something(self):
        #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
