import pytest
import sys
from src.main import main, parser_config

def test_parser_config_sucesso(monkeypatch, tmp_path):
    
    csv_fake = tmp_path / "dados.csv"
    csv_fake.write_text("header")
    
    monkeypatch.setattr(sys, "argv", ["vendas-cli", str(csv_fake), "--inicio", "01-01-2026"])
    
    config = parser_config()
    assert config["arquivo"] == str(csv_fake)
    assert config["inicio"].day == 1

def test_main_fluxo_completo(monkeypatch, tmp_path):
    csv_fake = tmp_path / "vendas.csv"
    csv_fake.write_text("produto,quantidade,preco_unitario,data_venda\nMouse,1,50.0,27-04-2026")
    
    monkeypatch.setattr(sys, "argv", ["vendas-cli", str(csv_fake)])
    
    try:
        main()
    except SystemExit:
        pass 