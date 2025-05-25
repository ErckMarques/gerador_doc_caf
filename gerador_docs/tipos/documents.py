
from typing import Dict
from gerador_docs.errors import CPFInvalidError, CPFFormatError, CPFLengthError, RGFormatError



class RG:
    """
    Representa um RG (Registro Geral) brasileiro.
    """
    def __init__(self, registro_geral: str, emissor: str, uf: str) -> None:
        self._num_rg = self._validar_digitos(registro_geral)
        self._emissor = emissor
        self._uf = uf

    @property
    def num_rg(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self._num_rg + ' ' + self._emissor.upper() + '/' + self._uf.upper()

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
            'numero': self.__str__(),
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
        return self._numero
    
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
            self._verificar_digitos(numero)
            self._verificar_repetidos(numero)
            self._verificar_tamanho(numero)
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
    
class CAR: pass

class CAF: pass