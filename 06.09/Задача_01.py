class regular_tetrahedron:
    def __init__(self, a):
        self.a = a
        
    def calculate_surface_area(self):
        return (f"surface area of regular tetrahedron with edge length = {self.a} - {(3**(1/2))*self.a**2}")
        
    def calculate_volume(self):
        return (f"volume with edge length = {self.a} - {((2**0.5)/12)*self.a**3}")
        
calc = regular_tetrahedron(3)

print(calc.calculate_surface_area())
print()
print(calc.calculate_volume())

# surface area of regular tetrahedron with edge length = 3 - 15.588457268119894

# volume with edge length = 3 - 3.1819805153394642
# >>>        