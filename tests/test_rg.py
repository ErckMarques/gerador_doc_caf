from gerador_docs import RG

def test_rg():
    """Testa a criação de um RG com dados válidos."""
    rg = RG("123456789", "SSP", "SP")
    assert rg.num_rg == "123456789 SSP/SP"
    assert rg._emissor == "SSP"
    assert rg._uf == "SP"