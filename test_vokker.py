import unittest

from CLS.Vokker import Vokker


class MyTestCase(unittest.TestCase):

    def test_init_instance(self):
        lection = Vokker()
        self.assertIsInstance(lection, Vokker)

    def test_create_new_datafile(self):
        datafile = 'test.vok'
        lection = Vokker()

        bool = lection.open(datafile)
        self.assertTrue(bool)

        lection.close()

    # def test_insert_new_data(self):
    #     datafile = 'test.vok'
    #     lection = Vokker()
    #
    #     lection.add('Auto', 'car')
    #     lection.add('Musik', 'music')
    #     translated = lection.get_vok_dict()
    #
    #     self.assertIn('Musik', translated)

    # def test_write_vok(self):
    #     datafile = 'test.vok'
    #     lection = Vokker()
    #     lection.open(datafile, "w")
    #     lection.add('Auto', 'car')
    #     lection.add('Baum', 'tree')
    #     lection.write()
    #
    #     lection.close()

    def test_read_vok(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection.open(datafile)
        lection.read()
        lection.close()

    def test_open_nonexistent_file_failed(self):
        datafile = 'not_existing_file.vok'
        lection = Vokker()
        rt = lection.open(datafile)
        self.assertFalse(rt, 'try to open a non existing file!!!')

    def test_open_if_safelock_is_true_failed(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection._safelock_ = True
        rt = lection.open(datafile)

        self.assertFalse(rt, "File opened, but safelock is True")

    def test_open_if_vok_new_data_not_empty_failed(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection._vok_new_data_ = ""
        rt = lection.open(datafile)
        self.assertFalse(rt, "still unsaved data in new_data")

    def test_close_non_opened_file_failed(self):
        l = Vokker()
        l._safelock_ = True
        rt = l.close()
        self.assertFalse(rt, "unable to close non-opened file!!! ")

    def test_close_if_safelock_is_true_failed(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection.open(datafile)
        lection._safelock_ = True
        rt = lection.close()
        self.assertFalse(rt, "safelock is activ")

    def test_close_if_vok_new_data_not_empty_failed(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection.open(datafile)
        lection._vok_new_data_ = dict()
        lection._vok_new_data_['Auto'] = 'car'

        rt = lection.close()
        self.assertFalse(rt, "still unsaved data in new_data")

    def test_read_non_exist_file_failed(self):
        v = Vokker()
        rt = v.read()
        self.assertFalse(rt, "read not existing file!!!")


if __name__ == '__main__':
    unittest.main()
