import unittest

from CLS.Vokker import Vokker


class MyTestCase(unittest.TestCase):

    def test_init_instance(self):
        lection = Vokker()
        self.assertIsInstance(lection, Vokker)

    def test_create_new_datafile(self):
        datafile = 'test.vok'
        lection = Vokker()

        bo = lection.open(datafile)
        self.assertTrue(bo)

        lection.close()

    # Vokker.open

    def test_open_existing_file(self):
        datafile = 'test.vok'
        lection = Vokker()
        rt = lection.open(datafile)
        self.assertTrue(rt)
        lection.close()

    def test_open_FAIL_nonexistent_file_failed(self):
        datafile = 'not_existing_file.vok'
        lection = Vokker()
        rt = lection.open(datafile)
        self.assertFalse(rt, 'try to open a non existing file!!!')

    def test_open_FAIL_if_safelock_is_true(self):
        datafile = 'test.vok'
        lec = Vokker()
        lec._safelock_ = True
        rt = lec.open(datafile)

        self.assertFalse(rt, "File opened, but safelock is True")
        lec.close()

    def test_open_FAIL_if_vok_new_data_not_empty(self):
        datafile = 'test.vok'
        lec = Vokker()
        lec._vok_new_data_ = ""
        rt = lec.open(datafile)
        self.assertFalse(rt, "still unsaved data in new_data")
        lec.close()

    # Vokker.close
    def test_close_FAIL_if_non_opened_file(self):
        l = Vokker()
        l._safelock_ = True
        rt = l.close()
        self.assertFalse(rt, "unable to close non-opened file!!! ")

    def test_close_FAIL_if_safelock_is_true(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection.open(datafile)
        lection._safelock_ = True
        rt = lection.close()
        self.assertFalse(rt, "safelock is activ")
        lection._file_handle_.close()

    def test_close_FAIL_if_vok_new_data_not_empty(self):
        datafile = 'test.vok'
        lection = Vokker()
        lection.open(datafile)
        lection._vok_new_data_ = dict()
        lection._vok_new_data_['Auto'] = 'car'

        rt = lection._file_handle_.close()
        self.assertFalse(rt, "still unsaved data in new_data")

    # Vokker.fileexist()
    def test_fileexist(self):
        file = "normal.vok"
        lec = Vokker()
        rt = lec.fileexist(file)
        self.assertTrue(rt)

    def test_fileexist_FAIL_non_existing_file(self):
        file = "non_existin_file.vok.vok"
        lec = Vokker()
        rt = lec.fileexist(file)
        self.assertFalse(rt)

    # Vokker.read()

    def test_read_normal_file(self):
        datafile = 'normal.vok'
        lection = Vokker()
        lection.open(datafile)
        lection.read()

        compartion_dict = {"Auto": "car",
                           "Baum": "tree",
                           "empfohlen": "recommend"}
        boo = bool(compartion_dict == lection.get_vok_dict())
        self.assertTrue(boo)

        lection._file_handle_.close()

    def test_read_Fail_not_opend_file(self):
        lection = Vokker()
        rt = lection.read()
        self.assertFalse(rt)


if __name__ == '__main__':
    unittest.main()
