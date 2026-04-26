import os
import argparse
from src.processing import parse_vendas
from src.analytics import gerar_relatorio_faturamento
from charset_normalizer import from_path

def main():

    caminho_csv = parser_config()
    codificacao = detectar_encoding(caminho_csv)
    
    try:
        print("Iniciando processamento...")
        with open(caminho_csv, mode="r", encoding=codificacao) as arquivo:
            print("Lendo arquivo...")
            vendas = parse_vendas(arquivo)
            print("Processando vendas...")
            relatorio = gerar_relatorio_faturamento(vendas)
            print(relatorio)
            print("Processamento concluído!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

def detectar_encoding(caminho_arquivo:str) -> str:
    resultado = from_path(caminho_arquivo).best()
    if resultado:
        return resultado.encoding
    return "utf-8"

def parser_config():
    parser = argparse.ArgumentParser(
        description="Processador de Vendas: Lê um CSV e gera um relatório de faturamento."
    )

    parser.add_argument(
        "arquivo", 
        help="Caminho para o arquivo CSV de vendas"
    )

    args = parser.parse_args()
    caminho_csv = args.arquivo

    if not os.path.exists(caminho_csv):
        print(f"Erro: O arquivo '{caminho_csv}' não foi encontrado.")
        sys.exit(1)

    return caminho_csv

if __name__ == "__main__":
    main()