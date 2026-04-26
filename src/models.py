from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Venda:
    produto: str
    quantidade: int
    preco_unitario: Decimal
    
    @property
    def faturamento_total(self) -> Decimal:
        return self.quantidade * self.preco_unitario