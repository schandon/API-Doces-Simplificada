from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from model import Base

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column("pk_pedido", Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.pk_cliente'), nullable=False)

    # Relacionamento com Cliente
    cliente = relationship("Cliente", backref="pedidos")

    # Relacionamento com a tabela de junção PedidoProduto
    produtos = relationship("PedidoProduto", back_populates="pedido")