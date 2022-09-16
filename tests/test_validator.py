from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4343 4123 1435 1231") == "Visa"


def test_get_issuer_master_card():
    assert get_issuer("5142 2131 5464 6523") == "Mastercard"
    assert not get_issuer("5642 2131 5464 6523") == "Mastercard"


def test_get_issuer_american_express():
    assert get_issuer("3343 4123 1435 1231") == "American Express"
