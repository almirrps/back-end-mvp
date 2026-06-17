from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    logradouro = Column(String(4000))
    bairro = Column(String(4000))
    cidade = Column(String(4000))
    estado = Column(String(2))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definicao do relacionamento entre o endereco e um cliente.
    # Aqui esta sendo definido a coluna 'cliente' que vai guardar
    # a referencia ao cliente, a chave estrangeira que relaciona
    # um cliente ao endereco.
    cliente = Column(Integer, ForeignKey("cliente.pk_cliente"), nullable=False)

    def __init__(self, logradouro:str, bairro:str, cidade:str, estado:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Endereco

        Arguments:
            logradouro: o endereco do cliente.
            bairro: o bairro do cliente.
            cidade: a cidade do cliente.
            estado: UF
            data_insercao: data de quando o endereco foi inserido
                           à base
        """
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        if data_insercao:
            self.data_insercao = data_insercao
