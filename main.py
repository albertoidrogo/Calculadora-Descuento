from App.calculator import AvanaCalculator

calc = AvanaCalculator()

print("=" * 45)
print("   AVANA HOME - Calculadora de Descuentos")
print("=" * 45)

precio = float(input("\nIngresá el precio del producto: $"))

print("\nMedios de pago disponibles:")
print("  1. efectivo      (20% OFF)")
print("  2. transferencia  (5% OFF)")
print("  3. tarjeta        (sin descuento)")
pago = input("\nMedio de pago: ")

resultado = calc.calcular(precio, pago)

print("\n" + "=" * 45)
print(f"Precio original:  ${resultado['precio_original']:,.2f}")
print(f"Descuento:        {resultado['porcentaje']}%  -${resultado['descuento']:,.2f}")
print(f"PRECIO FINAL:     ${resultado['precio_final']:,.2f}")
print("=" * 45)