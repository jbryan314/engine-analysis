from src.model.elements.element import Element
from src.model.ports import FluidInputPort, FluidOutputPort, ShaftOutputPort


class Compressor(Element):

    """ Compressor element

    Attributes:
        pressure_ratio : float
            The pressure ratio P_out / P_in that the compressor is designed for.
        efficiency : float
            Adiabatic efficiency of the compressor. Must be between 0 and 1.
    """

    def __init__(self, pressure_ratio, efficiency):
        if efficiency < 0 or efficiency > 1:
            raise ValueError('Adiabatic efficiency must be between 0 and 1')
        super().__init__()
        # design parameters
        self.pressure_ratio = pressure_ratio
        self.efficiency = efficiency
        # ports
        self.Fl_I = FluidInputPort(self)
        self.Fl_O = FluidOutputPort(self)
        self.Sh_O = ShaftOutputPort(self)
