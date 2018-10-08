from src.model.elements.element import Element
import numpy as np


class Ambient(Element):

    """ Ambient air conditions

    Static Class Attributes:
        atm_data : np.ndarray
            Atmospheric data in US units
            atm_data[0] -- Altitude [ft]
            atm_data[1] -- Temperature [R]
            atm_data[2] -- Pressure [psia]
            atm_data[3] -- Density [lbm/ft^3]
            atm_data[4] -- Viscosity [lbf-s/ft^2]

    Instance Attributes:
        alt : float
            Altitude at which to retrieve ambient data
    """

    atm_data = np.genfromtxt(fname='data/atm_props_US.csv', dtype=float, skip_header=1, delimiter='\t').T
    atm_data[3] *= 32.174  # converts densities from [slug/ft^3] to [lbm/ft^3]

    def __init__(self, altitude):
        super().__init__()
        # use linear interpolation to find values at given altitude
        # TODO: check for accuracy and implement cubic spline interpolation if necessary
        self.alt = altitude
        self.temperature = np.interp(altitude, self.atm_data[0], self.atm_data[1])
        self.pressure = np.interp(altitude, self.atm_data[0], self.atm_data[2])
        self.density = np.interp(altitude, self.atm_data[0], self.atm_data[3])
        self.viscosity = np.interp(altitude, self.atm_data[0], self.atm_data[4])

    @property
    def altitude(self):
        return self.alt

    @altitude.setter
    def altitude(self, val):
        self.alt = val
        self.temperature = np.interp(val, self.atm_data[0], self.atm_data[1])
        self.pressure = np.interp(val, self.atm_data[0], self.atm_data[2])
        self.density = np.interp(val, self.atm_data[0], self.atm_data[3])
        self.viscosity = np.interp(val, self.atm_data[0], self.atm_data[4])
