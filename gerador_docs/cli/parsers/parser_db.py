from argparse import ArgumentParser, _SubParsersAction
from argparse import ONE_OR_MORE

from rich_argparse import RawDescriptionRichHelpFormatter

def db_subparser(subparser: _SubParsersAction) -> ArgumentParser:
    db_subparser: ArgumentParser = subparser.add_parser(
        "db",
        formatter_class=RawDescriptionRichHelpFormatter,
        help="Comandos relacionados à manipulação dos dados dos poços e seus responsáveis (CRUD)."
    )

    db_subparser.set_defaults(
        command="db",
    )

    db_subparser.add_argument(
        "-t", "--table",
        help="Nome da tabela a ser manipulada",
        required=True,
        metavar="table name".upper(),
    )

    db_subparser.add_argument(
        "-a", "--add",
        help="adiciona as informações de um poço",
        nargs=ONE_OR_MORE,
        action="append",
        metavar="resp local ci".upper(),
    )

    db_subparser.add_argument(
        "-r", "--remove",
        help="remove as informações de um poço",
        nargs=ONE_OR_MORE,
        metavar="id / ci".upper(),
    )  

    db_subparser.add_argument(
        "-u", "--update",
        help="atualiza as informações de um poço",
        nargs=ONE_OR_MORE,
        metavar="id / ci".upper(),
    )
    
    # lista as informações de um poço
    db_subparser.add_argument(
        "-l", "--list",
        metavar="id / ci".upper(),
        help="lista as informações de um poço",
    )

    return db_subparser