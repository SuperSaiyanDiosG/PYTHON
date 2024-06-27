def pulgadas_a_cm(pulgadas):
  """
  Convierte una cantidad de pulgadas a centímetros.

  Parámetros:
    pulgadas: Valor en pulgadas a convertir.

  Retorna:
    Valor equivalente en centímetros.
  """
  centimetros = pulgadas * 2.54
  return centimetros

# Ejemplo de uso
cantidad_pulgadas = float(input("Ingrese la cantidad en pulgadas: "))
centimetros = pulgadas_a_cm(cantidad_pulgadas)
print(f"{cantidad_pulgadas} pulgadas equivalen a {centimetros:.2f} centímetros.")
