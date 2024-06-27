def calcular_calibre_trifasico(potencia, tension, longitud, material, factor_potencia=0.85):
  """
  Calcula el calibre de cable necesario para una instalación trifásica.

  Args:
    potencia: Potencia total en Watts (W) de la carga trifásica.
    tension: Tensión de línea en Volts (V) del sistema trifásico.
    longitud: Longitud del cable en metros (m).
    material: Material del conductor ("cobre" o "aluminio").
    factor_potencia: Factor de potencia de la carga trifásica (cos(φ)). Valor por defecto: 0.85.

  Returns:
    Calibre de cable adecuado según la tabla de calibres.
  """

  # Cálculo de la corriente
  corriente = potencia / (sqrt(3) * tension * factor_potencia)

  # Corrección del factor de longitud
  if longitud > 50:
    correccion_longitud = 1 + (longitud - 50) / 100
    corriente *= correccion_longitud

  # Selección del material del conductor
  if material.lower() == "cobre":
    tabla_calibre = tabla_calibre_cobre
  elif material.lower() == "aluminio":
    tabla_calibre = tabla_calibre_aluminio
  else:
    raise ValueError("Material del conductor no válido. Elija 'cobre' o 'aluminio'.")

  # Búsqueda del calibre adecuado en la tabla
  for calibre, intensidad_maxima in tabla_calibre.items():
    if corriente <= intensidad_maxima:
      return calibre

  raise ValueError("No se encontró un calibre adecuado para la corriente calculada.")

# Tabla de calibres de cable para cobre (intensidad máxima en amperios)
tabla_calibre_cobre = {
  "8": 16,
  "6": 25,
  "4": 40,
  "2": 63,
  "1": 80,
  "0": 100,
  "2/0": 150,
  "3/0": 200,
  "4/0": 300}

# Tabla de calibres de cable para aluminio (intensidad máxima en amperios)
tabla_calibre_aluminio = {
  "8": 10,
  "6": 16,
  "4": 25,
  "2": 40,
  "1": 63,
  "0": 80,
  "2/0": 100,
  "3/0": 125,
  "4/0": 160}

# Ejemplo de uso
potencia = 5000  # Potencia en Watts (W)
tension = 480  # Tensión de línea en Volts (V)
longitud = 100  # Longitud del cable en metros (m)
material = "cobre"  # Material del conductor ("cobre" o "aluminio")

calibre = calcular_calibre_trifasico(potencia, tension, longitud, material)
print(f"Calibre de cable recomendado")
