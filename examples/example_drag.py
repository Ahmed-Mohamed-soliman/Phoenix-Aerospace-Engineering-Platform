from src.physics.drag import calculate_drag

drag = calculate_drag(
    rho=1.225,
    velocity=70,
    wing_area=16,
    cd=0.03
)

print(f"Drag Force = {drag:.2f} N")
