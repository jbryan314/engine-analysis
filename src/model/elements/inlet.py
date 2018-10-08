from src.model.elements.element import Element
from src.model.ports import FluidInputPort, FluidOutputPort


class Inlet(Element):

    """ Engine inlet """

    def __init__(self):
        super().__init__()
        # attributes
        # ports
        self.Fl_I = FluidInputPort(self)
        self.Fl_O = FluidOutputPort(self)

    def read_in(self):
        pass

    def calculate(self):
        pass

    def read_out(self):
        pass
