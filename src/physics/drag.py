"""
Drag Force Calculation Module
Phoenix Aerospace Engineering Platform (PAEP)
"""

def calculate_drag(rho, velocity, wing_area, cd):
    """
    Calculate aerodynamic drag force.
    """

    return 0.5 * rho * velocity**2 * wing_area * cd
