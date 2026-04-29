from datetime import datetime, timedelta
from tabulate import tabulate
from src.models import Venda
from typing import Dict,List
import argparse

def validar_data(data_str: str) -> datetime:
    try:
        return datetime.strptime(data_str, "%d-%m-%Y")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Formato de data inválido: {data_str}. Use dd-mm-YYYY")


#Tabulação para terminal
def gerar_tabela_vendas(vendas: List[Venda]) -> str:
    dados_tabela = [
        [
            v.data_venda.strftime("%d/%m/%Y"),
            v.produto, 
            v.quantidade, 
            f"R$ {v.preco_unitario:,.2f}",
            f"R$ {v.faturamento_total:,.2f}"
        ]
        for v in vendas
    ]

    cabecalho = [ "Data", "Produto", "Qtd", "Preço Unit.", "Total"]

    return tabulate(dados_tabela, headers=cabecalho, tablefmt="grid", numalign="right")



def gerar_tabela_agrupada(dados_agrupados: Dict[str, int]) -> str:
    dados_formatados = sorted(
        dados_agrupados.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    cabecalhos = ["Produto", "Quantidade Total"]
    mais_vendido = dados_formatados[0]
    
    return tabulate(dados_formatados, headers=cabecalhos, tablefmt="grid")