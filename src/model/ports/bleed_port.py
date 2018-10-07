from src.model.ports.fluid import FluidInputPort, FluidOutputPort


class BleedInPort(FluidInputPort):
    """ Port to manage the flow of air back into the fluid flow from a bleed """
    def __init__(self):
        super().__init__()


class BleedOutPort(FluidOutputPort):
    """ Port to manage the flow of air out of the fluid flow into a bleed """
    def __init__(self):
        super().__init__()
