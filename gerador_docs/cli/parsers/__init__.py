
from argparse import ArgumentParser

from .parser_pocos import poco_subparser

def config_subparsers(parser: ArgumentParser) -> None: 
    subparser = parser.add_subparsers(dest="command", required=True,)

    poco_subparser(subparser)
