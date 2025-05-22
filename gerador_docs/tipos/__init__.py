from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Union, Literal

from gerador_docs.errors import CPFInvalidError, CPFFormatError, CPFLengthError, RGFormatError
from gerador_docs.errors import GenderError, MaritalStatusError
from gerador_docs.tipos._typing import DadosPessoaisDict

Enderecos = Union[List['Endereco'], List[Dict[str, str]]]


class RG:
    """
    Representa um RG (Registro Geral) brasileiro.
    """
    def __init__(self, registro_geral: str, emissor: str, uf: str) -> None:
        self._num_rg = self._validar_digitos(registro_geral)
        self._emissor = emissor
        self._uf = uf

    def __str__(self) -> str:
        return self._num_rg + ' ' + self._emissor.upper() + ' / ' + self._uf.upper()

    def __repr__(self) -> str:
        return f'<RG(registro_geral={self._num_rg}, emissor={self._emissor}, uf={self._uf})>'
    
    def _validar_digitos(self, rg: str):
        rg_limpo = rg.replace(".", "").replace("-", "")
        if not rg_limpo.isdigit():
            raise RGFormatError(f"RG inválido: {rg}.")
        return rg_limpo
    
    def to_dict(self) -> Dict[str, str]:
        """Exporta o RG como um dicionário.
        :return: RG em formato de dicionário.
        """
        return {
            'numero': self._num_rg,
            'emissor': self._emissor,
            'uf': self._uf
        }

class CPF:
    """
    Representa um CPF (Cadastro de Pessoas Físicas) brasileiro.
    """
    def __init__(self, numero: str):
        self._numero = self._validate(numero)

    @property
    def numero(self) -> str:
        return self._numero

    def __str__(self):
        return self.numero
    
    def __repr__(self):
        cpf = self.numero.replace('.', '').replace('-', '')
        return f"<CPF(numero='{cpf}')>"
       
    def _validate(self, numero: str) -> str:
        """
        Valida o CPF.
        :param numero: CPF a ser validado.
        :return: CPF validado.
        :raises CPFInvalidError: Se o CPF for inválido.
        """
        try:
            self._verificar_repetidos(numero)
            self._verificar_tamanho(numero)
            self._verificar_digitos(numero)
            self._validar_primeiro_verificador(numero)
            self._validar_segundo_verificador(numero)
        except (CPFLengthError, CPFFormatError, CPFInvalidError) as e:
            raise CPFInvalidError(f"CPF inválido: {numero}. Erro: {str(e)}")            
        return self._formatar(numero)
    
    def _formatar(self, numero: str) -> str:
        """
        Formata o CPF.
        :return: CPF formatado.
        """
        return f"{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}"
    
    def _validar_primeiro_verificador(self, cpf: str) -> bool:
        """
        Valida o dígito verificador do CPF.
        :return: True se o dígito verificador for válido, False caso contrário.
        :raises CPFInvalidError: Se o dígito verificador for inválido.
        """
        # Verifica o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        primeiro_digito = 0 if resto == 10 else resto
        if primeiro_digito != int(cpf[9]):
            raise CPFInvalidError(f"O primeiro dígito verificador é inválido.")
        return True
    
    def _validar_segundo_verificador(self, cpf: str) -> bool:
        """
        Valida o segundo dígito verificador do CPF.
        :return: True se o segundo dígito verificador for válido, False caso contrário.
        :raises CPFInvalidError: Se o dígito verificador for inválido.
        """
        # Verifica o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        segundo_digito = 0 if resto == 10 else resto
        if segundo_digito != int(cpf[10]):
            raise CPFInvalidError(f"O segundo dígito verificador é inválido.")
        return True
    
    def _verificar_tamanho(self, cpf: str) -> bool:
        """
        Verifica o tamanho do CPF.
        :return: True se o tamanho do CPF for válido, False caso contrário.
        :raises CPFLengthError: Se o tamanho do CPF for inválido.
        """
        if len(cpf) != 11:
            raise CPFLengthError(f"O CPF deve ter 11 dígitos.")
        return True
    
    def _verificar_digitos(self, cpf: str) -> bool:
        """
        Verifica se o CPF contém apenas dígitos.
        :return: True se o CPF contiver apenas dígitos, False caso contrário.
        :raises CPFFormatError: Se o CPF contiver caracteres não numéricos.
        """
        if not cpf.isdigit():
            raise CPFFormatError(f"O CPF deve conter apenas dígitos.")
        return True
    
    def _verificar_repetidos(self, numero: str) -> bool:
        """
        Verifica se o CPF contém todos os dígitos iguais.
        :return: True se o CPF contiver todos os dígitos iguais, False caso contrário.
        :raises CPFInvalidError: Se o CPF contiver todos os dígitos iguais.
        """
        if len(set(numero)) == 1:
            raise CPFInvalidError(f"CPF inválido: {numero}. O CPF não pode conter todos os dígitos iguais.")
        return True
    
    def to_dict(self) -> Dict[str, str]:
        """Exporta o CPF como um dicionário.
        :return: CPF em formato de dicionário.
        """
        return {
            'numero': self.numero
        }
    
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
        return f'{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}/{self.estado}, CEP: {self.cep}'
    
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
    
    def to_dict(self):
        """Exporta o endereço como um dicionário.
        :return: Endereço em formato de dicionário.
        """
        return asdict(self)

@dataclass(repr=True, frozen=True)
class DadosPessoais:
    nome_completo: str
    cpf: CPF 
    rg: RG 
    genero: Literal['M', 'F', 'O']  # Masculino, Feminino ou Outro
    estado_civil: Literal['solteiro', 'casado', 'divorciado', 'viuvo']
    profissao: str
    endereco: Dict[Literal['residencial', 'trabalho'], List[Endereco]] = field(default_factory=dict)
    nacionalidade: str = field(init=False)

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
                'trabalho': [endereco]
            }
        )
        # print(endereco.to_dict())
        print(dados_pessoais.to_dict(), sort_dicts=False)
    except ValueError as e:
        print(e)
    except CPFInvalidError as e:
        print(e)