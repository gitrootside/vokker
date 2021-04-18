import re


class Vokker:
    # Filestructure: first line: number of lines

    def __init__(self):
        self.datafile = None
        self._file_handle = None
        self._vok_data = None
        self._vok_new_data = None
        self._datafolder = "test_data"
        self._safelock = False  # Lock for deleting data
        self._seperator = ';'

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
        if (self._safelock is False) and (self._vok_new_data is None):
            try:
                self._file_handle = open(self._datafolder + '/' + filename, mode)
                rt = True
            except FileNotFoundError:
                rt = False

        return rt

    def close(self):
        rt = False
        if (self._safelock is False) and (self._vok_new_data is None):
            self._file_handle.close()
            rt = True
            self._file_handle = None
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

        if source not in self._vok_data:
            self._vok_data[source] = translate
            return True
        else:
            return False

    def get_vok_dict(self):
        return self._vok_data

    def write(self):
        # todo : think about overwrite und append

        for key in self._vok_data:
            data = f'{key},{self._vok_data[key]}\n'
            self._file_handle.write(data)

    def fileexist(self, file):

        try:
            f = open(self._datafolder + "/" + file, "r")
            f.close()
            return f
        except:
            return False

    def read(self):
        rt = False
        if (self._file_handle is not None) and (self._vok_data is None) and (self._safelock is False):
            rt = True
            self._vok_data = dict()
            self._vok_new_data = dict()

            first = True
            for data in self._file_handle:
                if first:
                    if re.match("\A\d{1,5}\s", data):    # Correct header
                        number_lines = int(data)
                        first = False
                        continue
                    else:
                        return False
                else:
                    if re.match("(\w+ *)+;(\w+ *)+", data):  # Correct datastructure
                        vok = data.split(self._seperator)
                        self._vok_data[vok[0]] = vok[1].strip()
                    else:
                        return False

            if len(self._vok_data) != number_lines:
                rt = False
        return rt
