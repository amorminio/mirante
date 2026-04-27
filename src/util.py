from datetime import datetime, timedelta

def validar_data(data_str: str) -> datetime:
    try:
        return datetime.strptime(data_str, "%d-%m-%Y")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Formato de data inválido: {data_str}. Use dd-mm-YYYY")