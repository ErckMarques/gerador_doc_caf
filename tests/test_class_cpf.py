import pytest

from gerador_docs import CPF

@pytest.mark.parametrize(
    "cpf_input, expected_output",
    [
        ("12345678909", "123.456.789-09"),
        ("11111111111", "111.111.111-11"),
        ("22222222222", "222.222.222-22"),
        ("33333333333", "333.333.333-33"),
        ("44444444444", "444.444.444-44"),
        ("55555555555", "555.555.555-55"),
        ("66666666666", "666.666.666-66"),
        ("77777777777", "777.777.777-77"),
        ("88888888888", "888.888.888-88"),
        ("99999999999", "999.999.999-99")
    ]
)
def test_cpf(cpf_input, expected_output):
    with pytest.raises(ValueError):
        cpf = CPF(cpf_input)
        assert cpf == expected_output, f"Expected {expected_output}, but got {str(cpf)}"
    
    #rever como escrever este teste