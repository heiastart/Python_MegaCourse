def celsiusToFahrenheit(cel):
    if cel < -273.15:
        return "Invalid temp!"
    else:
        F = cel * (9/5) + 32
        return F

print(celsiusToFahrenheit(35))