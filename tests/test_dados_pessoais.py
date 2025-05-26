import pytest

from dataclasses import replace

from gerador_docs import DadosPessoais
from gerador_docs.errors import MaritalStatusError, GenderError

def test_dados_pessoais(dados_pessoais: DadosPessoais):
    """Testa a criação e representação dos dados pessoais."""
    
    assert dados_pessoais.nome_completo == 'João da Silva'
    assert dados_pessoais.numero_cpf == '123.456.789-09'
    assert dados_pessoais.numero_rg == '1047991 SSP/PE'
    assert dados_pessoais.genero == 'M'
    assert dados_pessoais.estado_civil == 'solteiro'
    assert dados_pessoais.profissao == 'Engenheiro'
    
    # Verifica o endereço
    endereco_residencial = dados_pessoais.endereco.get('residencial', [])
    assert len(endereco_residencial) == 1
    assert str(endereco_residencial[0]) == 'Rua das Flores, 123, Centro, Feira Nova/PE CEP: 55715-000'
    
    # Verifica a exportação para dicionário
    expected_dict = {
        'nome_completo': 'João da Silva',
        'cpf': {'numero':dados_pessoais.numero_cpf},
        'rg': {'numero': dados_pessoais.numero_rg},
        'genero': 'M',
        'estado_civil': 'solteiro',
        'profissao': 'Engenheiro',
        'endereco': {
            'residencial': [endereco_residencial[0].to_dict()],
            'trabalho': []
        },
        'nacionalidade': "brasileiro"
    }
    
    assert dados_pessoais.to_dict() == expected_dict

@pytest.mark.parametrize("marital_status_alt", ["amigado", "mora junto"])
def test_exception_MaritalStatusError(dados_pessoais: DadosPessoais, marital_status_alt):
    """Testa a exceção de estado civil inválido."""
    
    with pytest.raises(MaritalStatusError, match="Valor inválido para estado civil"):
        replace(dados_pessoais, estado_civil=marital_status_alt)

def test_exception_GenderError(dados_pessoais: DadosPessoais):
    """Testa a exceção de gênero inválido."""

    with pytest.raises(GenderError, match="Valor inválido para gênero"):
        replace(dados_pessoais, genero='X')