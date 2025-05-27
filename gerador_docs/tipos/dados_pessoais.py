from dataclasses import dataclass, field
from typing import List, Optional, Dict, Union, Literal

from gerador_docs.tipos.documents  import CPF, RG
from gerador_docs.tipos.endereco import Endereco, Enderecos
from gerador_docs.errors import GenderError, MaritalStatusError
from gerador_docs.tipos._typing import DadosPessoaisDict


@dataclass(frozen=True, init=False, kw_only=True)
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
        :param genero: Gênero da pessoa (M/m, F/f ou O/o).
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
        
        self._normalizar_e_validar_genero(genero)

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
    
    def _normalizar_e_validar_genero(self, genero: str) -> Union[str, GenderError]:
        """Normaliza e valida o gênero.
        :param genero: Gênero a ser normalizado e validado.
        :return: Gênero normalizado.
        :raises GenderError: Se o gênero não for válido.
        """
        genero = genero.upper()
        if genero not in ('M', 'F', 'O'):
            raise GenderError(f"Valor inválido para gênero: {genero}. Deve ser 'M', 'F' ou 'O'.")
        return genero

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
