"""Funciones:
cm_a_pulgadas(centimetros): Recibe un valor en centímetros y lo convierte a pulgadas.
pulgadas_a_cm(pulgadas): Recibe un valor en pulgadas y lo convierte a centímetros.
Fórmulas de conversión:
Centímetros a pulgadas: Se multiplica por 0.3937.
Pulgadas a centímetros: Se multiplica por 2.54.
Ejemplos de uso:
Se solicita al usuario ingresar la cantidad a convertir.
Se llama a la función correspondiente (según la unidad de entrada).
Se imprime el resultado con dos decimales."""

def cm_a_pulgadas(centimetros):
  """
  Convierte una cantidad de centímetros a pulgadas.

  Parámetros:
    centimetros: Valor en centímetros a convertir.

  Retorna:
    Valor equivalente en pulgadas.
  """
  pulgadas = centimetros * 0.3937
  return pulgadas

# Ejemplo de uso
cantidad_cm = float(input("Ingrese la cantidad en centímetros: "))
pulgadas = cm_a_pulgadas(cantidad_cm)
print(f"{cantidad_cm} centímetros equivalen a {pulgadas:.2f} pulgadas.")
