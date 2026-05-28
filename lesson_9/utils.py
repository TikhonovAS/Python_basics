def format_message(text):
    """
    Оборачивает техт в единый формат для логов.
    """
    return f"[LOG]{text}"


def calculate_discount(price, percent):
    """
    Считает цену со скидкой. Возвращает float, округленный до 2 знаков.
    """
    discount = price * (percent / 100)
    return round(price - discount, 2)