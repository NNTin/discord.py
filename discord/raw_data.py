class RawData:
    __slots__ = ['_data']

    def __init__(self):
        pass

    def to_dict(self):
        if '_data' in self.__slots__:
            return self._data
        else:
            return None
