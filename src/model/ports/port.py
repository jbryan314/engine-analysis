import weakref


class Port:

    """ Port base class, inherited by all other port classes """

    def __init__(self, parent):
        self.parent_element = weakref.ref(parent)  # uses weakref to keep object reference garbage collector friendly
        self.link = None

    def __str__(self):
        attributes = ''
        for k, v in self.__dict__.items():
            attributes += '{}: {}\n'.format(k, v)
        return attributes

    def verify(self):
        return self.link.verify()
