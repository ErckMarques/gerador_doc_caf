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

def create_db():
    db = TinyDB()


class TinyDbRepository:
    
    def __init__(self, db: TinyDB) -> None:
        self._db = db