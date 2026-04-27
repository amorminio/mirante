import io
from decimal import Decimal
from src.models import Venda
from src.processing import parse_vendas
from datetime import datetime
from src.util import validar_data
import pytest
import argparse


def test_parse_vendas():
    mock_data = "produto,quantidade,preco_unitario,data_venda\nTeclado,7,224.34,08/05/2023"
    
    buffer = io.StringIO(mock_data)
    resultado = parse_vendas(buffer)
    
    assert len(resultado) == 1
    assert resultado[0].produto == "Teclado"
    assert resultado[0].quantidade == 7
    assert resultado[0].data_venda == datetime(2023, 5, 8)
    assert resultado[0].preco_unitario == Decimal("224.34")
    
def test_parse_vendas_cobre_erros_e_avisos():
    conteudo_csv = (
        "produto,quantidade,preco_unitario,data_venda\n"
        "Mouse,10,50.0,27/04/2026\n"          
        "Teclado,5,100.0,\n"                  
        "Erro,nao_numero,0.0,01/01/2026\n"    
        ",,,01/01/2026"                       
    )
    arquivo_falso = io.StringIO(conteudo_csv)
    
    vendas = parse_vendas(arquivo_falso)
    
    # Validações
    assert len(vendas) == 1
    assert vendas[0].produto == "Mouse"


def test_validar_data_sucesso():
    data = validar_data("27-04-2026")
    assert data.day == 27
    assert data.year == 2026

def test_validar_data_erro():
    with pytest.raises(argparse.ArgumentTypeError):
        validar_data("data-invalida")

def test_parse_vendas_filtros_data():
    dados = [
        "produto,quantidade,preco_unitario,data_venda",
        "Antigo,1,10.0,01/01/2020",
        "Novo,1,10.0,01/01/2026"
    ]
    inicio = datetime(2025, 1, 1)
    
    # Testa apenas início (vai ignorar o 'Antigo')
    vendas = parse_vendas(dados, inicio=inicio)
    assert len(vendas) == 1
    assert vendas[0].produto == "Novo"