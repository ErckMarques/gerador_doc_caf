from argparse import ArgumentParser

import pytest

from gerador_docs.cli import _create_parser
from gerador_docs import CPF, DadosPessoais, Endereco, RG

@pytest.fixture(scope='module')
def endereco():
    """Fixture para criar um endereço de teste."""
    return Endereco(
        tag='residencial',
        bairro='Centro',
        logradouro='Rua das Flores',
        numero='123',
        complemento='Apto 1',
        cidade='Feira Nova',
        estado='PE',
        cep='55715-000'
    )

@pytest.fixture(scope='module')
def dados_pessoais(endereco):
    """Fixture para criar dados pessoais de teste."""
    return DadosPessoais(
        nome_completo='João da Silva',
        cpf=CPF('12345678909'),
        rg=RG('1047991', 'SSP', 'PE'),
        genero='M',
        estado_civil='solteiro',
        profissao='Engenheiro',
        endereco=[endereco]
    )

@pytest.fixture(scope='module')
def parser() -> ArgumentParser:
    """Fixture para criar o parser de argumentos."""
    return _create_parser()