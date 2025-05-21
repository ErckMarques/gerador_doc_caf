class CPFInvalidError(Exception):
    """Exception raised for invalid CPF numbers."""
    pass

class CPFFormatError(Exception):
    """Exception raised for invalid CPF format."""
    pass

class CPFLengthError(Exception):
    """Exception raised for invalid CPF length."""
    pass

class RGFormatError(Exception):
    """Exception raised for invalid RG format."""
    pass