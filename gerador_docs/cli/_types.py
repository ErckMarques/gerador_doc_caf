"Provides dict-like mapper types and functions for parser.args"
from argparse import Namespace
from typing import Any, Literal, TypedDict, NotRequired, Union, Required

class NamespaceDictLikeDB(TypedDict):
    command: str
    table: NotRequired[str]
    dados: NotRequired[str]
    action: Literal["add", "remove", "update", "list"]

NamespaceDictLike = {
    "db": NamespaceDictLikeDB,
}

class NamespaceMapper(Namespace):
    """
    Esta classe herda de argparser.Namespace extendendo-a com um método to_dict, que retorna um objeto
    NamespaceDictLike[command], onde 'command' é o nome do comando utilizado no parser.

    uso pretendido:
        args = parser.parse_args(namespace=MyNamespace)
        args -> args.to_dict() # if command db, e.g., type(args) -> NamespaceDictLikeDB[TypedDict]
    """

    def __init__(self, **kwargs) -> None:
        super().__init__() # chamada mantida por segurança
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self,) -> Union[NamespaceDictLikeDB, None]:
        cmd = getattr(self, 'command', None)
        cls = NamespaceDictLike.get(cmd)
        if cls is None:
            return None
        return cls(**vars(self))
