def celsiusToFahrenheit(cel):
    if cel < -273.15:
        return "Invalid temp!"
    else:
        F = cel * (9/5) + 32
        return F

index = [1, 2, 3, 4]
temperatures = [10, -20, -289, 100]

for i,j in zip(index, temperatures):
    print('%s is %s degrees Celsius' %(i,j))
#for i in temperatures:
#    print(celsiusToFahrenheit(i))