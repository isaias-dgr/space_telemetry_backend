from dataclasses import fields
from decimal import Decimal
from typing import Any, Type, TypeVar

T = TypeVar("T")


def to_dict(items: Any) -> dict:
    return [item.to_dict() for item in items]


def from_dict(cls: Type[T], data: dict) -> T:
    fieldtypes = {f.name: f.type for f in fields(cls)}
    d = {}
    for f in data:
        if isinstance(data[f], dict):
            o = from_dict(fieldtypes[f], data[f])
        else:
            o = data[f]
        d[f] = o
    return cls(**d)


def convert_floats_to_decimal(obj: Any) -> Any:
    if isinstance(obj, list):
        return [convert_floats_to_decimal(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, float):
        return Decimal(str(obj))  # Convertir float a Decimal
    else:
        return obj
