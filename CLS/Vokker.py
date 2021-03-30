import re as re


class Vokker:
    # Filestructure: first line: number of lines

    def __init__(self):
        self.datafile = None
        self._file_handle_ = None
        self._vok_data_ = None
        self._vok_new_data_ = None
        self._datafolder_ = "test_data"
        self._safelock_ = False  # Lock for deleting data
        self._seperator_ = ';'

    def set_filename(self, filename):

        self.datafile = filename

    def open(self, filename, mode: str = "r"):
        """
        open a vok-file and hold the connection, store the instance in _file_handle_

        :param filename:
        :param mode: like in standard-python open
        :return: False if connection failed.... True if connection successful applied
        """
        rt = False
        if (self._safelock_ is False) and (self._vok_new_data_ is None):
            try:
                self._file_handle_ = open(self._datafolder_ + '/' + filename, mode)
                rt = True
            except FileNotFoundError:
                rt = False

        return rt

    def close(self):
        rt = False
        if (self._safelock_ is False) and (self._vok_new_data_ is None):
            self._file_handle_.close()
            rt = True
            self._file_handle_ = None
        return rt

    def add(self, *args):
        # todo : extends the data for insert more than one meaning for one word

        """ simple add a vok to the dictionary

        :param args: 2 words for vok
        :return:    False if args empty and length unequal 2 or key still in dictionary
                    True ok
        """
        if args and len(args) == 2:
            source = args[0]
            translate = args[1]
        else:
            return False  # more than two words

        if source not in self._vok_data_:
            self._vok_data_[source] = translate
            return True
        else:
            return False

    def get_vok_dict(self):
        return self._vok_data_

    def write(self):
        # todo : think about overwrite und append

        for key in self._vok_data_:
            data = f'{key},{self._vok_data_[key]}\n'
            self._file_handle_.write(data)

    def fileexist(self, file):

        try:
            f = open(self._datafolder_ + "/" + file, "r")
            f.close()
            return f
        except:
            return False

    def read(self):
        rt = False
        if (self._file_handle_ is not None) and (self._vok_data_ is None) and (self._safelock_ is False):
            rt = True
            self._vok_data_ = dict()
            self._vok_new_data_ = dict()

            first = True
            for data in self._file_handle_:
                if first:
                    if re.match("\A\d{1,5}\s", data):
                        number_lines = int(data)
                        first = False
                    else:
                        return False
                else:
                    # todo regex
                    vok = data.split(self._seperator_)
                    self._vok_data_[vok[0]] = vok[1].strip()

            if len(self._vok_data_) != number_lines:
                rt = False
        return rt
