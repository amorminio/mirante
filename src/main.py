import os
from src.processing import parse_vendas
from src.analytics import gerar_relatorio_faturamento

def main():
    
    caminho = "data/exemplo1.csv"
    #caminho = input("Digite o caminho do arquivo CSV: ")
    
    try:
        print("Iniciando processamento...")
        with open(caminho, mode="r", encoding="utf-8",errors="replace") as arquivo:
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

if __name__ == "__main__":
    main()