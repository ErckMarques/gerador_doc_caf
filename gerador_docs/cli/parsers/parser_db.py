from argparse import ArgumentParser, _SubParsersAction, ONE_OR_MORE

import textwrap

def db_subparser(subparser: _SubParsersAction, /, formatter_class) -> ArgumentParser:
    db_parser: ArgumentParser = subparser.add_parser(
        "db",
        formatter_class=formatter_class,
        description=textwrap.dedent(
            """
            Use este comando para adicionar, remover, atualizar ou listar dados em tabelas específicas.
            Os dados devem ser fornecidos como argumentos adicionais atravéa do argumento posicional '--dados',
            e a ação a ser executada deve ser especificada pelo argumento [blue]OBRIGATÓRIO[/] '--action'.
            
            As ações disponíveis são:
                - add: Adiciona novos dados à tabela.
                - remove: Remove dados da tabela.
                - update: Atualiza dados existentes na tabela.
                - list: Lista os dados da tabela, ou os nomes das tabelas + descrição disponíveis (em estudo de viabilização).
            Cada ação requer que você forneça os dados necessários através do argumento '--dados'.
            
            [yellow]IMPORTANTE: O argumento '--dados' pode ser usado múltiplas vezes para fornecer vários valores.[/]
            
            [red]ATENÇÃO[/]: 
                ao utilizar [green]'--action remove'[/] -> [green]'--dados'[/] deve receber um identificador ou vários identificadores 
                que permita identificar o dado no banco de dados. Em caso de dúvidas sobre o identificador utilize: [green]'--action list'[/].
            """
        ),
        usage=textwrap.dedent(
            """
            Exemplos de uso:
                1. Adicionar valores a uma tabela:
                    - %(prog)s NOME_TABELA --dados VALOR1 --action add
                    - %(prog)s NOME_TABELA --dados VALOR1 --dados VALOR2 --action add
                2. Remover/Atualizar valores a uma tabela:
                    - %(prog)s NOME_TABELA --dados VALOR1 --action remove
                    - %(prog)s NOME_TABELA --dados VALOR1 --dados VALOR2 --action remove
                    - %(prog)s NOME_TABELA --dados VALOR1 --dados VALOR2 --action update
                3. Listar registros de uma tabela
                    - %(prog)s NOME_TABELA --action list
                4. Listar todas as tabelas disponiveis
                    - %(prog)s --action list (em estudo de viabilização)
            """
        ),
        help="Comandos relacionados à manipulação dos dados dos poços e seus responsáveis (CRUD)."
    )

    db_parser.set_defaults(command="db")

    # Argumento posicional obrigatório: nome da tabela
    db_parser.add_argument(
        "table",
        default=None,
        help="Nome da tabela a ser manipulada",
        metavar="NOME_TABELA",
    )

    # Argumento opcional repetível: dados
    db_parser.add_argument(
        "--dados",
        help="Dados a serem manipulados. Pode ser usado múltiplas vezes.",
        default=None,
        nargs=ONE_OR_MORE,
        action="append",
        metavar="VALORES"
    )

    # Ação CRUD como uma única opção com choices
    db_parser.add_argument(
        "--action",
        metavar='ACTION',
        choices=["add", "remove", "update", "list"],
        help="Ação a ser executada na tabela."
    )

    return db_parser

# todo: função de validação dos dados para cada ação.
# todo: add rich elements for terminal exibition