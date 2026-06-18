from pydantic import BaseModel


class EnderecoSchema(BaseModel):
    """ Define como um novo endereco a ser inserido deve ser representado
    """
    cliente_id: int = 1
    logradouro: str = "Rua das Flores, 31"
    bairro: str = "Bairro Jardins"
    cidade: str = "Sao Paulo"
    estado: str = "SP"

