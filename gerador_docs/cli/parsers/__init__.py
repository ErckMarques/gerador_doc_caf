from argparse import ArgumentParser

from .parser_db import db_subparser
from .parser_pocos import poco_subparser

def config_subparsers(parser: ArgumentParser) -> None: 
    subparser = parser.add_subparsers(dest="command", required=True,)

    db_subparser(subparser)
    poco_subparser(subparser)
