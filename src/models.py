from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime


@dataclass(frozen=True)
class Venda:
    produto: str
    quantidade: int
    preco_unitario: Decimal
    data_venda: datetime
    
    @property
    def faturamento_total(self) -> Decimal:
        return self.quantidade * self.preco_unitario