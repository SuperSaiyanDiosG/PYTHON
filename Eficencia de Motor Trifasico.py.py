import math

def calculate_three_phase_motor_efficiency(input_power, voltage, current, power_factor, output_power):
    """
    Calculates the efficiency of a three-phase motor.

    Args:
        input_power: The input power of the motor (in watts).
        voltage: The voltage of the motor (in volts).
        current: The current drawn by the motor (in amps).
        power_factor: The power factor of the motor (between 0 and 1).
        output_power: The output power of the motor (in watts).

    Returns:
        The efficiency of the motor (as a percentage).
    """

    if input_power <= 0 or output_power <= 0:
        raise ValueError("Input and output power must be positive numbers.")

    # Calculate input power using the formula:
    # input_power = voltage * current * power_factor * math.sqrt(3)

    # Efficiency calculation:
    efficiency = (output_power / input_power) * 100
    return efficiency

# Example usage
input_power = 1500  # Input power (in watts)
voltage = 480  # Voltage (in volts)
current = 6.8  # Current (in amps)
power_factor = 0.8  # Power factor
output_power = 1200  # Output power (in watts)

efficiency = calculate_three_phase_motor_efficiency(input_power, voltage, current, power_factor, output_power)
print("Efficiency:", efficiency, "%")
