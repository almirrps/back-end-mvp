from pydantic import BaseModel
from typing import Optional


class EnderecoSchema(BaseModel):
    """ Define como um novo endereco a ser inserido deve ser representado
    """
    cliente_id: int = 1
    logradouro: str = "Rua das Flores, 31"
    bairro: str = "Bairro Jardins"
    cidade: str = "Sao Paulo"
    estado: str = "SP"

class EnderecoUpdateSchema(BaseModel):
    """ Define como um novo endereço a ser atualizado deve ser representado.
    """
    id: int  
    cliente_id: int
    logradouro: str
    bairro: str
    cidade: str
    estado: str