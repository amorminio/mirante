from typing import List,Dict,Tuple
from decimal import Decimal
from src.models import Venda
from datetime import datetime

# Relatório - Faturamento total das vendas
def gerar_relatorio_faturamento(vendas: List[Venda]) -> Decimal:
    if not vendas:
        return Decimal("0.00")

    total = sum(venda.faturamento_total for venda in vendas)

    return total

# Relatório 2 - Filtro de vendas por intervalo de datas
def filtro_por_intervalo(vendas: List[Venda], data_inicial: datetime, data_final: datetime) -> List[Venda]:
    return [v for v in vendas if data_inicial <= v.data_compra <= data_final]
    

# Relatório 3 - Vendas por produto
def vendas_por_produto(vendas: List[Venda]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for v in vendas:
        resultado[v.produto] = resultado.get(v.produto, 0) + v.quantidade
    return resultado


# Relatório 4 - Produto mais vendido
def produto_mais_vendido(vendas: List[Venda]) -> Tuple[str, int]:
    agrupado = vendas_por_produto(vendas)
    if not agrupado:
        return ("Sem vendas", 0)
    
    # chave com o maior valor
    produto_top = max(agrupado, key=agrupado.get)
    return (produto_top, agrupado[produto_top])
    