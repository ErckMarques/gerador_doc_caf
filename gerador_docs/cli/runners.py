from argparse import Namespace

class DefaultRunner:
    def poco(self, args: Namespace) -> None:
        print(f"Executando comando 'poco' com os argumentos: {args}")

    def db(self, args: Namespace) -> None:
        print(f"Executando comando 'db' com os argumentos: {args}")
