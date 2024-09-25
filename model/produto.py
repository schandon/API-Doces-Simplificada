from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from sqlalchemy.orm import relationship
from model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    descricao = Column(String(4000), nullable=True)
    valor = Column(Float, nullable=True)
    imagem_path = Column(String(2048), nullable=True)
    quantidade = Column(Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now)
    valor_total = Column(Float, nullable=True)

    pedidos = relationship("PedidoProduto", back_populates="produto")

    def __init__(self, nome: str, descricao: str, valor: float, quantidade: int,
                 imagem_path: str, data_insercao: Union[DateTime, None] = None):
        
        self.nome = nome
        self.descricao = descricao
        self.valor = valor  # Corrigido para 'valor'
        self.quantidade = quantidade
        self.imagem_path = imagem_path
        if data_insercao:
            self.data_insercao = data_insercao
        self.atualizar_valor_total()  

    def atualizar_valor_total(self):
        if self.quantidade is not None and self.valor is not None:  # Corrigido para 'valor'
            self.valor_total = self.quantidade * self.valor
        else:
            self.valor_total = 0
