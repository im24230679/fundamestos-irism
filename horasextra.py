# Realizar un programa que permitaleer las horas trabajadas.

# Pedir número de horas trabajadas
horas_trabajadas = int(input("Ingresa el número de horas trabajadas: "))

# Definir pagos
pago_normal = 200
pago_extra = 350

# Calcular el pago total
if horas_trabajadas <= 8:
    pago_total = horas_trabajadas * tarifa_normal

else:
    horas_extras = horas_trabajadas - 8
    pago_normal = 8 * tarifa_normal
    pago_extra = horas_extras * pago_extra
    pago_total = pago_normal + pago_extra

# Mostrar el pago total
print(f"El pago total es: ${pago_total:.2f} MXN")