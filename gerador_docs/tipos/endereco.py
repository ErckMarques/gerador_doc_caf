from dataclasses import dataclass
from typing import Dict, List, Literal, Optional, Union

from gerador_docs.tipos._typing import EnderecoDict

Enderecos = Union[List['Endereco'], Dict[Optional[Literal['residencial', 'trabalho']], List['Endereco']]]

@dataclass(frozen=True)
class Endereco:
    """
    Representa um endereço.
    """
    tag: Literal['residencial', 'trabalho']
    bairro: str
    logradouro: str
    numero: str = 'S/N'
    complemento: Optional[str] = None
    cidade: str = 'Feira Nova'
    estado: str = 'PE'
    cep: str = '55715-000'

    def __str__(self) -> str:
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}/{self.estado} CEP: {self.cep}'
    
    def __format__(self, format_spec: str) -> str:
        """Formata o endereço de acordo com a especificação.
        
        format_spec pode ser:
        - 'short': apenas logradouro, número e cidade (Rua Joaquim Correia, S/N, Feira Nova)
        - 'default': formato completo
        - 'oneline': tudo em uma linha sem quebras
        """
        if format_spec == 'short':
            return f"{self.logradouro}, {self.numero}, {self.cidade}"
        elif format_spec == 'oneline':
            return str(self).replace('\n', ' ')
        else:  # default
            return str(self)
    
    def to_dict(self) -> EnderecoDict:
        """Exporta o endereço como um dicionário.
        :return: Endereço em formato de dicionário.
        """
        return {
            'tag': self.tag,
            'bairro': self.bairro,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'complemento': self.complemento,
            'cidade': self.cidade,
            'estado': self.estado,
            'cep': self.cep
        }