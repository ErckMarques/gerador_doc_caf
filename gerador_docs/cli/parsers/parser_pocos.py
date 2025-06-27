from argparse import ArgumentParser, _SubParsersAction
from argparse import ONE_OR_MORE

from rich_argparse import RawDescriptionRichHelpFormatter

def poco_subparser(subparser: _SubParsersAction) -> ArgumentParser:

    poco_subparser: ArgumentParser = subparser.add_parser(
        "poco",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à emissão dos documentos e dados dos responsáveis pelos poços."
    )

    poco_subparser.set_defaults(
        command="poco",
    )

    poco_subparser.add_argument(
        "pag",
        help="gera a solicitação de pagamento para um ou mais poços".capitalize(),
        nargs=ONE_OR_MORE,
    )

    return poco_subparser