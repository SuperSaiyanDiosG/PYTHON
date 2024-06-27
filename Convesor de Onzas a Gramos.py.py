def ounces_to_grams(ounces):
    """Converts ounces to grams.

    Args:
        ounces: The value in ounces to convert.

    Returns:
        The equivalent value in grams.
    """
    if not isinstance(ounces, (int, float)):
        raise TypeError(f"Expected a number (int or float), but received: {ounces}")

    return ounces * 28.3495  # Conversion factor from ounces to grams

# Example usage
ounces_value = 13
grams_value = ounces_to_grams(ounces_value)
print(f"{ounces_value} ounces are equivalent to {grams_value:.2f} grams.")
