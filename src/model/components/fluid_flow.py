from src.model.components.element import Element
from src.model.ports.fluid_port import FluidInputPort, FluidOutputPort


class FlowStart(Element):

    """ FlowStart will the start a flow stream from known conditions

    Attributes:
        C_mf : float
            Carbon mass fraction
        H2_mf : float
            Hydrogen mass fraction
        N2_mf : float
            Nitrogen mass fraction
        O2_mf : float
            Oxygen mass fraction
        FAR : float
            Fuel-to-air ratio
        m_dot : float
            Mass flow rate [lbm/sec]
        Pt : float
            Total pressure of the flow [psia]
        Tt : float
            Absolute temperature of the flow [R]
        fuel_type : str
            Type of fuel used
        Fl_O : FluidOutputPort
            Primary exit flow
    """

    def __init__(self, fuel_type):
        if not isinstance(fuel_type, str):
            raise TypeError('fuel_type must be passed in as a string')
        # attributes
        self.fuel_type = fuel_type
        self.C_mf = 0
        self.H2_mf = 0
        self.N2_mf = 0
        self.O2_mf = 0
        self.FAR = 0
        self.m_dot = 0
        self.Pt = 0
        self.Tt = 0
        # ports
        self.Fl_O = FluidOutputPort()

    def read_out(self):
        pass


class FlowEnd(Element):

    """ FlowEnd terminates a flow stream.

    Attributes:
        Pt : float
            Total pressure of the flow [psia]
        Tt : float
            Absolute temperature of the flow [R}
        m_dot : float
            Mass flow rate [lbm/sec]
        Fl_I : FluidInputPort
            Primary inlet flow
    """

    def __init__(self):
        self.Pt = 0
        self.Tt = 0
        self.m_dot = 0
        self.Fl_I = FluidInputPort()

    def read_in(self):
        pass
