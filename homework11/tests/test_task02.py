from homework11.task02.discount import EveningDiscount, MorningDiscount, Order


def test_discount_is_accounted():
    order = Order(100, MorningDiscount)
    assert order.final_price() == 50


def test_order_without_discount():
    order = Order(100)
    assert order.final_price() == 100


def test_discount_change():
    order = Order(100, MorningDiscount)
    assert order.final_price() == 50
    order.set_discount(EveningDiscount)
    assert order.final_price() == 10
