from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List


class ProdutoSchema(BaseModel):
    nome: str = "Bolo de Laranja"
    descricao: Optional[str] = "Bolo com sabor de laranja, ser cobertura. "
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 300.10
    quantidade: int = 1

class ProdutoBuscaSchema(BaseModel):
    id: Optional[int] = 1
    # nome: Optional[str] = "Bolo de Laranja"


class ProdutoViewSchema(BaseModel):
    id: int = 1
    nome: str = "Bolo de Laranja"
    descricao: Optional[str] = "Bolo com sabor de laranja, ser cobertura. "
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 300.10
    nota_media: int = 0


class ProdutoDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_produto(produto):
    nota_media = 0
     
    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "imagem": produto.imagem_path,
        "valor": float(produto.valor),
        "nota_media": nota_media,
    }


class ProdutoListaViewSchema(BaseModel):
    produtos: List[ProdutoViewSchema]


def apresenta_lista_produto(produtos):
    result = []
    for produto in produtos:
        result.append(apresenta_produto(produto))
    return {"produtos": result}
