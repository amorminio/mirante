import io
from decimal import Decimal
from src.models import Venda
from src.processing import parse_vendas


def test_linha_csv_para_objeto_venda():
    mock_data = "produto,quantidade,preco_unitario,data_venda\nTeclado,2,50.00,27-04-2026"
    buffer = io.StringIO(mock_data)
    resultado = parse_vendas(buffer)
    
    print('resultado>>',resultado)
    
    assert len(resultado) == 1
    assert resultado[0].produto == "Teclado"
    assert resultado[0].quantidade == 2
    assert resultado[0].data_venda == datetime(2026, 4, 27)
    
    
    