# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/000_AIOKafkaImports.ipynb.

# %% auto 0
__all__ = ['dummy']

# %% ../nbs/000_AIOKafkaImports.ipynb 1
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from ._components.meta import export

__all__ = [
    "AIOKafkaConsumer",
    "AIOKafkaProducer",
]

# %% ../nbs/000_AIOKafkaImports.ipynb 2
@export("_dummy")
def dummy() -> None:
    pass