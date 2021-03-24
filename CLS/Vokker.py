class Vokker:

    def __init__(self):
        self.datafile = None
        self._file_handle_ = None
        self._vok_dict_ = dict()
        self._vok_new_data_ = dict()
        self._datafolder_ = "data"
        self._safelock_ = False  # Lock for deleting data

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
        if self._safelock_ is False:
            try:
                self._file_handle_ = open('data/' + filename, mode)
                rt = True
            except FileNotFoundError:
                rt = False
        else:
            rt = False

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

        if source not in self._vok_dict_:
            self._vok_dict_[source] = translate
            return True
        else:
            return False

    def get_vok_dict(self):
        return self._vok_dict_

    def write(self):
        # todo : think about overwrite und append

        for key in self._vok_dict_:
            data = f'{key},{self._vok_dict_[key]}\n'
            self._file_handle_.write(data)

    def read(self):
        if self._vok_dict_ is not None:
            for data in self._file_handle_:
                vok = data.split(",")
                self._vok_dict_[vok[0]] = vok[1].strip()
                return True
        else:
            # Datafield is not empty, don`t read
            return False

    def close(self):
        self._file_handle_.close()
        self._file_handle_ = None
