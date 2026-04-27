import csv
from typing import List,Iterable
from decimal import Decimal
from src.models import Venda
from .logger import configurar_logger, get_logger
from typing import Optional
from datetime import datetime

logger = get_logger(__name__)

def parse_vendas(
        dados_csv: Iterable[str],
        inicio: Optional[datetime] = None,
        fim: Optional[datetime] = None
        ) -> List[Venda]:
    
    
    linhas = csv.DictReader(dados_csv)
    vendas: List[Venda] = []
    
    print('Linhas>>',linhas)
    for linha in linhas:
        print('passo 2')
        try:
            if not linha["data_venda"]:
                logger.warning(f"Linha com data vazia ignorada: {linha}")
                continue

            data_venda = datetime.strptime(linha["data_venda"], "%d/%m/%Y")

            if inicio and data_venda < inicio:
                continue
            if fim and data_venda > fim:
                continue

            vendas.append(
                Venda(
                    produto=linha["produto"],
                    quantidade=int(linha["quantidade"]),
                    preco_unitario=Decimal(linha["preco_unitario"]),
                    data_venda=data_venda
                )
            )
            
        except (ValueError, KeyError) as e:
            logger.error(f"Erro ao processar linha {linha}: {e}")
    
    logger.info(f"Foram processadas {len(vendas)} vendas")    
    return vendas


def vendas_por_produto(vendas: List[Venda]) -> dict[str, Decimal]:
    
    vendas_por_produto = defaultdict(Decimal)
    
    for venda in vendas:
        vendas_por_produto[venda.produto] += venda.faturamento_total
    
    logger.info(f"Foram processadas {len(vendas_por_produto)} vendas")
    
    return vendas_por_produto