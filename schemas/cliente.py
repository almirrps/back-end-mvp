from pydantic import BaseModel
from typing import Optional, List
from model.cliente import Cliente

from schemas import EnderecoSchema


class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Antonio Silva"
    sexo: str = "masculino"
    cpf: str = "459.006.028-00"
    idade: Optional[int] = 49

class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que sera
        feita apenas com base no nome do cliente.
    """
    nome: str = "Teste"


class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes sera retornada.
    """
    clientes:List[ClienteSchema]


def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representacao do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "nome": cliente.nome,
            "sexo": cliente.sexo,
            "cpf": cliente.cpf,
            "idade": cliente.idade,
        })

    return {"clientes": result}


class ClienteViewSchema(BaseModel):
    """ Define como um cliente sera retornado: cliente + enderecos.
    """
    id: int = 1
    nome: str = "Antonio Silva"
    sexo: str = "masculino"
    cpf: str = "459.006.028-00"
    idade: Optional[int] = 49
    total_enderecos: int = 1
    enderecos:List[EnderecoSchema]


class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado apos uma requisicao
        de remocao.
    """
    message: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representacao do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "sexo": cliente.sexo,
        "cpf": cliente.cpf,
        "idade": cliente.idade,
        "total_enderecos": len(cliente.enderecos),
        "enderecos": [{"logradouro": c.logradouro, "bairro": c.bairro, "cidade": c.cidade,
                       "estado": c.estado} for c in cliente.enderecos]
    }
