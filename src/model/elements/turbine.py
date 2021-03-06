from src.model.elements.element import Element
from src.model.ports import FluidInputPort, FluidOutputPort, ShaftInputPort


class Turbine(Element):

    """ Turbine """

    def __init__(self):
        super().__init__()
        # attributes
        # ports
        self.Fl_I = FluidInputPort(self)
        self.Fl_O = FluidOutputPort(self)
        self.Sh_I = ShaftInputPort(self)

    def read_in(self):
        pass

    def calculate(self):
        pass

    def read_out(self):
        pass
