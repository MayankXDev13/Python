import math

def circle_stats(radius):
    area = round(math.pi * (radius ** 2), 4)
    circumference = round(2 * math.pi * radius, 4)
    return area, circumference


area, circumference = circle_stats(5)

print(f"Area: {area}, Circumference: {circumference}")