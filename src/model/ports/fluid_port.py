from src.model.ports.port import Port


class FluidPort(Port):
    """ Parent class for fluid input/output ports """
    def __init__(self, parent):
        super().__init__(parent)


class FluidInputPort(FluidPort):
    """ Port to manage the flow of air into an element """
    def __init__(self, parent):
        super().__init__(parent)


class FluidOutputPort(FluidPort):
    """ Port to manage the flow of air out of an element """
    def __init__(self, parent):
        super().__init__(parent)
