from pathlib import Path

from tinydb import TinyDB, Query
from tinydb.table import Document


"""
Este pacote python contém as lógicas para integração com a persistência de dados
no primeiro momento utilizerei por padrão o tinydb, a medida que o software for aumentando
vamos trocar para o sqlite e, se necessário, para um ORM ou outro banco de maior porte.

Começarei utilizando o REPOSITORY PATTERN para poder trocar entre o tinydb e o sqlite facilmente. 
Contudo, percebi que antes de definir como vou fazer as coisas, preciso voltar e definir melhor os tipos de dados
ou a forma como vou inserir dados apartir da CLI e as tabelas que serão utilizadas. 
"""

_INSTANCE_PATH = Path(__file__).parent / 'instance'

if not _INSTANCE_PATH.exists():
    _INSTANCE_PATH.mkdir()

def create_engine(db_path_or_uri: Path | str):
    """Esta tem por proposito realizar configurações e instanciar o objeto de conexao com o banco de dados.
    Args:
        db_path_or_uri (Path | str): 
            string ou objeto Path de caminho do banco ou arquivo de banco de dados ou nome do banco de dados, por padrão, 
            se passado apenas 'meu_banco.json', ele é criado na raiz do projeto dentro de './instance/'.
            ou string URI semelhante à utilizada no sqlalchemy, mysql ou postgressql.
    
            Ex.: db_path_or_uri='tinydb+aiotinydb://instance/dados.json'
            Ex.: db_path_or_uri='sgbd+extension://instance/dados.json'

    """
    global _INSTANCE_PATH

    def select_repository(): 
        """Factory que retorna uma instancia de IRepository, especificada na URI de conexão, por padrão trabalha com o tinydb."""
        pass



class TinyDbRepository:
    
    def __init__(self, db: TinyDB) -> None:
        self._db = db