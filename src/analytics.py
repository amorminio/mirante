from typing import List,Dict,Tuple
from decimal import Decimal
from src.models import Venda
from datetime import datetime
from src.util import gerar_tabela_agrupada, gerar_tabela_vendas

# Relatório - Faturamento total das vendas
def gerar_relatorio_faturamento(vendas: List[Venda]) -> Decimal:
    if not vendas:
        return Decimal("0.00")

    total = sum(venda.faturamento_total for venda in vendas)

    print(gerar_tabela_vendas(vendas))
    print(f"Total de faturamento: R$ {total:,.2f}")
    return total

# Relatório 2 - Filtro de vendas por intervalo de datas
def filtro_por_intervalo(vendas: List[Venda], data_inicial: datetime, data_final: datetime) -> List[Venda]:
    return [v for v in vendas if data_inicial <= v.data_compra <= data_final]
    

# Relatório 3 - Vendas por produto
def vendas_por_produto(vendas: List[Venda]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for v in vendas:
        resultado[v.produto] = resultado.get(v.produto, 0) + v.quantidade
    
    print(gerar_tabela_agrupada(resultado))
    return resultado


# Relatório 4 - Produto mais vendido
def produto_mais_vendido(vendas: List[Venda]) -> Tuple[List[str], int]:
    agrupado = vendas_por_produto(vendas)
    
    if not agrupado:
        return (["Sem vendas"], 0)

    # 1. Descobre qual é a maior quantidade vendida
    vendas_maximas = max(agrupado.values())
    
    # 2. Filtra todos os produtos que atingiram essa quantidade
    produtos_top = [
        produto for produto, quantidade in agrupado.items() 
        if quantidade == vendas_maximas
    ]
    print(f"\n\nProduto(s) mais vendido(s): {produtos_top}")
    print(f"\n\n")
    
    return (produtos_top, vendas_maximas)


def mais_vendidos(vendas: List[Venda]):
    agrupado = sorted(vendas_por_produto(vendas))
    first = agrupado[0]
    
    result = [x for x in agrupado if x[1] == first[1]]
    return result
    
    






