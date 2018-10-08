class Element:

    """ Element base class, inherited by all other element classes. """

    def __str__(self):
        attributes = ''
        if self.__dict__:
            for k, v in self.__dict__.items():
                attributes += '{}: {}\n'.format(k, v)
        else:
            attributes = 'This element has no defined attributes.\n'
        return attributes

    def read_in(self):
        # gets data from input ports
        return

    def calculate(self):
        # runs calculations for element
        return

    def read_out(self):
        # sends data to output ports
        return

    def run(self):
        self.read_in()
        self.calculate()
        self.read_out()
        # TODO: tell all downstream linked elements to run
