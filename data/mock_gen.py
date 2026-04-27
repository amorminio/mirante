import csv
import random

produtos_base = [
    "Mouse Gamer RGB", "Teclado Mecânico", "Monitor 24 Pol", "SSD 480GB", 
    "Memória RAM 8GB", "Cabo HDMI 2m", "Mousepad Extra Large", "Headset USB",
    "Webcam 1080p", "Adaptador Wi-Fi", "Processador i5", "Placa de Vídeo",
    "Fonte 500W", "Gabinete ATX", "Cooler Fan 120mm", "Pendrive 64GB",
    "Roteador Dual Band", "Switch 8 Portas", "Cabo de Rede Cat6", "Pasta Térmica"
]

def gerar_dados_teste(nome_arquivo, num_linhas=300):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(["produto", "quantidade", "preco_unitario", "data_venda"])
        
        for _ in range(num_linhas):
            produto = random.choice(produtos_base)
            quantidade = random.randint(1, 10)
            preco = round(random.uniform(10.0, 500.0), 2)
            data_venda = f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/{random.randint(2020, 2026):04d}"
            escritor.writerow([produto, quantidade, preco,data_venda])

gerar_dados_teste('vendas_100_linhas.csv')