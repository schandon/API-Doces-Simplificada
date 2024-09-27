from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from model import Base

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column("pk_pedido", Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.pk_cliente'))
    id_produto = Column(Integer, ForeignKey('produto.pk_produto'))
    cliente = relationship("Cliente")
    produto = relationship("Produto")


    def __init__(self, id_cliente, id_produto):
        self.id_cliente = id_cliente
        self.id_produto = id_produto