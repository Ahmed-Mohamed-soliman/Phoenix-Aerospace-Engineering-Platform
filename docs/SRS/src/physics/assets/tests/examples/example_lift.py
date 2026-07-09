from src.physics.lift import calculate_lift

lift = calculate_lift(
    rho=1.225,
    velocity=70,
    wing_area=16,
    cl=1.1
)

print(f"Lift Force = {lift:.2f} N")
