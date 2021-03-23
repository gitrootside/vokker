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

    def test_insert_new_data(self):
        datafile = 'test.vok'
        lection = Vokker(datafile)
        lection.open()
        lection.add_vok('Auto', 'car')
        translated = lection.get_vok_dict()
        self.assertIn('Auto', translated)
        print(translated['Auto'])


if __name__ == '__main__':
    unittest.main()
