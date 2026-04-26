from decimal import Decimal
from src.models import Venda
from src.analytics import gerar_relatorio_faturamento

def test_gerar_relatorio_faturamento():
    vendas = [
        Venda("p1", 2, Decimal("510.00")),
        Venda("p2", 3, Decimal("1345.00")),
        Venda("p3", 3, Decimal("700.00")),
        Venda("p4", 3, Decimal("500.00")),
    ]
    relatorio = gerar_relatorio_faturamento(vendas)
    assert relatorio == Decimal("8655.00")