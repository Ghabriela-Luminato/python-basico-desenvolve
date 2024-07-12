
import math

raios = [1.5, 0.8, 2.3, 5.0]
areas = list(map(lambda r: round(math.pi * r**2, 2), raios))
print(areas)
