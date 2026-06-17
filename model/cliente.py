from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Endereco

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    sexo = Column(String(140))
    cpf = Column(String(140))
    idade = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definicao do relacionamento entre o cliente e o endereco.
    # Essa relacao e implicita, nao esta salva na tabela 'cliente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    enderecos = relationship("Endereco")

    def __init__(self, nome:str, sexo:str, cpf:str, idade:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Cliente

        Arguments:
            nome: nome do cliente.
            sexo: sexo do cliente.
            cpf: cpf dp cliente.
            idade: idade do cliente
            data_insercao: data de quando o cliente foi inserido a base
        """
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade

        # se nao for informada, sera o data exata da insercao no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_endereco(self, endereco:Endereco):
        """ Adiciona um novo Endereco ao Cliente
        """
        self.enderecos.append(endereco)

