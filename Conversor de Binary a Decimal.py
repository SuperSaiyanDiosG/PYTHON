def convertir_decimal_a_bcd(numero_decimal):
  """
  Convierte un número decimal a BCD (Código Decimal Binario).

  Args:
    numero_decimal: El número decimal a convertir.

  Returns:
    Una lista que representa el número en BCD.
  """

  bcd = []
  for digito in str(numero_decimal):
    digito_bcd = bin(int(digito))[2:].zfill(4)  # Completar con ceros a la izquierda
    bcd.extend(digito_bcd)
  return bcd

numero_decimal = 4096  # Ejemplo de número decimal

bcd = convertir_decimal_a_bcd(numero_decimal)
print(f"BCD de {numero_decimal}: {bcd}")

