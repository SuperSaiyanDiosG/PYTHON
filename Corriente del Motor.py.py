import math

def calculate_three_phase_motor_current(power, voltage, power_factor):
  """
  Calculates the current of a three-phase motor.

  Args:
    power: The power of the motor (in watts).
    voltage: The voltage of the motor (in volts).
    power_factor: The power factor of the motor (between 0 and 1).

  Returns:
    The current of the motor (in amps).
  """

  current = (power * math.sqrt(3)) / (voltage * power_factor)
  return current

# Example usage
power = 2500  # Power of the motor (in watts)
voltage = 480  # Voltage of the motor (in volts)
power_factor = 0.8  # Power factor of the motor (between 0 and 1)

current = calculate_three_phase_motor_current(power, voltage, power_factor)
print("Current:", current, "amps")
