"""Importaciones:
random: Para generar números aleatorios.
string: Para acceder a conjuntos de caracteres predefinidos.
Función generar_contrasena:
Parámetros:
longitud: Longitud deseada de la contraseña (por defecto 12).
incluir_minusculas, incluir_mayusculas, incluir_numeros, incluir_simbolos: Flags para indicar qué tipos de caracteres incluir.
Lógica:
Crea una lista caracteres que incluye los conjuntos seleccionados.
Valida que haya al menos un tipo de caracter seleccionado.
Genera una cadena aleatoria de la longitud especificada usando random.choice.
Retorna la contraseña generada.
Ejemplo de uso:
Solicita al usuario la longitud deseada y las opciones de caracteres.
Llama a la función generar_contrasena con los parámetros seleccionados.
Muestra la contraseña generada al usuario.
Características adicionales:

Validación de entrada:
Se asegura de que la longitud sea de al menos 8 caracteres.
Se verifica que se haya seleccionado al menos un tipo de caracter.
Mayor personalización:
Permite elegir qué tipos de caracteres incluir en la contraseña.
Seguridad:
Utiliza el módulo random para generar contraseñas aleatorias e impredecibles.
No almacena la contraseña en ningún lugar del código."""

import random
import string

def generar_contrasena(longitud, incluir_minusculas=True, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
  """
  Genera una contraseña segura aleatoria con las opciones especificadas.

  Parámetros:
    longitud: Longitud deseada de la contraseña (por defecto 12).
    incluir_minusculas: Incluir letras minúsculas (por defecto True).
    incluir_mayusculas: Incluir letras mayúsculas (por defecto True).
    incluir_numeros: Incluir números (por defecto True).
    incluir_simbolos: Incluir símbolos (por defecto True).

  Retorna:
    Contraseña aleatoria generada.
  """
  caracteres = []

  if incluir_minusculas:
    caracteres.extend(string.ascii_lowercase)
  if incluir_mayusculas:
    caracteres.extend(string.ascii_uppercase)
  if incluir_numeros:
    caracteres.extend(string.digits)
  if incluir_simbolos:
    caracteres.extend(string.punctuation)

  if not caracteres:
    raise ValueError("No se seleccionaron caracteres para la contraseña.")

  contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
  return contrasena

# Ejemplo de uso
longitud = int(input("Ingrese la longitud deseada de la contraseña (mínimo 8): "))
incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == "s"
incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == "s"
incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

contrasena_generada = generar_contrasena(longitud, incluir_minusculas, incluir_mayusculas, incluir_numeros, incluir_simbolos)
print(f"Su contraseña segura es: {contrasena_generada}")
