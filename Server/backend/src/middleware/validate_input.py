from flask import request

def validate_input(N, P, K, temperature, humidity, ph, rainfall):
    data=request.get_json()
    N=data.get("N")
    P=data.get("P")
    K=data.get("K")
    temperature=data.get("temperature")
    humidity=data.get("humidity")
    ph=data.get("ph")
    rainfall=data.get("rainfall")

    if N < 0 or P < 0 or K < 0:
        return "NPK values cannot be negative"

    if temperature < -50 or temperature > 60:
        return "Unrealistic temperature"

    if humidity < 0 or humidity > 100:
        return "Humidity must be between 0 and 100"

    if ph < 0 or ph > 14:
        return "pH must be between 0 and 14"

    if rainfall < 0:
        return "Rainfall cannot be negative"

    return "Valid Input"