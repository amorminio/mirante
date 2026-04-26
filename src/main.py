import os
from src.processing import parse_vendas
from src.analytics import gerar_relatorio_faturamento
from charset_normalizer import from_path


def main():
   
    #caminho = input("Digite o caminho do arquivo CSV: ")
    caminho = "data/exemplo1.csv"
    codificacao = detectar_encoding(caminho)
    print(f"Codificação detectada: {codificacao}")
    
    try:
        print("Iniciando processamento...")
        with open(caminho, mode="r", encoding=codificacao) as arquivo:
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


if __name__ == "__main__":
    main()