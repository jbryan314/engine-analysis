from src.model.ports.port import Port


class ShaftPort(Port):
    def __init__(self):
        super().__init__()
        self.rot_speed = 0
        self.inertia = 0
        self.power = 0
        self.torque = 0


class ShaftInputPort(ShaftPort):
    def __init__(self):
        super().__init__()


class ShaftOutputPort(ShaftPort):
    def __init__(self):
        super().__init__()
