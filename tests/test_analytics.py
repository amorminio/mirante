from decimal import Decimal
from src.models import Venda
from src.analytics import gerar_relatorio_faturamento
from datetime import datetime

def test_gerar_relatorio_faturamento():
    vendas = [
        Venda("p1", 2, Decimal("100.00"), datetime(2025,12,31)),
        Venda("p2", 1, Decimal("100.00"), datetime(2025,12,31)),
        Venda("p3", 3, Decimal("100.00"), datetime(2025,12,31)),
        Venda("p4", 4, Decimal("100.00"), datetime(2025,12,31)),
    ]
    relatorio = gerar_relatorio_faturamento(vendas)
    assert relatorio == Decimal("1000.00")