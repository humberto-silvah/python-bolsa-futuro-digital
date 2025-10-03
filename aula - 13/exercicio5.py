def calcular_frete(peso,distacia):
    if (peso <= 10):
        valor= (5 * distacia)

    elif peso > 10:
        valor= (7 * distacia)

    return valor

def test_frete():
    assert calcular_frete(10 , 10)
    assert calcular_frete(20, 10)