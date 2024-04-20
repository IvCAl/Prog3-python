from __future__ import annotations
from enum import Enum

class Cambio(Enum):
    eur=1.00
    usd=1.07
    yen=164.99
    ars=926.04

class Monedas:
    cantidad:float
    def __init__(self,cambio:Cambio,cantidad=0):
        self.moneda=cambio
        self.cantidad=cantidad
    def __str__(self) -> str:
        return f"{self.moneda.name}: {self.cantidad}"
    def sumarMonedas(monedaDestino:Monedas,monedaOrigen:Monedas):
        cantidadDestino:float=monedaOrigen.cantidad*monedaDestino.moneda.value/monedaOrigen.moneda.value
        return Monedas(monedaDestino.moneda,cantidadDestino+monedaDestino.cantidad)

a=Monedas(Cambio.ars,27)
b=Monedas(Cambio.yen,0)

c=Monedas.sumarMonedas(b,a)
print(c)