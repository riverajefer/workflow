celsius = float(input("Ingrese el valor de la temperatura en celsius: "))
celsiusfahrenheit = (celsius * 9/5) + 32
kelvin  = (celsius + 273.15)
rankine  = (celsius * 9/5) + 491.67

print('%.2f°  Celsius Equivale a: %0.2f° Fahrenheit' %(celsius, celsiusfahrenheit))
print('%.2f°  Celsius Equivale a: %0.2f° kelvin' %(celsius, kelvin))
print('%.2f°  Celsius Equivale a: %0.2f° Rankine' %(celsius, rankine))