from argparse import Namespace

class DefaultRunner:
    def poco(self, args: Namespace) -> None:
        print(f"Executando comando 'poco' com os argumentos: {args}")

    def db(self, args: Namespace) -> None:
        print(f"Executando comando 'db' com os argumentos: {args}")

    def dec(self, args: Namespace) -> None:
        print(f"Executando comando 'dec' com os argumentos: {args}")
    
    def pagamento(self, args: Namespace) -> None:
        print(f"Executando comando 'pagamento' com os argumentos: {args}")
    
    def caf(self, args: Namespace) -> None:
        print(f"Executando comando 'caf' com os argumentos: {args}")

