import math

degrees = [0,30,45,60,90]

for de in degrees:
    a = math.sin(math.pi * (de / 180))
    b = math.cos(math.pi * (de / 180))
    c = math.tan(math.pi * (de / 180))

    print(f"sin({de:2d}) : {a:.4f}")
    print(f"cos({de:2d}) : {a:.4f}")
    print(f"tan({de:2d}) : {a:.4f}")
