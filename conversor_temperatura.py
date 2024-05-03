class ConversorTemperatura:
    @staticmethod
    def fahrenheit_para_celsius(f):
        return (f - 32) * 5.0/9.0

    @staticmethod
    def celsius_para_fahrenheit(c):
        return (c * 9.0/5.0) + 32

# Exemplo de uso:
temp_celsius = ConversorTemperatura.fahrenheit_para_celsius(100)
print(f'100°F é igual a {temp_celsius:.2f}°C')
temp_fahrenheit = ConversorTemperatura.celsius_para_fahrenheit(0)
print(f'0°C é igual a {temp_fahrenheit:.2f}°F')
