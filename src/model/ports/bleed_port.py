from src.model.ports import FluidInputPort, FluidOutputPort


class BleedInPort(FluidInputPort):
    """ Port to manage the flow of air back into the fluid flow from a bleed """
    def __init__(self, parent):
        super().__init__(parent)


class BleedOutPort(FluidOutputPort):
    """ Port to manage the flow of air out of the fluid flow into a bleed """
    def __init__(self, parent):
        super().__init__(parent)
