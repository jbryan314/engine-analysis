from src.model.ports.port import Port


class FuelPort(Port):
    """ Parent class for fluid input/output ports """
    def __init__(self):
        super().__init__()


class FuelInputPort(FuelPort):
    """ Port to manage the flow of air into an element """
    def __init__(self):
        super().__init__()


class FuelOutputPort(FuelPort):
    """ Port to manage the flow of air out of an element """
    def __init__(self):
        super().__init__()
