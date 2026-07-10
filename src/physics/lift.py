"""
Lift Force Calculation Module
Phoenix Aerospace Engineering Platform (PAEP)
"""

def calculate_lift(rho, velocity, wing_area, cl):
    """
    Calculate aerodynamic lift force.

    Parameters
    ----------
    rho : float
        Air density (kg/m³)
    velocity : float
        Aircraft velocity (m/s)
    wing_area : float
        Wing area (m²)
    cl : float
        Lift coefficient

    Returns
    -------
    float
        Lift force (N)
    """

    return 0.5 * rho * velocity ** 2 * wing_area * cl
