def get_issuer(number: str) -> str:
    if number.startswith("4"):
        return "Visa"
    if number.startswith("3"):
        return "American Express"
    if number.startswith("5"):
        return "Mastercard"
