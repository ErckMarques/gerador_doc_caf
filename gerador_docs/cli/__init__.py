from argparse import ArgumentParser
from textwrap import dedent

from rich_argparse import RawDescriptionRichHelpFormatter

from gerador_docs.cli.parsers import config_subparsers as config_parser
from gerador_docs.cli._types import NamespaceMapper

def _create_parser() -> ArgumentParser:
    """
    Create and return an instance of ArgumentParser with the necessary subcommands.
    """
    parser = ArgumentParser(
        'docgen',
        description=dedent("""
            Gerador de Documentação para a emissão de CAF e Declarações de Agricultor
            e outros tipos de documentos comuns da Secretaria de Agricultura de Feira Nova-PE.
        """
        ),
        epilog='Use "docgen <comando> -h/--help" para mais informações sobre cada comando.',
        formatter_class=RawDescriptionRichHelpFormatter,
    )
    
    # Add subcommands
    config_parser(parser)
    
    return parser

def main() -> None:
    """
    Main function to execute the command line interface.
    """
    
    parser = _create_parser()
    
    try:
        from gerador_docs.cli.shell import clear

        clear()  # Clear the console before displaying the help message
        args = parser.parse_args(namespace=NamespaceMapper())

        print(
            dedent(f"""
            Comando: {args.command}
            Argumentos: {args.to_dict()}
            """
            )
        )
        
        # Here you would handle the parsed arguments and execute the corresponding actions
        # For now, we just print the parsed arguments

    except Exception as e:
        print(f"Erro ao processar os argumentos: {e}")
        parser.print_help()
        return
    else:
        from gerador_docs.cli.runners import DefaultRunner

        default_runner = DefaultRunner()
        getattr(default_runner, args.command)(vars(args))
