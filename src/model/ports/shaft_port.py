from src.model.ports.port import Port


class ShaftPort(Port):
    def __init__(self, parent):
        super().__init__(parent)
        self.rot_speed = 0
        self.inertia = 0
        self.power = 0
        self.torque = 0


class ShaftInputPort(ShaftPort):
    def __init__(self, parent):
        super().__init__(parent)


class ShaftOutputPort(ShaftPort):
    def __init__(self, parent):
        super().__init__(parent)
