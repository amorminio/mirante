import os
import argparse
from charset_normalizer import from_path
from typing import Dict,Any
from datetime import datetime
from .logger import configurar_logger, get_logger
from .util import validar_data
from src.processing import parse_vendas
from src.analytics import gerar_relatorio_faturamento, vendas_por_produto

def main() -> None:

    configurar_logger()
    params = parser_config()
    logger = get_logger(__name__)
    
    caminho_csv = params["arquivo"]
    inicio = params["inicio"]
    fim = params["fim"]
    
    codificacao = detectar_encoding(caminho_csv)
    
    try:
        logger.info(f"Iniciando processamento: {caminho_csv}")
        logger.info('Parâmetros informados: %s', params)
        
        with open(caminho_csv, mode="r", encoding=codificacao) as arquivo:
            logger.info("Lendo arquivo")
            logger.info("Processando vendas...")
            
            vendas = parse_vendas(
                arquivo,
                inicio=inicio,
                fim=fim
            )
            
            relatorio_faturamento = gerar_relatorio_faturamento(vendas)
            relatorio_vendas_por_produto = vendas_por_produto(vendas)
           
            logger.info("Processamento concluído!")
    except FileNotFoundError:
        logger.error("Arquivo não encontrado!")
    except Exception as e:
        logger.error(f"Erro ao processar arquivo: {e}")

def detectar_encoding(caminho_arquivo:str) -> str:
    resultado = from_path(caminho_arquivo).best()
    
    if resultado:
        return resultado.encoding
    return "utf-8"


#Definição dos argumentos do script
def parser_config() -> Dict[str,Any]:
    parser = argparse.ArgumentParser(
        description="Processador de Vendas: Lê um CSV e gera um relatório de faturamento."
    )

    parser.add_argument("arquivo", help="Caminho para o arquivo CSV")
    parser.add_argument("--inicio", help="Data inicial do período (dd-mm-YYYY)", type=validar_data)
    parser.add_argument("--fim", help="Data final do período (dd-mm-YYYY)", type=validar_data)

    args = parser.parse_args()
    caminho_csv = args.arquivo

    if not os.path.exists(caminho_csv):
        parser.error(f"O arquivo '{caminho_csv}' não foi encontrado.")

    configs = vars(args)
    
    return configs

if __name__ == "__main__":
    main()