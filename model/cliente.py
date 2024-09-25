from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from sqlalchemy.orm import relationship
from typing import Union

from  model import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140), unique=True, nullable=False)
    email = Column(String(4000), nullable=False)
    cep = Column(String(12), nullable=False)
    endereco = Column(String(4000),nullable=True)
    bairro = Column(String(4000), nullable=True)
    localidade = Column(String(4000),nullable=True)
    uf = Column(String(2), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now)

    pedidos = relationship("Pedido")

    def __init__(self, nome:str, email:str, cep:str , endereco:str, bairro: str, localidade: str, uf:str,
        data_nascimento:Union[DateTime, None] = None, data_insercao:Union[DateTime, None] = None):
        
        self.nome = nome
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        if data_nascimento:
            self.data_nascimento = data_nascimento
        if data_insercao:
            self.data_insercao = data_insercao
