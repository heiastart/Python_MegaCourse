temps = [10, -20, -289, 100]

def writer(temp, filepath):
    with open(filepath, 'w') as file:
        for cels in temp:
            if cels > -273.15:
                F = cels * (9/5) + 32
                file.write('Temperature in Fahrenheit is ' + str(F) + ' for ' + str(cels) + ' degrees Celsius\n')

writer(temps, 'temps.txt')


for c in temps:
    if c > -273.15:
        F = c * (9 / 5) + 32
        print('Temperature in Fahrenheit is ' + str(F) + ' for ' + str(c) + ' degrees Celsius')
    else:
        print('Invalid temp-value of ' + str(c) + ' degrees Celsius')