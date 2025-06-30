from argparse import ArgumentParser, _SubParsersAction
from rich_argparse import RawDescriptionRichHelpFormatter

def declaracao_subparser(subparser: _SubParsersAction) -> ArgumentParser:

    declaracao_subparser: ArgumentParser = subparser.add_parser(
        "dec",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à emissão das declarações de pescador/agricultor."
    )

    declaracao_subparser.set_defaults(
        command="dec",
    )

    return declaracao_subparser