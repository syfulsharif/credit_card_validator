from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4343 4123 1435 1231") == "Visa"
