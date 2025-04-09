def calculate_volume_of_sphere(radius):
    volume = (4/3) * 3.14 * (radius ** 3)
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a sphere with radius {radius1} is {volume1:.2f} cubic units.")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of a sphere with radius {radius2} is {volume2:.2f} cubic units.")