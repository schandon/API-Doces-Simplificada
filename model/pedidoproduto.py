from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from model import Base


class PedidoProduto(Base):
    __tablename__ = 'pedido_produto'

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.pk_pedido'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.pk_produto'), nullable=False)

    # Relacionamento entre PedidoProduto e Pedido
    pedido = relationship("Pedido", back_populates="produtos")

    # Relacionamento entre PedidoProduto e Produto
    produto = relationship("Produto", back_populates="pedidos")
