from src.model.components.element import Element
from src.model.ports import FluidInputPort, FluidOutputPort, ShaftInputPort


class Turbine(Element):

    """ Turbine """

    def __init__(self):
        super().__init__()
        # attributes
        # ports
        self.Fl_I = FluidInputPort()
        self.Fl_O = FluidOutputPort()
        self.Sh_I = ShaftInputPort()

    def read_in(self):
        pass

    def calculate(self):
        pass

    def read_out(self):
        pass
