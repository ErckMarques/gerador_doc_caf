
def test_dados_pessoais(dados_pessoais):
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