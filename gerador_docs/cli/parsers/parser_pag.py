from argparse import ArgumentParser, _SubParsersAction
from rich_argparse import RawDescriptionRichHelpFormatter

def declaracao_subparser(subparser: _SubParsersAction) -> ArgumentParser:
    declaracao_subparser: ArgumentParser = subparser.add_parser(
        "pagamento",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à emissão das solicitações de pagamento emitidas pela secretaria."
    )

    declaracao_subparser.set_defaults(
        command="pagamento",
    )

    return declaracao_subparser