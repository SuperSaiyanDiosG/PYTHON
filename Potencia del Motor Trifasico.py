import math

def calculate_three_phase_motor_power(voltage, current, power_factor):
  """
  Calculates the power of a three-phase motor.

  Args:
    voltage: The voltage of the motor (in volts).
    current: The current drawn by the motor (in amps).
    power_factor: The power factor of the motor (between 0 and 1).

  Returns:
    The power of the motor (in watts).
  """

  power = (voltage * current * power_factor * math.sqrt(3))
  return power

# Example usage
voltage = 480  # Voltage of the motor (in volts)
current = 3.8  # Current drawn by the motor (in amps)
power_factor = 0.8  # Power factor of the motor

power = calculate_three_phase_motor_power(voltage, current, power_factor)
print("Power:", power, "watts")
