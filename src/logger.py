import logging
import sys

def configurar_logger(nivel=logging.INFO) -> None:
    formato="%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=nivel,
        format=formato,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("vendas_cli.log", encoding="utf-8"),
        ]
    )

def get_logger(nome) -> logging.Logger:
    return logging.getLogger(nome)