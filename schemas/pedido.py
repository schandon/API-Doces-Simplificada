from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class PedidoSchema(BaseModel):
    cliente_id: int  = 1
    produto_id: int = 1
    
class PedidoBuscaSchema(BaseModel):
  id: Optional[int] = 1

class PedidoViewSchema(BaseModel):
  id: int = 1
  
  
class PedidoDelSchema(BaseModel):
  id: int
  
def apresenta_pedido(pedido): 
    return {
        "id": pedido.id,
        "cliente_id": pedido.cliente_id,
        "produto_id": pedido.produto_id        
    }
    
class PedidoListaViewSchema(BaseModel):
    pedidos: List[PedidoViewSchema]
    
def apresenta_lista_pedido(Pedidos):
    result = []
    for pedido in Pedidos:
        result.append(apresenta_pedido(pedido))
    return {"pedidos": result}