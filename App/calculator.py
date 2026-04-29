class AvanaCalculator:
    """
    Calculadora de descuentos para Avana Home.
    Efectivo:      20% de descuento
    Transferencia:  5% de descuento
    Tarjeta:        sin descuento
    """

    DESCUENTOS = {
        "efectivo":       0.20,
        "transferencia":  0.05,
        "tarjeta":        0.00,
    }

    def calcular(self, precio, medio_de_pago):
        """
        Calcula el precio final con descuento.

        Args:
            precio: precio original (debe ser mayor a 0)
            medio_de_pago: 'efectivo', 'transferencia' o 'tarjeta'

        Returns:
            dict con precio_original, descuento y precio_final

        Raises:
            ValueError: si el precio o medio de pago son inválidos
        """
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor a 0.")

        medio_de_pago = medio_de_pago.lower().strip()
        if medio_de_pago not in self.DESCUENTOS:
            raise ValueError(
                f"Medio de pago '{medio_de_pago}' no válido. "
                f"Use: efectivo, transferencia o tarjeta."
            )

        porcentaje = self.DESCUENTOS[medio_de_pago]
        descuento  = round(precio * porcentaje, 2)
        final      = round(precio - descuento, 2)

        return {
            "precio_original":     precio,
            "porcentaje":          round(porcentaje * 100, 1),
            "descuento":           descuento,
            "precio_final":        final,
        }