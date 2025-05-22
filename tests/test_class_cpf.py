import pytest

from gerador_docs import CPF

@pytest.mark.parametrize(
        cpf_input, expected,
        [
            ('','')
        ]
)
def test_cpf_validos(cpf_input, expected):
    assert cpf == expected, f"Expected {expected}, but got {str(cpf)}"
    