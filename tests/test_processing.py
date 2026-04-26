import io
from decimal import Decimal
from src.models import Venda
from src.processing import parse_vendas


def test_linha_csv_para_objeto_venda():
    mock_data = "produto,quantidade,preco_unitario\nTeclado,2,50.00"
    buffer = io.StringIO(mock_data)
    resultado = parse_vendas(buffer)
    
    assert len(resultado) == 1
    assert resultado[0].produto == "Teclado"
    assert resultado[0].quantidade == 2
    assert resultado[0].faturamento_total == Decimal("100.00")
    
    
    