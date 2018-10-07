from src.model.components.element import Element
from src.model.ports import FuelOutputPort


class FuelStart(Element):

    """ FuelStart starts the flow of fuel """

    def __init__(self):
        super().__init__()
        # attributes
        # ports
        self.Fu_O = FuelOutputPort()

    def read_out(self):
        pass
