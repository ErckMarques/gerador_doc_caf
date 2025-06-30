from argparse import ArgumentParser, _SubParsersAction
from rich_argparse import RawDescriptionRichHelpFormatter

def caf_subparser(subparser: _SubParsersAction) -> ArgumentParser:

    caf_subparser: ArgumentParser = subparser.add_parser(
        "caf",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à emissão dos documentos relacionados ao CAF."
    )

    caf_subparser.set_defaults(
        command="caf",
    )

    return caf_subparser