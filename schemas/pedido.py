from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List

class PedidoSchema(BaseModel):
    id_cliente: int = 1
    id_produto: int = 1
    
class PedidoBuscaSchema(BaseModel):
  id: Optional[int] = 1

class PedidoViewSchema(BaseModel):
  id: int = 1
  
  
class PedidoDelSchema(BaseModel):
  id: int
  
def apresenta_pedido(pedido): 
    return {
        "id": pedido.id,
        "id_cliente": pedido.id_cliente,
        "id_produto": pedido.id_produto        
    }
    
class PedidoListaViewSchema(BaseModel):
    pedidos: List[PedidoViewSchema]
    
def apresenta_lista_pedido(Pedidos):
    result = []
    for pedido in Pedidos:
        result.append(apresenta_pedido(pedido))
    return {"pedidos": result}