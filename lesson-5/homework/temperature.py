def convert_cel_to_far(degree_celsius):
    return degree_celsius * (9/5) + 32
def convert_far_to_cel(degree_fahrenheit):
    return (degree_fahrenheit - 32)  * (5/9)

degree_F = float(input('Enter a temperature in degrees F: '))
print(f"{degree_F} degrees F = {convert_far_to_cel(degree_F):.2f} degrees C")
degree_C = float(input('Enter a temperature in degrees C: '))
print(f"{degree_C} degrees C = {convert_cel_to_far(degree_C):.2f} degrees F")

