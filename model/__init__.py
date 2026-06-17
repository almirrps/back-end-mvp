from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.endereco import Endereco
from model.cliente import Cliente

db_path = "database/"
# Verifica se o diretorio nao existe
if not os.path.exists(db_path):
   # entao cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa e uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexao com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de secao com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele nao existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso nao existam
Base.metadata.create_all(engine)
