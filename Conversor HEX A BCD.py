def convertir_hex_a_bcd(numero_hex):
  """
  Convierte un número hexadecimal a BCD (Código Decimal Binario).

  Args:
    numero_hex: El número hexadecimal a convertir (sin prefijo 0x).

  Returns:
    Una lista que representa el número en BCD.
  """

  # Eliminar prefijo "0x" si está presente
  if numero_hex.startswith("0x"):
    numero_hex = numero_hex[2:]

  # Validar entrada hexadecimal
  try:
    int(numero_hex, 16)
  except ValueError:
    raise ValueError(f"Entrada no válida: {numero_hex}. Se esperaba un número hexadecimal.")

  # Convertir HEX a decimal
  numero_decimal = int(numero_hex, 16)

  # Convertir decimal a BCD (utilizando la función del ejemplo anterior)
  bcd = convertir_decimal_a_bcd(numero_decimal)

  return bcd

def convertir_decimal_a_bcd(numero_decimal):
  """
  Convierte un número decimal a BCD (Código Decimal Binario).

  Args:
    numero_decimal: El número decimal a convertir.

  Returns:
(    Una lista que representa el número en BCD.
  """

  bcd = []
  for digito in str(numero_decimal):
    digito_bcd = bin(int(digito))[2:].zfill(4)  # Completar con ceros a la izquierda
    bcd.extend(digito_bcd)
  return bcd

# Ejemplo de uso
numero_hex = "4096"
bcd = convertir_hex_a_bcd(numero_hex)
print(f"BCD de {numero_hex}: {bcd}")
