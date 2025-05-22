from typing import List, Optional, Dict, Literal, TypedDict

class EnderecoDict(TypedDict):
    tag: Literal['residencial', 'trabalho']
    bairro: str
    logradouro: str
    numero: str
    complemento: Optional[str]
    cidade: str
    estado: str
    cep: str

class DadosPessoaisDict(TypedDict):
    nome_completo: str
    genero: Literal['M', 'F', 'O']
    estado_civil: Literal['solteiro', 'casado', 'divorciado', 'viuvo']
    profissao: str
    nacionalidade: str
    cpf: Dict[str, str]
    rg: Dict[str, str]
    endereco: Dict[Literal['residencial', 'trabalho'], List[EnderecoDict]]