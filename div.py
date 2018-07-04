def celsiusToFahrenheit(cel):
    if cel < -273.15:
        return "Invalid temp!"
    else:
        F = cel * (9/5) + 32
        return F

temperatures = [10, -20, -289, 100]

for i in temperatures:
    print(celsiusToFahrenheit(i))