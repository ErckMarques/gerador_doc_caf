from argparse import ArgumentParser

import shlex

def test_command_add(parser: ArgumentParser) -> None:
    """
    Test the 'add' command functionality.
    """
    args = parser.parse_args(shlex.split("db --table pocos -a resp1 local1 ci1 -a resp2 local2 ci2"))
    
    assert args.command == "db"
    assert args.table == "pocos"
    assert isinstance(args.add, list)
    assert len(args.add) == 2
    
    # Here you would typically call the function that handles the 'add' command
    # and check if it behaves as expected, e.g., adding a record to the database.

def test_command_add_with_different_format(parser: ArgumentParser) -> None:
    """
    Test the 'add' command functionality with a different format.
    """
    args = parser.parse_args(shlex.split("db --table pocos -a resp1,local1,ci1"))

    assert args.command == "db"
    assert args.table == "pocos"
    assert isinstance(args.add, list)
    assert args.add != [["resp1", "local1", "ci1"]], f"args.add is {args.add}" # args.add -> [['resp1,local1,ci1']]