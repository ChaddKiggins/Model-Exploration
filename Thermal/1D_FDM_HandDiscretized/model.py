#
#1D Finite Difference thermal model (Cylidrical - Radial)
#Backwards Euler Time stepping
#

import numpy as np
from scipy.sparse import diags

class FDM_1D_Thermal:

    """
    Implements the 1D heat equation using finite difference spatial discretisation 
    and backwards euler time stepping. This will focus on cylindrical coordinates,
    focusing on the radial direction. Matrix building will be 'hand built' and 
    solving will be done with a scipy sparse solver.
    """

    def __init__(self):

        pass