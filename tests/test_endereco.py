import pytest

from gerador_docs import Endereco

def test_endereco_str(endereco: Endereco):
    """Testa a representação em string do endereço."""
    
    assert str(endereco) == 'Rua das Flores, 123, Centro, Feira Nova/PE CEP: 55715-000'

def test_endereco_to_dict(endereco: Endereco):
    """Testa a exportação do endereço como dicionário."""
    expected_dict = {
        'tag': 'residencial',
        'bairro': 'Centro',
        'logradouro': 'Rua das Flores',
        'numero': '123',
        'complemento': 'Apto 1',
        'cidade': 'Feira Nova',
        'estado': 'PE',
        'cep': '55715-000'
    }
    
    assert endereco.to_dict() == expected_dict