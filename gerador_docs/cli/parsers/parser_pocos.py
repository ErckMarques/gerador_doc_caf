from argparse import ArgumentParser, _SubParsersAction
from argparse import ONE_OR_MORE

from rich_argparse import RawDescriptionRichHelpFormatter

def poco_subparser(subparser: _SubParsersAction) -> ArgumentParser:

    poco_subparser: ArgumentParser = subparser.add_parser(
        "poco",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à emissão das solicitações de pagamento dos poços."
    )

    poco_subparser.set_defaults(
        command="poco",
    )

    return poco_subparser