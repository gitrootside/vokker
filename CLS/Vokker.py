class Vokker:
    datafile = None
    _file_handle_ = None
    _vok_dict_ = dict()
    _datafolder_ = "data"

    def __init__(self):
        pass

    def open(self, mode: str = "r"):
        """
        open a vok-file and hold the connection, store the instance in _file_handle_

        :param mode: like in standard-python open
        :return: False if connection failed.... True if connection successful applied
        """
        try:
            self._file_handle_ = open('data/' + self.datafile, mode)
        except FileNotFoundError:
            return False

        return True

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
