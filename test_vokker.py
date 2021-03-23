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

        lection.close()

    def test_insert_new_data(self):
        datafile = 'test.vok'
        lection = Vokker(datafile)

        lection.add('Auto', 'car')
        lection.add('Musik', 'music')
        translated = lection.get_vok_dict()

        self.assertIn('Musik', translated)


    def test_write_vok(self):
        datafile = 'test.vok'
        lection = Vokker(datafile)
        lection.open("w")
        lection.add('Auto', 'car')
        lection.add('Baum', 'tree')
        lection.write()

        lection.close()


    def test_read_vok(self):
        datafile = 'test.vok'
        lection = Vokker(datafile)
        lection.open()
        lection.read()
        lection.close()


if __name__ == '__main__':
    unittest.main()
