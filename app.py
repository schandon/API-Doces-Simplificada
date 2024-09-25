from email.mime import base
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS
from flask import redirect
from model.produto import Produto
from model.cliente import Cliente
from model.pedido import Pedido
from model import Session
from schemas.produto import *
from schemas.error import *
from schemas.pedido import *
from schemas.cliente import *
from logger import logger


info = Info(title="Api Doces", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes da base")
pedido_tag = Tag(name="Pedido", description="Adição, visualização e remoção de Peiddos da base")

@app.get('/')
def home():
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    session = Session()
    produto = Produto(
        nome=form.nome,
        descricao=form.descricao,
        valor=form.valor,
        imagem_path=form.imagem,
        quantidade=form.quantidade
        )
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
    except IntegrityError as e:
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um Produto a partir do id do produto

    Retorna uma representação dos produtos e comentários associados.
    """
    produto_id = query.id
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Produto econtrado: '{produto.nome}'")
        return apresenta_produto(produto), 200


@app.get('/produtos', tags=[produto_tag],
         responses={"200": ProdutoListaViewSchema, "404": ErrorSchema})
def get_produtos():
    """Lista todos os produtos cadastrados na base

    Retorna uma lista de representações de produtos.
    """
    logger.debug(f"Coletando lista de produtos")
    session = Session()
    produtos = session.query(Produto).all()
    print(produtos)
    if not produtos:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de produtos. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de produtos")
        return apresenta_lista_produto(produtos), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    produto_id = query.id
    produto_nome = query.nome

    logger.debug(f"Deletando dados sobre produto #{produto_id}")
    session = Session()

    if produto_id:
        count = session.query(Produto).filter(Produto.id == produto_id).delete()
    else:
        count = session.query(Produto).filter(Produto.nome == produto_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado produto #{produto_id}")
        return {"mesage": "Produto removido", "id": produto_id}
    else: 
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 400



#-------------------Clientes----------------------------------------------#
@app.post('/cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados

    Retorna uma representação dos clientes e comentários associados.
    """
    session = Session()
    cliente = cliente(
        nome=form.nome,
        descricao=form.descricao,
        valor=form.valor,
        imagem_path=form.imagem,
        quantidade=form.quantidade
        )
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # adicionando cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200
    except IntegrityError as e:
        error_msg = "cliente de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):
    """Faz a busca por um cliente a partir do id do cliente

    Retorna uma representação dos clientes e comentários associados.
    """
    cliente_id = query.id
    logger.debug(f"Coletando dados sobre cliente #{cliente_id}")
    session = Session()
    cliente = session.query(cliente).filter(cliente.id == cliente_id).first()
    if not cliente:
        error_msg = "cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar cliente '{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"cliente econtrado: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

@app.get('/cliente', tags=[cliente_tag],
         responses={"200": ClienteListaViewSchema, "404": ErrorSchema})
def get_clientes():
    """Lista todos os clientes cadastrados na base

    Retorna uma lista de representações de clientes.
    """
    logger.debug(f"Coletando lista de clientes")
    session = Session()
    clientes = session.query(Cliente).all()
    print(clientes)
    if not clientes:
        error_msg = "cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de clientes. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de clientes")
        return apresenta_lista_cliente(clientes), 200
    
@app.delete('/cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_cliente(query: ClienteBuscaSchema):
    """Deleta um cliente a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cliente_id = query.id
    cliente_nome = query.nome

    logger.debug(f"Deletando dados sobre cliente #{cliente_id}")
    session = Session()

    if cliente_id:
        count = session.query(Cliente).filter(Cliente.id == cliente_id).delete()
    else:
        count = session.query(Cliente).filter(Cliente.nome == cliente_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado cliente #{cliente_id}")
        return {"mesage": "cliente removido", "id": cliente_id}
    else: 
        error_msg = "cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar cliente #'{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    
    
    
    #-------------------Pedido----------------------------------------------#
    
    
@app.post('/pedido', tags=[pedido_tag],
          responses={"200": PedidoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pedido(form: PedidoSchema):
    """Adiciona um novo pedido à base de dados

    Retorna uma representação dos pedidos e comentários associados.
    """
    session = Session()
    pedido = pedido(
        nome=form.nome,
        descricao=form.descricao,
        valor=form.valor,
        imagem_path=form.imagem,
        quantidade=form.quantidade
        )
    logger.debug(f"Adicionando pedido de nome: '{pedido.nome}'")
    try:
        # adicionando pedido
        session.add(pedido)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado pedido de nome: '{pedido.nome}'")
        return apresenta_pedido(pedido), 200
    except IntegrityError as e:
        error_msg = "pedido de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar pedido '{pedido.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar pedido '{pedido.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/pedido', tags=[pedido_tag],
         responses={"200": PedidoViewSchema, "404": ErrorSchema})
def get_pedido(query: PedidoBuscaSchema):
    """Faz a busca por um pedido a partir do id do pedido

    Retorna uma representação dos pedidos e comentários associados.
    """
    pedido_id = query.id
    logger.debug(f"Coletando dados sobre pedido #{pedido_id}")
    session = Session()
    pedido = session.query(pedido).filter(pedido.id == pedido_id).first()
    if not pedido:
        error_msg = "pedido não encontrado na base :/"
        logger.warning(f"Erro ao buscar pedido '{pedido_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"pedido econtrado: '{pedido.nome}'")
        return apresenta_pedido(pedido), 200

@app.get('/pedido', tags=[pedido_tag],
         responses={"200": PedidoListaViewSchema, "404": ErrorSchema})
def get_pedidos():
    """Lista todos os pedidos cadastrados na base

    Retorna uma lista de representações de pedidos.
    """
    logger.debug(f"Coletando lista de pedidos")
    session = Session()
    pedidos = session.query(pedidos).all()
    print(pedidos)
    if not pedidos:
        error_msg = "pedido não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de pedidos. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de pedidos")
        return apresenta_lista_pedido(pedidos), 200
    
@app.delete('/pedido', tags=[pedido_tag],
            responses={"200": PedidoDelSchema, "404": ErrorSchema})
def del_pedido(query: PedidoBuscaSchema):
    """Deleta um pedido a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    pedido_id = query.id
    pedido_nome = query.nome

    logger.debug(f"Deletando dados sobre pedido #{pedido_id}")
    session = Session()

    if pedido_id:
        count = session.query(Pedido).filter(Pedido.id == pedido_id).delete()
    else:
        count = session.query(Pedido).filter(Pedido.nome == pedido_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado pedido #{pedido_id}")
        return {"mesage": "pedido removido", "id": pedido_id}
    else: 
        error_msg = "pedido não encontrado na base :/"
        logger.warning(f"Erro ao deletar pedido #'{pedido_id}', {error_msg}")
        return {"mesage": error_msg}, 400