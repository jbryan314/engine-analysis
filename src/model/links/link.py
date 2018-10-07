class Link:

    """ Links two ports of a given type. Checks to make sure the selected ports are compatible. Sends objects from one
    port to the other.

    Parameters:

    Attributes:

    """

    def __init__(self, from_port, to_port):
        self.from_port = from_port
        self.to_port = to_port

    def __str__(self):
        return 'From: {}\nTo: {}\n'.format(self.from_port, self.to_port)

    def pass_data(self):
        # TODO: get data from in_port
        # TODO: send data to out_port
        pass

    def verify(self):
        # TODO: check if from_port and to_port are of similar type (i.e. both flow ports, shaft ports, etc)
        # TODO: check if from_port links to an out-going port
        # TODO: check if to_port links to an incoming port
        pass
