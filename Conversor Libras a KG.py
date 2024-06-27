def libras_a_kg(libras):
  """
  Convierte libras a kilogramos.

  Args:
    libras: El valor en libras a convertir.

  Returns:
    El valor equivalente en kilogramos.
  """
  if not isinstance(libras, (int, float)):
    raise TypeError(f"Se esperaba un número (int o float), pero se recibió: {libras}")
  
  return libras * 0.453592  # Factor de conversión de libras a kilogramos

# Ejemplo de uso
cantidad_libras = 5
cantidad_kg = libras_a_kg(cantidad_libras)
print(f"{cantidad_libras} libras equivalen a {cantidad_kg:.2f} kilogramos.")


