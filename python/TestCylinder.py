from Cylinder import *


c1 = Cylinder()
print(f'Cyl radius = {c1.get_radius()}, height = {c1.get_height()}, base area = {c1.get_area()}, volume = {c1.get_volume()}')

c2 = Cylinder(2, 6.2)
print(f'Cyl radius = {c2.get_radius()}, '
      f'height = {c2.get_height()}, '
      f'base area = {c2.get_area()}, '
      f'volume = {c2.get_volume()}')
