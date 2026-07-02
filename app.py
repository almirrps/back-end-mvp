from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Cliente, Endereco
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API de Cadastro de Clientes", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app, resources={r"/*": {"origins": ["null", "http://127.0.0.1:5000"]}})

# definindo tags
home_tag = Tag(name="Documentacao", description="Selecao de documentacao: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adicao, visualizacao e remocao de clientes a base")
endereco_tag = Tag(name="Endereco", description="Adicao de um endereco a um cliente cadastrado na base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentacao.
    """
    return redirect('/openapi')


@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """Adiciona um novo Cliente a base de dados

    Retorna uma representacao dos clientes e enderecos associados.
    """
    cliente = Cliente(
        nome = form.nome,
        sexo = form.sexo,
        cpf = form.cpf,
        idade = form.idade)
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexao com a base
        session = Session()
        # adicionando cliente
        session.add(cliente)
        # efetivando o comando de adicao de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome e a provavel razao do IntegrityError
        error_msg = "Cliente de mesmo nome ja salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Nao foi possivel salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.put('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_cliente(query: ClienteBuscaSchema, form: ClienteSchema):
    """Atualiza os dados de um Cliente existente na base de dados

    Retorna uma representacao do cliente atualizado.
    """
    
    nomeCli = query.nome
    
    logger.debug(f"Atualizando cliente de nome: '{nomeCli}'")
    try:
        # criando conexao com a base
        session = Session()
        
        # buscando o cliente existente pelo Nome
        cliente = session.query(Cliente).filter(Cliente.nome == nomeCli).first()
        
        # se o cliente nao for encontrado, retorna erro 404
        if not cliente:
            error_msg = "Cliente nao encontrado na base :/"
            logger.warning(f"Erro ao atualizar cliente Nome '{nomeCli}', {error_msg}")
            return {"mesage": error_msg}, 404

        # Atualizando os dados do cliente encontrado
        cliente.nome = form.nome
        cliente.sexo = form.sexo
        cliente.cpf = form.cpf
        cliente.idade = form.idade
           
        # efetivando o comando de atualizacao no banco
        session.commit()
        logger.debug(f"Cliente '{nomeCli}' atualizado com sucesso!")
        
        return apresenta_cliente(cliente), 200

    except Exception as e:
        # caso ocorra um erro fora do previsto (ex: quebra de constraint)
        session.rollback() # desfaz alteracoes em caso de erro
        error_msg = "Nao foi possivel atualizar o item :/"
        logger.warning(f"Erro ao atualizar cliente '{nomeCli}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_clientes():
    """Faz a busca por todos os Clientes cadastrados

    Retorna uma representacao da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")
    # criando conexao com a base
    session = Session()
    # fazendo a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # se nao ha clientes cadastrados
        return {"clientes": []}, 200
    else:
        logger.debug(f"%d clientes encontrados" % len(clientes))
        # retorna a representacao de cliente
        print(clientes)
        return apresenta_clientes(clientes), 200


@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):
    """Faz a busca por um Cliente a partir do id do cliente

    Retorna uma representacao dos clientes e enderecos associados.
    """
    cliente_nome = query.nome
    logger.debug(f"Coletando dados sobre cliente #{cliente_nome}")
    # criando conexao com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(Cliente.nome == cliente_nome).first()

    if not cliente:
        # se o cliente nao foi encontrado
        error_msg = "Cliente nao encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente '{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.nome}'")
        # retorna a representacao de cliente
        return apresenta_cliente(cliente), 200


@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_cliente(query: ClienteBuscaSchema):
    """Deleta um Cliente a partir do nome de cliente informado

    Retorna uma mensagem de confirmacao da remocao.
    """
    cliente_nome = unquote(unquote(query.nome))
    print(cliente_nome)
    logger.debug(f"Deletando dados sobre cliente #{cliente_nome}")
    # criando conexao com a base
    session = Session()
    # fazendo a remocao
    count = session.query(Cliente).filter(Cliente.nome == cliente_nome).delete()
    session.commit()

    if count:
        # retorna a representacao da mensagem de confirmacao
        logger.debug(f"Deletado cliente #{cliente_nome}")
        return {"mesage": "Cliente removido", "id": cliente_nome}
    else:
        # se o cliente nao foi encontrado
        error_msg = "Cliente nao encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente #'{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/endereco', tags=[endereco_tag],
          responses={"200": ClienteViewSchema, "404": ErrorSchema})
def add_endereco(form: EnderecoSchema):
    """Adiciona de um novo endereco a um cliente cadastrado na base identificado pelo id

    Retorna uma representacao dos clientes e enderecos associados.
    """
    cliente_id  = form.cliente_id
    logger.debug(f"Adicionando enderecos ao cliente #{cliente_id}")
    # criando conexao com a base
    session = Session()
    # fazendo a busca pelo cliente
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        # se cliente nao encontrado
        error_msg = "Cliente nao encontrado na base :/"
        logger.warning(f"Erro ao adicionar endereco ao cliente '{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o endereco
    logradouro = form.logradouro
    bairro = form.bairro
    cidade = form.cidade
    estado = form.estado
    endereco = Endereco(logradouro, bairro, cidade, estado)

    # adicionando o endereco ao cliente
    cliente.adiciona_endereco(endereco)
    session.commit()

    logger.debug(f"Adicionado endereco ao cliente #{cliente_id}")

    # retorna a representacao de cliente
    return apresenta_cliente(cliente), 200
