from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Union, Literal

from gerador_docs.tipos.documents  import CPF, RG

from gerador_docs.errors import CPFInvalidError
from gerador_docs.errors import GenderError, MaritalStatusError
from gerador_docs.tipos._typing import DadosPessoaisDict, EnderecoDict

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

@dataclass(repr=True, frozen=True, init=False)
class DadosPessoais:
    nome_completo: str
    cpf: CPF 
    rg: RG 
    genero: Literal['M', 'F', 'O']  # Masculino, Feminino ou Outro
    estado_civil: Literal['solteiro', 'casado', 'divorciado', 'viuvo']
    profissao: str
    endereco: Dict[Optional[Literal['residencial', 'trabalho']], List[Endereco]] = field(default_factory=dict)
    nacionalidade: str = field(init=False)

    def __init__(self, nome_completo: str, cpf: CPF, rg: RG, genero: str, estado_civil: str, profissao: str, endereco: Enderecos):
        """Inicializa os dados pessoais.
        :param nome_completo: Nome completo da pessoa.
        :param cpf: CPF da pessoa.
        :param rg: RG da pessoa.
        :param genero: Gênero da pessoa (M, F ou O).
        :param estado_civil: Estado civil da pessoa (solteiro, casado, divorciado ou viuvo).
        :param profissao: Profissão da pessoa.
        :param endereco: Endereço(s) da pessoa (residencial e/ou trabalho).
        """

        # Processamento do endereco
        enderecos_processados = {'residencial': [], 'trabalho': []}
        # Suporta tanto lista quanto dict para o argumento endereco
        if isinstance(endereco, dict):
            for tag, lista in endereco.items():
                if tag not in enderecos_processados:
                    continue
                for item in lista:
                    if isinstance(item, dict):
                        end = Endereco(**item)
                    else:
                        end = item
                    enderecos_processados[tag].append(end)
        elif isinstance(endereco, list):
            for item in endereco:
                if isinstance(item, dict):
                    end = Endereco(**item)
                else:
                    end = item
                if hasattr(end, 'tag') and end.tag in enderecos_processados:
                    enderecos_processados[end.tag].append(end)
        else:
            raise ValueError("O argumento 'endereco' deve ser uma lista ou um dicionário.")

        object.__setattr__(self, 'nome_completo', nome_completo)
        object.__setattr__(self, 'cpf', cpf)
        object.__setattr__(self, 'rg', rg)
        object.__setattr__(self, 'genero', genero)
        object.__setattr__(self, 'estado_civil', estado_civil)
        object.__setattr__(self, 'profissao', profissao)
        object.__setattr__(self, 'endereco', enderecos_processados)
        object.__setattr__(self, 'nacionalidade', None)  # Inicializa como None, será definido no __post_init__

        self.__post_init__()

    def __post_init__(self):
        """Método chamado após a inicialização do dataclass.
        Valida os dados pessoais e define a nacionalidade com base no gênero.
        """
        object.__setattr__(self, 'nacionalidade', 'brasileira' if self.genero == 'F' else 'brasileiro')
        if len(self.genero) != 1:
            raise GenderError(f"Valor inválido para gênero: {self.genero}. Deve ser 'M', 'F' ou 'O'.")
        if self.estado_civil not in ('solteiro', 'casado', 'divorciado', 'viuvo'):
            raise MaritalStatusError(f"Valor inválido para estado civil: {self.estado_civil}. Deve ser 'solteiro', 'casado', 'divorciado' ou 'viuvo'.")

    @property
    def numero_cpf(self) -> str:
        """Retorna o número do CPF."""
        return self.cpf.numero
    
    @property
    def numero_rg(self) -> str:
        """Retorna o número do RG + EMISSOR."""
        return str(self.rg)

    @property
    def endereco_completo(self) -> List[str]:
        """Retorna o(s) endereço(s) completo(s)."""
        return [str(end) for end in self.endereco]

    def to_dict(self) -> DadosPessoaisDict:
        """Exporta os dados pessoais como um dicionário.
        :return: Dados pessoais em formato de dicionário.
        """
        return {
            'nome_completo': self.nome_completo,
            'genero': self.genero,
            'estado_civil': self.estado_civil,
            'profissao': self.profissao,
            'nacionalidade': self.nacionalidade,
            'cpf': self.cpf.to_dict(),
            'rg': self.rg.to_dict(),
            'endereco': {
                'residencial': [endereco.to_dict() for endereco in self.endereco.get('residencial', [])],
                'trabalho': [endereco.to_dict() for endereco in self.endereco.get('trabalho', [])],
            },
        }

if __name__ == '__main__':
    from pprint import pprint as print
    # Exemplo de uso
    try:
        cpf = CPF('12345678909') # CPF válido -> 123.456.789-09
        rg = RG('1047991', 'SSP', 'PE')
        endereco = Endereco(tag='trabalho', bairro='Centro', logradouro='Rua Joaquim Correia', complemento='Prédio Público') # Rua Joaquim Correia, S/N, Centro, Feira Nova/PE, CEP: 55715-000
        endereco2 = Endereco(tag='residencial', bairro='Zona Rural', logradouro='Sítio Cachoeira do Salobro')
        dados_pessoais = DadosPessoais(
            nome_completo='João da Silva', 
            genero='M', 
            estado_civil='solteiro', 
            profissao='agricultor', 
            cpf=cpf, 
            rg=rg, 
            endereco={
                'residencial': [endereco2],
                'trabalho': [endereco],
            }
        )
        # print(endereco.to_dict())
        print(dados_pessoais.to_dict(), sort_dicts=False)
    except ValueError as e:
        print(e)
    except CPFInvalidError as e:
        print(e)