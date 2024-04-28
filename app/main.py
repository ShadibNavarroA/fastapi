from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from typing import List

from fastapi import FastAPI, Depends

app = FastAPI()


class Ingredientes:
    def __init__(self, nombre: str, cantidad: int):
        self.nombre = nombre
        self.cantidad = cantidad



class SandwichPreparationStrategy(ABC):
    @abstractmethod
    def preparar_sandwich(self, ingredientes: List[Ingredientes]) -> str:
        pass



class BasicSandwichPreparation(SandwichPreparationStrategy):
    def preparar_sandwich(self, ingredientes: List[Ingredientes]) -> str:
        sandwich = "Preparando sándwich básico con los siguientes ingredientes:\n"
        sandwich += "- pan\n"
        for ingrediente in ingredientes:
            sandwich += f"- {ingrediente.nombre} x{ingrediente.cantidad}\n"
        sandwich += "- pan\n"
        return sandwich



class SpecialSandwichPreparation(SandwichPreparationStrategy):
    def preparar_sandwich(self, ingredientes: List[Ingredientes]) -> str:
        sandwich = "Preparando sándwich especial con los siguientes ingredientes:\n"
        sandwich += "- pan integral\n"
        for ingrediente in ingredientes:
            sandwich += f"- {ingrediente.nombre} x{ingrediente.cantidad}\n"
        sandwich += "- pan integral\n"
        return sandwich



class SandwichPreparationContext:
    def __init__(self, strategy: SandwichPreparationStrategy):
        self._strategy = strategy

    def preparar_sandwich(self, ingredientes: List[Ingredientes]) -> str:
        return self._strategy.preparar_sandwich(ingredientes)




ingredientes = [Ingredientes("Jamón", 2), Ingredientes("Queso", 1)]

@app.get("/special")
def get_special():
    special = SpecialSandwichPreparation()
    context = SandwichPreparationContext(special)
    print(context.preparar_sandwich(ingredientes))

@app.get("/basic")
def get_basic():
    basic = BasicSandwichPreparation()
    context = SandwichPreparationContext(basic)
    print(context.preparar_sandwich(ingredientes))


