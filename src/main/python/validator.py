def validate_temperature(t):
    # El CISO cambió el rango: ahora es de 2 a 8 grados
    if t < 2 or t > 8:
        return False
    return True