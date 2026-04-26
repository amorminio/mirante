from typing import List
from decimal import Decimal
from src.models import Venda

def gerar_relatorio_faturamento(vendas: List[Venda]) -> Decimal:
    """
    Calcula o faturamento total da lista de vendas.
    """

    if not vendas:
        return Decimal("0.00")

    total = sum(venda.faturamento_total for venda in vendas)

    return total
