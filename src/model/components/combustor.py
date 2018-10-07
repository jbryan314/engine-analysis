from src.model.components.element import Element
from src.model.ports import FluidInputPort, FluidOutputPort, FuelInputPort


class Combustor(Element):

    """ The thing that burns the fuel """

    def __init__(self):
        super().__init__()
        # attributes
        # TODO: get important variables from Julie
        # ports
        self.Fl_I = FluidInputPort()
        self.Fl_O = FluidOutputPort()
        self.Fu_I = FuelInputPort()

    def read_in(self):
        pass

    def calculate(self):
        pass

    def read_out(self):
        pass
