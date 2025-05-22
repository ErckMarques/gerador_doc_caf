import pytest

from gerador_docs import CPF
from gerador_docs.errors import CPFInvalidError

@pytest.mark.parametrize(
    "cpf_input",
    [
        "11111111111",
        "22222222222",
        "33333333333",
    ]
)
@pytest.mark.parametrize(
    "cpf_lengh_invalid",
    [
        "1254321",
        "1234568791564765"
    ]
)
@pytest.mark.parametrize(
    "cpf_format_invalid",
    [
        "asdgfcvgbhn",
        "1235as456sd",
    ]
)
def test_cpf_invalid(cpf_input, cpf_lengh_invalid, cpf_format_invalid):
    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_input)
        assert str(exc_info.value) == f"CPF inválido: {cpf_input}. Erro O CPF não pode conter todos os dígitos iguais."
    
    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_lengh_invalid)
        assert str(exc_info.value) == f"O CPF deve ter 11 dígitos."

    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_format_invalid)
        assert str(exc_info.value) == f"O CPF deve conter apenas dígitos."