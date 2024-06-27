def ley_ohm(magnitud, valor1, valor2):
  """
  Calcula la magnitud desconocida en la ley de Ohm.

  Args:
    magnitud (str): La magnitud que se desea calcular ("V", "I" o "R").
    valor1 (float): El valor conocido de una de las otras dos magnitudes.
    valor2 (float): El valor conocido de la otra magnitud.

  Returns:
    float: El valor calculado de la magnitud desconocida.
  """

  if magnitud == "V":
    return valor1 * valor2
  elif magnitud == "I":
    return valor1 / valor2
  elif magnitud == "R":
    return valor2 / valor1
  else:
    raise ValueError("Magnitud no válida: {}".format(magnitud))

# Ejemplo de uso
voltaje = ley_ohm("V", 120, 2)
corriente = ley_ohm("I", voltaje, 10)
resistencia = ley_ohm("R", voltaje, corriente)

print("Voltaje:", voltaje)
print("Corriente:", corriente)
print("Resistencia:", resistencia)
