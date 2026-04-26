import csv
from typing import List,Iterable
from decimal import Decimal
from src.models import Venda

def parse_vendas(dados_csv: Iterable[str]) -> List[Venda]:
    leitor = csv.DictReader(dados_csv)
    vendas = []
    for linha in leitor:
        try:
            vendas.append(
                Venda(
                    produto=linha["produto"],
                    quantidade=int(linha["quantidade"]),
                    preco_unitario=Decimal(linha["preco_unitario"])
                )
            )
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar linha {linha}: {e}")
    return vendas