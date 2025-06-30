from argparse import ArgumentParser

import shlex

def test_command_remove(parser: ArgumentParser) -> None:
    """
    Test the 'remove' command functionality.
    """
    args = parser.parse_args(shlex.split("db --table pocos -r ci1 id1 ci2 id2"))

    assert args.command == "db"
    assert args.table == "pocos"
    assert isinstance(args.remove, list)
    assert args.remove == ['ci1', 'id1', 'ci2', 'id2']

    # Here you would typically call the function that handles the 'remove' command
    # and check if it behaves as expected, e.g., removing a record from the database.