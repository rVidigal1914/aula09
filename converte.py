def celsius_para_fahrenheit(celsius_list):
    fahrenheit_list = []
    for celsius in celsius_list:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list

# Exemplo de uso:
temperaturas_celsius = [0, 20, 30, 100]
temperaturas_fahrenheit = celsius_para_fahrenheit(temperaturas_celsius)

print("Temperaturas em Celsius:", temperaturas_celsius)
print("Temperaturas em Fahrenheit:", temperaturas_fahrenheit)
