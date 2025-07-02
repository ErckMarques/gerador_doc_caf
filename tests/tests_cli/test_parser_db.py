from argparse import ArgumentParser, Namespace
import shlex

from gerador_docs.cli import NamespaceMapper

def test_commands_db(parser: ArgumentParser):
    args: Namespace = parser.parse_args(
        shlex.split(
            "db users --dados valor1 --dados valor2 --action update"
        )
    )

    assert args.command == 'db'
    assert args.table == 'users'
    assert args.action == 'update'
    assert isinstance(args.dados, list)
    assert len(args.dados) <= 2

def test_others_forms_of_arguments_for_data(parser: ArgumentParser):
    args: Namespace = parser.parse_args(
        shlex.split(
            "db users --dados valor1 valor2 --dados nome:valor1 idade:valor2  ci:valor3 --dados nome:valor1,idade:valor2,ci:valor3 --action update"
        )
    )
    # o que separa os valores são os espaços em branco
    assert args.dados[0] == ["valor1", "valor2"]
    assert args.dados[1] == ['nome:valor1', 'idade:valor2', 'ci:valor3']
    assert args.dados[2] == ['nome:valor1,idade:valor2,ci:valor3']

def test_integration_with_NamespaceMapper(parser: ArgumentParser):

    args = parser.parse_args(
        shlex.split(
            "db users --dados valor1 --dados valor2 --action update"
        ),
        namespace=NamespaceMapper()
    )

    args = args.to_dict()

    assert isinstance(args, dict)
    assert args.get('command', False), "O argumento command não foi devidamente analisado"
    assert args.get('table', False), "O argumento table não foi devidamente analisado"
    assert args.get('action', False), "O argumento action não foi devidamente analisado"
    assert all(isinstance(item, list) for item in args.get('dados', default="")), "O argumento dados não foi devidamente analisado"    