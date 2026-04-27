from decimal import Decimal
from src.models import Venda
from src.analytics import gerar_relatorio_faturamento, produto_mais_vendido
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

# def test_gerar_tabela_vendas_cobertura(massa_de_dados):
#     resultado = gerar_tabela_vendas(massa_de_dados)
#     assert "Monitor" in resultado
#     assert "R$" in resultado

# def test_produto_mais_vendido_vazio():
#     produto, qtd = produto_mais_vendido([])
#     assert produto == ""
#     assert qtd == 0