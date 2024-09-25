from pydantic import BaseModel, ConfigDict 
from typing import Optional, List
from datetime import datetime

class ClienteSchema(BaseModel):
    cliente_id: int = 1
    nome: str = "Alexandre Pereira"
    email: str = "Alexandre.Pereira@teste.com"
    cep: str = "95259025"
    endereco: Optional[str] = ""
    bairro: Optional[str] = ""
    localidade: Optional[str] = ""
    uf: Optional[str] = ""    
    
    model_config = ConfigDict(from_attributes=True) 
         
class ClienteBuscaSchema(BaseModel):
  id: Optional[int] = 1
  nome: Optional[str] = "Alexandre Pereira"
  
  
class ClienteViewSchema(BaseModel):
    id: int = 1
    nome: str = "Alexandre Pereira"
    
class ClienteDelSchema(BaseModel):
    id: int
    nome: str = "Alexandre Pereira"
    
def apresenta_cliente(cliente):
     
    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "email": cliente.email,
        "cep": cliente.cep,
        "endereco": cliente.endereco,
        "bairro": cliente.bairro,
        "localidade": cliente.localidade,
        "uf": cliente.uf
    }
    
class ClienteListaViewSchema(BaseModel):
    clientes: List[ClienteViewSchema]

def apresenta_lista_cliente(clientes):
    result = []
    for cliente in clientes:
        result.append(apresenta_cliente(cliente))
    return {"clientes": result}