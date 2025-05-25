import pytest

from gerador_docs import CPF
from gerador_docs.errors import CPFInvalidError

@pytest.mark.parametrize(
    "cpf_repeted_numbers",
    [
        "11111111111",
        "22222222222",
        "33333333333",
    ]
)
def test_cpf_repetd_numbers(cpf_repeted_numbers):
    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_repeted_numbers)
        assert str(exc_info.value) == f"Erro O CPF não pode conter todos os dígitos iguais."

@pytest.mark.parametrize(
    "cpf_lengh_invalid",
    [
        "1254321",
        "1234568791564765"
    ]
)
def test_cpf_invalid_length(cpf_lengh_invalid):
    '''Testa se o cpf tem 11 dígitos.'''
    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_lengh_invalid)
        assert str(exc_info.value) == f"O CPF deve ter 11 dígitos."

@pytest.mark.parametrize(
    "cpf_format_invalid",
    [
        "asdgfcvgbhn",
        "1235as456sd",
    ]
)
def test_cpf_invalid_format(cpf_format_invalid):
    '''Testa se o cpf contem apenas números.'''
    with pytest.raises(CPFInvalidError) as exc_info:
        CPF(cpf_format_invalid)
        assert str(exc_info.value) == f"O CPF deve conter apenas dígitos."

@pytest.mark.parametrize(
    "cpf_valid",
    [
        "12345678909",
        "52998224725"

    ]
)
def test_cpf_valid(cpf_valid):
    '''Testa se o cpf é valido.'''
    cpf = CPF(cpf_valid)
    assert cpf.numero == f"{cpf_valid[:3]}.{cpf_valid[3:6]}.{cpf_valid[6:9]}-{cpf_valid[9:]}"