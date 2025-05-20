from dataclasses import dataclass, field
from typing import List, Optional

from gerador_docs.errors import CPFInvalidError, CPFFormatError, CPFLengthError

class CPF:
    """
    Representa um CPF (Cadastro de Pessoas Físicas) brasileiro.
    """
    def __init__(self, numero: str):
        self.numero = self._validate(numero)

    def __str__(self):
        return self.numero
    
    def __repr__(self):
        cpf = self.numero.replace('.', '').replace('-', '')
        return f"<CPF(numero='{cpf}')>"
    
    def __eq__(self, other):
        if isinstance(other, CPF):
            return self.numero == other.numero
        return False
    
    def _validate(self, numero: str) -> str:
        """
        Valida o CPF.
        :param numero: CPF a ser validado.
        :return: CPF validado.
        :raises ValueError: Se o CPF for inválido.
        """
        try:
            self.verificar_repetidos(numero)
            self._verificar_tamanho(numero)
            self._verificar_digitos(numero)
            self._validar_primeiro_verificador(numero)
            self._validar_segundo_verificador(numero)
        except (CPFLengthError, CPFFormatError, CPFInvalidError) as e:
            raise ValueError(f"CPF inválido: {numero}. Erro: {str(e)}")            
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
        """
        # Verifica o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        primeiro_digito = 0 if resto == 10 else resto
        if primeiro_digito != int(cpf[9]):
            raise CPFInvalidError(f"CPF inválido: {cpf}. O primeiro dígito verificador é inválido.")
        return True
    
    def _validar_segundo_verificador(self, cpf: str) -> bool:
        """
        Valida o segundo dígito verificador do CPF.
        :return: True se o segundo dígito verificador for válido, False caso contrário.
        """
        # Verifica o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        segundo_digito = 0 if resto == 10 else resto
        if segundo_digito != int(cpf[10]):
            raise CPFInvalidError(f"CPF inválido: {cpf}. O segundo dígito verificador é inválido.")
        return True
    
    def _verificar_tamanho(self, cpf: str) -> bool:
        """
        Verifica o tamanho do CPF.
        :return: True se o tamanho do CPF for válido, False caso contrário.
        """
        if len(cpf) != 11:
            raise CPFLengthError(f"CPF inválido: {cpf}. O CPF deve ter 11 dígitos.")
        return True
    
    def _verificar_digitos(self, cpf: str) -> bool:
        """
        Verifica se o CPF contém apenas dígitos.
        :return: True se o CPF contiver apenas dígitos, False caso contrário.
        """
        if not cpf.isdigit():
            raise CPFFormatError(f"CPF inválido: {cpf}. O CPF deve conter apenas dígitos.")
        return True
    
    def verificar_repetidos(self, numero: str) -> bool:
        """
        Verifica se o CPF contém todos os dígitos iguais.
        :return: True se o CPF contiver todos os dígitos iguais, False caso contrário.
        """
        if len(set(numero)) == 1:
            raise CPFInvalidError(f"CPF inválido: {numero}. O CPF não pode conter todos os dígitos iguais.")
        return True
    
@dataclass
class Endereco:
    """
    Representa um endereço.
    """
    logradouro: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str = 'Feira Nova'
    estado: str = 'PE'
    cep: str = '55715-000'

# rever sobre dataclass