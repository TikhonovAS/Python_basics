from utils import calculate_discount


def test_discount():
    """Проверяет, что скидка 20% от 1000 = 800.0"""
    result = calculate_discount(1000, 20)
    assert result == 800.0, f"Ожидали 800.0, получили {result}"


def test_discount_zero_percent():
    """Проверяет, что скидка 0% не меняет цену"""
    result = calculate_discount(500, 0)
    assert result == 500.0

def test_discount_invalid_percent():
    """Проверяет поведение при скидке > 100% (должно уйти в минус или 0)"""
    result = calculate_discount(100, 150)
    assert result == -50.0
