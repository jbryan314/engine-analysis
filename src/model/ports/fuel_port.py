from src.model.ports.port import Port


class FuelPort(Port):
    """ Parent class for fluid input/output ports """
    def __init__(self, parent):
        super().__init__(parent)


class FuelInputPort(FuelPort):
    """ Port to manage the flow of air into an element """
    def __init__(self, parent):
        super().__init__(parent)


class FuelOutputPort(FuelPort):
    """ Port to manage the flow of air out of an element """
    def __init__(self, parent):
        super().__init__(parent)
